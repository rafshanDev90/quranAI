from fastapi import FastAPI
from search import query_quran
from orchestrator import generate_answer

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Bayyan AI API"}

@app.get("/search")
def search(q: str):
    # 1. Get raw vector search results for the UI cards
    raw_results = query_quran(q)
    
    # 2. Get the LLM generated answer from the orchestrator
    llm_answer = generate_answer(q)

    # 3. Format the verses for the UI
    formatted_matches = []
    # ChromaDB returns lists of lists, so we access index [0]
    docs = raw_results.get('documents', [[]])[0]
    metas = raw_results.get('metadatas', [[]])[0]

    for i in range(len(docs)):
        formatted_matches.append({
            "text": docs[i],
            "surah": metas[i]['surah_name'],
            "ayah": metas[i]['ayah_no'],
            "arabic": metas[i]['arabic_text']
        })
    
    return {
        "query": q, 
        "answer": llm_answer,
        "matches": formatted_matches
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
