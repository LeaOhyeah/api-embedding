---
# 🚀 **Sentence Embedding API**  

Sentence Embedding API adalah layanan berbasis **FastAPI** yang mengubah teks menjadi embedding menggunakan **Sentence Transformers** dan melakukan semantic searching dengan Postgresql.  

## 📌 **Fitur**  
✅ **Konversi teks ke embedding** menggunakan model `all-MiniLM-L6-v2` dan `multi-qa-mpnet-base-dot-v1`.  
✅ **Pencarian berbasis semantic search** menggunakan PostgreSQL dan vektor embedding.  
✅ **Dokumentasi API otomatis dengan Swagger dan Redoc**.  
✅ **Format output JSON yang mudah diintegrasikan**.  

## 🛠 **Teknologi yang Digunakan**  
- **Python 3.12**  
- **FastAPI**  
- **Sentence Transformers**  
- **Uvicorn** (untuk menjalankan server)  
- **PostgreSQL** (jika menggunakan fitur pencarian)  

---

## 🚀 **Instalasi & Menjalankan Server**  

### 1️⃣ **Clone Repository**  
```bash
git clone https://github.com/leaohyeah/api-embedding.git
cd api-embedding
```

### 2️⃣ **Buat Virtual Environment**  
```bash
python3 -m venv myenv
source myenv/bin/activate  # Linux/macOS
myenv\Scripts\activate     # Windows
```

### 3️⃣ **Instal Dependensi**  
```bash
pip install -r requirements.txt
```

### 4️⃣ **Jalankan Server FastAPI**  
```bash
uvicorn api:app --reload
```
Server akan berjalan di: **`http://127.0.0.1:8000`**  

---

## 📡 **Contoh API Endpoint**  

### 🔹 **Konversi Teks ke Embedding (300D)**  
**Endpoint:** `POST /embed`  

#### **📥 Request (JSON)**  
```json
{
  "text": "Saya sangat senang hari ini!"
}
```

#### **📤 Response (JSON)**  
```json
{
  "status": "success",
  "message": "Embedding generated successfully",
  "data": {
    "embedding": [0.12, -0.45, 0.78, ...]
  }
}
```

---

## 📜 **Dokumentasi API Swagger**  
Dokumentasi API tersedia secara otomatis di:  

🔹 **Swagger UI:** [`http://127.0.0.1:8000/docs`](http://127.0.0.1:8000/docs)  
🔹 **ReDoc UI:** [`http://127.0.0.1:8000/redoc`](http://127.0.0.1:8000/redoc)  

Gunakan Swagger untuk mencoba API secara langsung di browser.  

---

## 📄 **Lisensi**  
Proyek ini menggunakan lisensi **MIT**.  

🔥 **Dikembangkan oleh [Lea Alyu/LeaOhyeah](https://github.com/leaohyeah)**  

---
