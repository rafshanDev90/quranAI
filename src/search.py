import chromadb
from chromadb.utils import embedding_functions

def query_quran(user_query):
    # 1. Connect to the local DB
    client = chromadb.PersistentClient(path="./quran_vectordb")
    
    # 2. Use the SAME model we used for embedding
    model_name = "all-MiniLM-L6-v2"
    emb_fn = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=model_name)
    
    collection = client.get_collection(name="quran_verses", embedding_function=emb_fn)

    # 3. Search for the top 3 most relevant ayahs
    results = collection.query(
        query_texts=[user_query],
        n_results=3
    )
    
    return results

if __name__ == "__main__":
    query = input("Ask a question about the Quran: ")
    res = query_quran(query)
    
    for i in range(len(res['documents'][0])):
        print(f"\nMatch {i+1}:")
        print(f"Text: {res['documents'][0][i]}")
        print(f"Source: Surah {res['metadatas'][0][i]['surah_name']} Ayah {res['metadatas'][0][i]['ayah_no']}")
