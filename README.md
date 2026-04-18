# 🚀 CareerLens AI — Intelligent Resume & Job Match Analyzer

CareerLens AI is an AI-powered resume evaluation system designed to simulate how recruiters assess candidates — going beyond keyword matching to provide semantic, insight-driven career feedback.

It leverages Natural Language Processing (NLP) and transformer-based models to analyze resumes, compare them with job descriptions, and generate actionable insights on skill alignment and gaps.

---

## 🌟 Key Capabilities

### 🧠 Semantic Resume Understanding
- Utilizes transformer-based embeddings to interpret meaning, not just keywords  
- Captures contextual similarity between resume content and job requirements  

### 📊 Intelligent Match Scoring
- Computes an overall match score based on semantic similarity  
- Provides a realistic estimate of candidate-job alignment  

### 🎯 Skill Gap Analysis
- Identifies missing and matched skills  
- Highlights critical areas for improvement  

### ⚡ Multi-Format Resume Processing
- Supports PDF, DOCX, and TXT files  
- Extracts and processes raw text efficiently  

### 🔍 Hybrid Matching Engine
- Combines rule-based skill extraction with AI-driven semantic matching  
- Ensures both precision and contextual understanding  

### 📈 Interactive Visual Feedback
- Displays match score using progress indicators  
- Categorizes results into matched and missing skills  
- Provides intuitive, recruiter-style insights  

---

## 🧠 System Architecture

Resume → Parsing → Text Preprocessing → Skill Extraction  
       → Semantic Embeddings → Similarity Analysis → Insights  

---

## ⚙️ Tech Stack

- Python  
- Streamlit (Interactive Web UI)  
- Natural Language Processing (NLP)  
- Sentence Transformers (Pre-trained Embedding Models)  
- Scikit-learn (Cosine Similarity)  
- PDFPlumber / python-docx (Resume Parsing)  

---

## 🔬 How It Works

1. Extracts raw text from uploaded resume  
2. Cleans and normalizes textual data  
3. Identifies relevant technical and soft skills  
4. Converts text into vector embeddings using transformer models  
5. Compares resume and job description semantically  
6. Generates:
   - Match Score  
   - Matched Skills  
   - Missing Skills  
   - Overall Fit Analysis  

---

## 💡 Why This Project Stands Out

- Goes beyond traditional keyword-based resume screening  
- Incorporates semantic understanding using AI models  
- Provides actionable career insights, not just outputs  
- Designed as a user-facing product, not just a backend script  

---

## 🚀 Run Locally

pip install -r requirements.txt  
streamlit run app_streamlit.py  

---

## 📸 Demo

Add screenshots of your Streamlit app here (UI + results)

---

## 🔮 Future Enhancements

- Personalized skill improvement recommendations  
- Industry-specific role optimization  
- Resume rewriting suggestions using AI  
- Public deployment with shareable link  

---

## 👨‍💻 Author

Built with a focus on bridging the gap between resumes and real-world job expectations using AI.