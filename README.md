# Sentence Embedding API

🚀 **Sentence Embedding API** adalah layanan berbasis **FastAPI** yang mengubah teks menjadi embedding menggunakan **Sentence Transformers**.

## 📌 Fitur
- **Konversi teks ke embedding** menggunakan model `all-MiniLM-L6-v2`.
- **API cepat & ringan** dengan FastAPI.
- **Format output JSON** untuk mempermudah integrasi.

## 🛠 Teknologi yang Digunakan
- **Python 3.12**
- **FastAPI**
- **Sentence Transformers**
- **Uvicorn** (untuk menjalankan server)

## 🚀 Instalasi & Menjalankan Server

### 1️⃣ **Clone Repository**
```bash
 git clone https://github.com/leaohyeah/api-embeddng.git
 cd sentence-trans
```

### 2️⃣ **Buat Virtual Environment**
```bash
python3 -m venv myenv
source myenv/bin/activate  # Linux/macOS
myenv\Scripts\activate    # Windows
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

## 📡 API Endpoint
### **🔹 Konversi Teks ke Embedding**
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
  "embedding": [0.12, -0.45, 0.78, ...]
}
```

## 📄 Lisensi
Proyek ini menggunakan lisensi **MIT**.

---
🔥 **Dikembangkan oleh [Lea Alyu/LeaOhyeah](https://github.com/leaohyeah)**

