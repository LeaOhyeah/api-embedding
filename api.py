from fastapi import FastAPI
from sentence_transformers import SentenceTransformer

app = FastAPI()

model = SentenceTransformer('all-MiniLM-L6-v2')

@app.get("/deteksi_emosi/")
def deteksi_emosi(teks: str):
    embedding = model.encode(teks)
    return {"teks": teks, "embedding": embedding.tolist()}
