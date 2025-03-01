from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import psycopg2

app = FastAPI(
    title="Semantic Search API",
    description="API untuk melakukan embedding teks dan pencarian semantik menggunakan Sentence Transformers.",
    version="1.0.0",
)

# Load models
model = SentenceTransformer('all-MiniLM-L6-v2')  # 384 dimensi
query_model = SentenceTransformer("multi-qa-mpnet-base-dot-v1")  # 768 dimensi

# Koneksi database PostgreSQL
conn = psycopg2.connect(
    dbname="tokko",
    user="postgres",
    password="konfirmasi11",
    host="localhost",
    port="5432"
)

# Schema untuk input
class TextInput(BaseModel):
    text: str

class SearchInput(BaseModel):
    query: str

@app.post("/embed/", tags=["Embedding"], response_model=dict)
def get_embedding(input_text: TextInput):
    """
    **Generate embedding (vector representation) dari teks input menggunakan model 'all-MiniLM-L6-v2'.**  
    Cocok untuk pencarian berbasis teks pendek.

    - **text**: Kalimat yang akan dikonversi menjadi embedding
    - **Returns**: Vektor dengan dimensi 384
    """
    try:
        embedding = model.encode(input_text.text).tolist()
        return {
            "status": "success",
            "message": "Embedding generated successfully",
            "data": {"embedding": embedding},
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "message": str(e)
        })

@app.post("/embed700/", tags=["Embedding"], response_model=dict)
def get_embedding_700(input_text: TextInput):
    """
    **Generate embedding menggunakan model 'multi-qa-mpnet-base-dot-v1'.**  
    Cocok untuk pencarian berbasis deskripsi produk yang lebih kompleks.

    - **text**: Kalimat yang akan dikonversi menjadi embedding
    - **Returns**: Vektor dengan dimensi 768
    """
    try:
        embedding = query_model.encode(input_text.text).tolist()
        return {
            "status": "success",
            "message": "Embedding generated successfully",
            "data": {"embedding_700": embedding},
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "message": str(e)
        })

@app.post("/search/", tags=["Search"], response_model=dict)
def search_products(input_data: SearchInput):
    """
    **Melakukan pencarian produk berdasarkan deskripsi atau kata kunci menggunakan vector search.**  

    - **query**: Deskripsi produk yang ingin dicari
    - **Returns**: List produk yang paling relevan berdasarkan jarak vektor

    **Contoh Query**:
    ```
    {
        "query": "comfortable sports shoes"
    }
    ```
    """
    try:
        query_embedding = query_model.encode(input_data.query).tolist()
        query_embedding_str = "[" + ",".join(map(str, query_embedding)) + "]"

        with conn.cursor() as cur:
            cur.execute("""
                SELECT id, name, description, price, embedding_700 <=> %s AS distance
                FROM products
                ORDER BY distance ASC
                LIMIT 3;
            """, (query_embedding_str,))

            results = cur.fetchall()
            if not results:
                return {"status": "success", "message": "No products found", "data": []}

            products = [
                {"id": r[0], "name": r[1], "description": r[2], "price": r[3], "distance": r[4]}
                for r in results
            ]

        return {
            "status": "success",
            "message": "Search completed",
            "data": products
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "message": str(e)
        })
