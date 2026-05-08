# NLP-Based Document Intelligence System

An end-to-end AI-powered document understanding system that extracts structured information from scanned documents and forms using OCR, NLP, Named Entity Recognition (NER), and FastAPI.

---

# 🌐 Live Demo

🔗 https://nlp-document-intelligence-system.onrender.com/docs

> ⚠️ First request may take some time because the project is deployed on Render free tier.

---

# 🧠 Project Overview

This project automates document understanding by converting scanned forms and document images into structured JSON data.

The system performs:

- OCR-based text extraction
- NLP preprocessing
- Named Entity Recognition (NER)
- Key-value extraction
- Structured JSON API responses

---

# 🔥 Features

✅ OCR-based text extraction using Tesseract OCR  
✅ Custom NER model training using spaCy  
✅ FUNSD dataset integration  
✅ FastAPI REST API  
✅ Swagger API documentation  
✅ Key-value pair extraction  
✅ Structured JSON output  
✅ Modular NLP pipeline architecture  
✅ Docker deployment support  
✅ Cloud deployment on Render

---

# 🏗️ Project Architecture

```text
Document Upload
       ↓
OCR Engine
       ↓
Text Cleaning
       ↓
NER Model
       ↓
Entity Extraction
       ↓
Post Processing
       ↓
Key-Value Extraction
       ↓
JSON API Response
```

---

# 📂 Project Structure

```text
nlp-document-intelligence-system/
│
├── api/
│   ├── app.py
│   ├── routes.py
│   └── schemas.py
│
├── data/
│   ├── annotations/
│   ├── processed/
│   └── raw/
│
├── deployment/
│   ├── Dockerfile
│   └── docker-compose.yml
│
├── models/
│   └── spacy_ner_model/
│
├── sample_documents/
│   └── form_sample.png
│
├── sample_outputs/
│   └── output.json
│
├── src/
│   ├── data_ingestion.py
│   ├── entity_extraction.py
│   ├── evaluate_model.py
│   ├── inference_pipeline.py
│   ├── key_value_extraction.py
│   ├── ocr_engine.py
│   ├── post_processing.py
│   ├── prepare_training_data.py
│   ├── preprocess.py
│   └── train_ner_model.py
│
├── tests/
│
├── .gitignore
├── main.py
├── README.md
├── render.yaml
└── requirements.txt
```

---

# ⚙️ Tech Stack

| Area | Technology |
|---|---|
| OCR | Tesseract OCR |
| NLP | spaCy |
| API Framework | FastAPI |
| Dataset | FUNSD |
| Image Processing | OpenCV |
| Deployment | Docker + Render |
| Language | Python |

---

# 📦 Dataset

This project uses the FUNSD dataset for training and evaluation.

Dataset Link:

https://guillaumejaume.github.io/FUNSD/

---

# 🚀 Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Nimalan07/nlp-document-intelligence-system.git
```

```bash
cd nlp-document-intelligence-system
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Install Tesseract OCR

Download and install:

https://github.com/UB-Mannheim/tesseract/wiki

After installation, update Tesseract path inside:

```text
src/ocr_engine.py
```

---

## 4️⃣ Train Model

```bash
python src/train_ner_model.py
```

---

## 5️⃣ Run Application

```bash
python main.py
```

---

# 📘 API Documentation

After starting the server:

```text
http://127.0.0.1:8000/docs
```

---

# 📤 Example API Response

```json
{
    "date:": "september 21 1976",
    "filter length": "20 mm true plastic rod length"
}
```

---

# 🧠 NLP Pipeline

## OCR Engine

Extracts raw text from scanned documents using Tesseract OCR.

---

## Text Preprocessing

Cleans OCR noise:
- removes extra spaces
- removes unwanted symbols
- normalizes text

---

## Named Entity Recognition (NER)

Custom spaCy model trained using FUNSD annotations.

Recognizes:
- QUESTION
- ANSWER
- HEADER

---

## Post Processing

Improves prediction quality by:
- removing noisy spans
- removing duplicates
- cleaning extracted entities

---

## Key-Value Extraction

Converts extracted entities into structured JSON format.

Example:

```json
{
    "question": "answer"
}
```

---

# 🐳 Docker Support

Build Docker image:

```bash
docker build -t nlp-document-intelligence-system .
```

Run container:

```bash
docker run -p 8000:8000 nlp-document-intelligence-system
```

---

# ☁️ Deployment

The project is deployed on Render using Docker.

Deployment platform:

https://render.com/

---

# 🎯 Future Improvements

- LayoutLM integration
- PDF support
- Multilingual OCR
- Better entity pairing
- Transformer-based NER
- Frontend UI
- Database integration
- Batch document processing

---

# 📸 Sample Output

```json
{
    "QUESTION": [
        {
            "text": "date:",
            "start": 0,
            "end": 5
        }
    ],
    "ANSWER": [
        {
            "text": "september 21 1976",
            "start": 6,
            "end": 25
        }
    ]
}
```

---

# 👨‍💻 Author

Nimalan Mani M

---

# ⭐ If you found this project useful

Give this repository a star ⭐