import os
from pymongo import MongoClient
from dotenv import load_dotenv

import chromadb
from chromadb.utils import embedding_functions

# Load environment variables (Create a .env file with your MONGO_URI)
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")

def get_processed_data():
    client = MongoClient(MONGO_URI)
    db = client['Agent']  # Replace with your actual DB name
    collection = db['surahs']          # Replace with your collection name

    # Fetch all Surahs
    surahs = collection.find({})
    
    final_documents = []

    for surah in surahs:
        surah_name = surah.get("transliteration")
        surah_id = surah.get("id") # e.g., 108
        
        # Loop through the verses array in your schema
        for verse in surah.get("verses", []):
            # Create a professional chunk
            chunk = {
                "text": verse.get("translation"), # We embed the English for search
                "metadata": {
                    "surah_name": surah_name,
                    "surah_no": surah_id,
                    "ayah_no": verse.get("id"),
                    "arabic_text": verse.get("text"), # Store Arabic to show in response
                    "id": f"{surah_id}:{verse.get('id')}" # e.g., "108:1"
                }
            }
            final_documents.append(chunk)

    client.close()
    return final_documents

# ... keep your existing get_processed_data() function above ...

def save_to_vector_db(data):
    # 1. Initialize Chroma Client (Creates a local folder 'quran_vectordb')
    client = chromadb.PersistentClient(path="./quran_vectordb")
    
    # 2. Use a free, high-quality embedding model from HuggingFace
    model_name = "all-MiniLM-L6-v2"
    emb_fn = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=model_name)
    
    # 3. Create (or get) a collection
    collection = client.get_or_create_collection(name="quran_verses", embedding_function=emb_fn)

    unique_data = {}
    for item in data:
        unique_id = item['metadata']['id']
        # If ID exists, it will just overwrite with the same data, ensuring uniqueness
        unique_data[unique_id] = item

    clean_list = list(unique_data.values())

    # 4. Prepare data for Chroma
    ids = [item['metadata']['id'] for item in clean_list]
    documents = [item['text'] for item in clean_list]
    metadatas = [item['metadata'] for item in clean_list]

    # 5. Add to database (This handles the embedding generation automatically)
    collection.upsert(
        ids=ids,
        documents=documents,
        metadatas=metadatas
    )
    print("🚀 Data successfully vectorized and saved to ./quran_vectordb")

def save_to_vector_db_v2(data):
    client = chromadb.PersistentClient(path="./quran_vectordb")
    
    model_name = "all-MiniLM-L6-v2"
    emb_fn = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=model_name)
    
    collection = client.get_or_create_collection(name="quran_verses", embedding_function=emb_fn)

    # De-duplicate data using a dictionary
    unique_data = {item['metadata']['id']: item for item in data}
    clean_list = list(unique_data.values())

    ids = [item['metadata']['id'] for item in clean_list]
    documents = [item['text'] for item in clean_list]
    metadatas = [item['metadata'] for item in clean_list]

    # --- FIX: Batch Processing ---
    batch_size = 100  # Small batches are safer for memory and HuggingFace models
    total_items = len(clean_list)
    
    print(f"Total verses to process: {total_items}")

    for i in range(0, total_items, batch_size):
        batch_ids = ids[i : i + batch_size]
        batch_docs = documents[i : i + batch_size]
        batch_metas = metadatas[i : i + batch_size]

        collection.upsert(
            ids=batch_ids,
            documents=batch_docs,
            metadatas=batch_metas
        )
        print(f"✅ Processed batch {i//batch_size + 1}: {i + len(batch_ids)}/{total_items} verses")

    print("🚀 Data successfully vectorized and saved to ./quran_vectordb")


if __name__ == "__main__":
    ayah_data = get_processed_data()
    if ayah_data:
        save_to_vector_db_v2(ayah_data)


