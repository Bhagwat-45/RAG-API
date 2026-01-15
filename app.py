from fastapi import FastAPI
import chromadb
import uuid
import ollama

app = FastAPI()
chroma = chromadb.PersistentClient(path="./db")
collection = chroma.get_or_create_collection("docs")

@app.post("/query")
def query(q:str):
    results = collection.query(query_texts=[q],n_results=1)
    context = results["documents"][0][0] if results["documents"] else ""

    answer = ollama.generate(
        model = "tinyllama",
        prompt= f"Context: {context}/n/nQuestion: {q}/n/nAnswer clearly and concisely:"
    )

    return {"answer": answer["response"]}

@app.post("/add")
def add_knowledge(text: str):
    try:
        doc_id = str(uuid.uuid4())

        collection.add(documents=[text],ids=[doc_id])

        return {
            "status" : "success",
            "message" : "Content added to Knowledge base",
            "id" : doc_id
        }

    except Exception as e:
        return {
            "status" : "error",
            "message": str(e)
        }

@app.get("/health")
def health():
    return {"status" : "okay"}