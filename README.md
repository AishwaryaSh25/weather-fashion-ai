# 🌦️ AI Weather Fashion Stylist

An AI-powered fashion recommendation system that suggests outfits based on real-time weather conditions and fashion trends using **Google Gemini**, **LangGraph**, and **RAG (Retrieval-Augmented Generation)**.

## 🚀 Features

* 🌤️ Weather-based outfit recommendations
* 👗 Fashion recommendations for women
* 🤖 AI-powered styling using Google Gemini
* 🔍 RAG-based retrieval using ChromaDB
* 🧠 Agentic workflow built with LangGraph
* 🎯 Personalized outfit suggestions with reasoning
* 📱 Interactive Streamlit interface

---

## 🛠️ Tech Stack

### AI & Agent Frameworks

* Google Gemini API
* LangChain
* LangGraph
* Retrieval-Augmented Generation (RAG)

### Vector Database

* ChromaDB
* Sentence Transformers

### Frontend

* Streamlit

### Backend

* Python

### Data Processing

* Pandas

---

## 📂 Project Structure

```text
weather-fashion-ai/
│
├── app.py                     # Streamlit UI
├── main.py
├── graph_builder.py           # LangGraph workflow
├── recommendation_node.py     # Recommendation agent
├── tool.py                    # Weather tools
├── season_mapper.py
├── filter_women.py
│
├── rag/
│   ├── create_vectordb.py
│   └── retriever.py
│
├── styles.csv
├── women_fashion.csv
├── women_fashion_50_rows.csv
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/weather-fashion-ai.git
cd weather-fashion-ai
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

Get your Gemini API Key from:

https://makersuite.google.com/app/apikey

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## 🧠 How It Works

1. User enters location and preferences.
2. Weather information is fetched.
3. LangGraph orchestrates the workflow.
4. Relevant fashion items are retrieved from ChromaDB using RAG.
5. Gemini analyzes weather and retrieved fashion data.
6. Personalized outfit recommendations are generated.

---

## 📊 Dataset

* Women's Fashion Dataset
* Custom filtered dataset (`women_fashion_50_rows.csv`)
* Fashion metadata stored in vector embeddings using ChromaDB

---

## 🔮 Future Improvements

* Image-based outfit recommendations
* User profile personalization
* Fashion trend analysis
* Multi-season wardrobe planning
* Outfit image generation

---

## 👩‍💻 Author

**Aishwarya Kumari**

B.Tech Electrical Engineering
IIT (ISM) Dhanbad


