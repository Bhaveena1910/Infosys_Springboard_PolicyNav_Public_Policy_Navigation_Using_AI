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
