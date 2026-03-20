📌 Project Title: PolicyNav – Q&A Multi-Language Engine, Summarization, Knowledge Graph & Full Integration (Milestone 3)

📖 Description

In Milestone 3, PolicyNav was transformed into an AI-powered intelligent policy assistant by integrating a Q&A engine, multilingual summarization, and an interactive knowledge graph.

This milestone builds on the secure authentication, admin controls, and readability analytics from Milestone 2, adding a powerful NLP pipeline for deeper document understanding.

The system uses Qwen 2.5-1.5B-Instruct (4-bit quantized) for text generation and NLLB-200 for translation across multiple languages. Policy retrieval is handled using FAISS with multilingual embeddings, enabling accurate and fast responses.

The entire application runs on Google Colab with Google Drive persistence, making it scalable and easy to deploy.

The platform is now AI-driven, multilingual, interactive, and highly scalable.

✅ Features Implemented

🤖 Q&A Multi-Language Engine

Retrieval-Augmented Generation (RAG) using FAISS + Qwen model

Supports questions in 8 languages with auto-translation

Answer translation back to user’s language

Simplified answer mode for easy understanding

Source attribution (document names + response time)

Chat history with styled UI (user/bot bubbles)

Clear chat functionality


🌐 Multi-Language Summarization

Supports PDF, TXT, DOCX, and text input

Adjustable summary lengths: Short / Medium / Long

Two-stage pipeline:

English summary generation

Translation to target language

Side-by-side display (English + translated summary)

Word count comparison

Supports: English, Hindi, Tamil, Kannada, Telugu, Marathi, Bengali, Malayalam


🧩 Knowledge Graph

Extracts entities using spaCy (ORG, PERSON, LAW, GPE)

Builds graph using NetworkX

Interactive visualization using PyVis

Document-to-entity relationship mapping

Drag, zoom, and explore connections

Graphs saved to Google Drive

Reset and regenerate option


📦 Vector Store & Document Processing

Handles PDF, HTML, TXT ingestion

Chunking (1500 characters) for efficient retrieval

Multilingual embeddings using SentenceTransformers

FAISS indexing for fast semantic search

Incremental ingestion (avoids reprocessing)

De-duplication of document chunks

Automated PDF downloader for government policy docs


🔗 Full Integration with Milestone 2

All features protected via JWT authentication

Role-based UI (User / Admin)

OTP verification & password reset retained

Account locking & password history maintained

Readability Dashboard still accessible

Admin panel (manage users, unlock, promote, delete) fully functional



🎨 UI/UX Enhancements

Custom fonts: Syne + DM Sans

Full CSS theme system with variables

Gradient top bar and grid background

Enhanced login page with branding

Sidebar user badge display

Unified page header design

Styled inputs, tabs, charts, and panels

Chat animations and smooth transitions

Custom scrollbar and responsive layout


⚙️ Technologies Used

Python

Streamlit + streamlit-option-menu

Qwen 2.5 LLM (BitsAndBytes 4-bit)

NLLB-200 (Translation)

SentenceTransformers (Embeddings)

FAISS (Vector Search)

spaCy + NetworkX + PyVis (Knowledge Graph)

SQLite + JWT + bcrypt (Authentication)

PyPDF2, python-docx (Document Processing)

Plotly, Pandas (Analytics)

Google Drive (Storage)

Pyngrok (Deployment)

📁 Project Structure

PolicyNav/
├── app.py                  
├── nlp_engine.py           
├── vector_store.py         
├── knowledge_graph.py      
├── readability_utils.py    
├── db.py                   
├── documents/              
├── graphs/                 
├── faiss_index.bin         
└── faiss_meta.pkl          

▶️ How to Run the Application

Step 1: Install Dependencies

pip install streamlit pyngrok pyjwt watchdog bcrypt PyPDF2 streamlit-option-menu textstat plotly python-docx

pip install sentence-transformers faiss-cpu transformers accelerate bitsandbytes spacy networkx pyvis torch langdetect beautifulsoup4

python -m spacy download en_core_web_sm


Step 2: Setup Google Drive

Mount Google Drive in Colab

Create folders:

PolicyNav/

PolicyNav/documents/

PolicyNav/graphs/


Step 3: Upload / Download Policy Documents

Use PDF downloader OR manually upload files into documents/


Step 4: Ingest Documents into FAISS

Run ingestion pipeline

Documents are chunked, embedded, and indexed

Already processed files are skipped automatically


Step 5: Configure Secrets

Add the following in Colab Secrets:

JWT_SECRET_KEY

EMAIL_ID

EMAIL_APP_PASSWORD

ADMIN_EMAIL_ID

ADMIN_PASSWORD

NGROK_AUTHTOKEN


Step 6: Launch Application

Run Streamlit app

Expose via ngrok public URL

📸 Screenshots

Home Page
<img width="1105" height="810" alt="Screenshot 2026-03-09 211939" src="https://github.com/user-attachments/assets/fe65d2e5-fa12-412c-9904-2cefdd684a92" />

User Dashboard
<img width="1919" height="868" alt="Screenshot 2026-03-09 212123" src="https://github.com/user-attachments/assets/df4efbcf-cbf5-4180-9cd0-651fdf941139" />

Q & A Chatbot
<img width="1918" height="629" alt="sum" src="https://github.com/user-attachments/assets/70ebe3c8-b110-4584-9e6e-e94a56367c05" />

Summarization
<img width="1899" height="847" alt="Screenshot 2026-03-09 212548" src="https://github.com/user-attachments/assets/99f98ba1-f60f-485d-84f1-2b353884f3e1" />

<img width="1538" height="868" alt="su" src="https://github.com/user-attachments/assets/5fb63883-80c4-4e84-930d-6c817a24ba4e" />

Knowledge Graph Visualization
<img width="1458" height="708" alt="Screenshot 2026-03-09 212843" src="https://github.com/user-attachments/assets/d246cdb6-abe6-4e22-a72b-6e7206c52e2f" />

<img width="1421" height="848" alt="Screenshot 2026-03-09 212923" src="https://github.com/user-attachments/assets/970cd6d1-914f-4aeb-b85d-0d9d874b94a6" />

<img width="1417" height="824" alt="Screenshot 2026-03-09 212957" src="https://github.com/user-attachments/assets/7a51e42c-0ad8-41e5-99e0-8e8f3fe16003" />

<img width="1357" height="846" alt="Screenshot 2026-03-09 213200" src="https://github.com/user-attachments/assets/f61c96fe-7a19-4049-8450-08a73e8f6f0e" />

Readability Analyzer

<img width="1478" height="768" alt="Screenshot 2026-03-09 213317" src="https://github.com/user-attachments/assets/9c0c6317-6128-4b79-9db3-6290bbc1ac84" />

<img width="1549" height="765" alt="Screenshot 2026-03-09 213345" src="https://github.com/user-attachments/assets/13fb36e9-862e-4e88-a788-d4104d11dbd5" />

<img width="1457" height="756" alt="Screenshot 2026-03-09 213412" src="https://github.com/user-attachments/assets/3074b9dd-936d-49bd-8272-af80ab7ced82" />













