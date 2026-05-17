
import os
import tempfile
import streamlit as st

from dotenv import load_dotenv

from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_mistralai import ChatMistralAI

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate

# =====================================================
# Page Configuration
# =====================================================

st.set_page_config(
    page_title="AI PDF Assistant",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# Custom CSS
# =====================================================



st.markdown("""
<style>

/* =====================================================
MAIN APP
===================================================== */

[data-testid="stAppViewContainer"]{
    background: linear-gradient(
        135deg,
        #0f172a 0%,
        #111827 50%,
        #1e293b 100%
    );

    color: white;
}

/* =====================================================
SIDEBAR
===================================================== */

[data-testid="stSidebar"]{
    background: linear-gradient(
        to bottom,
        #020617,
        #0f172a
    );

    border-right: 1px solid rgba(255,255,255,0.08);
}

/* Force sidebar text visibility */

section[data-testid="stSidebar"] *{
    color: white !important;
}

/* =====================================================
TYPOGRAPHY
===================================================== */

.hero-title{
    font-size: 4rem;
    font-weight: 800;
    text-align: center;

    margin-top: 20px;
    margin-bottom: 10px;

    color: white;

    line-height: 1.1;
}

.hero-subtitle{
    text-align: center;

    font-size: 1.2rem;

    color: #CBD5E1;

    margin-bottom: 40px;

    max-width: 900px;

    margin-left: auto;
    margin-right: auto;

    line-height: 1.7;
}

/* =====================================================
GLASS CARD
===================================================== */

.glass-card{
    background: rgba(255,255,255,0.05);

    border: 1px solid rgba(255,255,255,0.08);

    backdrop-filter: blur(12px);

    border-radius: 20px;

    padding: 25px;

    margin-bottom: 20px;
}

/* =====================================================
UPLOAD SECTION
===================================================== */

.upload-box{

    background: rgba(255,255,255,0.03);

    border: 1px solid rgba(255,255,255,0.08);

    border-radius: 20px;

    padding: 25px;

    backdrop-filter: blur(10px);
}

/* =====================================================
FILE UPLOADER CONTAINER
===================================================== */

[data-testid="stFileUploader"]{

    width: 100%;
}

/* =====================================================
UPLOAD DROPZONE
===================================================== */

[data-testid="stFileUploaderDropzone"]{

    background: rgba(255,255,255,0.04) !important;

    border: 2px dashed rgba(255,255,255,0.15) !important;

    border-radius: 18px !important;

    padding: 35px !important;

    transition: 0.3s ease !important;
}

/* Hover effect */

[data-testid="stFileUploaderDropzone"]:hover{

    border: 2px dashed #7c3aed !important;

    background: rgba(124,58,237,0.08) !important;
}

/* =====================================================
UPLOAD BUTTON
===================================================== */

[data-testid="stFileUploaderDropzone"] button{

    background: linear-gradient(
        to right,
        #2563eb,
        #7c3aed
    ) !important;

    color: white !important;

    border: none !important;

    border-radius: 12px !important;

    padding: 10px 22px !important;

    font-weight: 600 !important;

    font-size: 15px !important;

    transition: 0.3s ease !important;
}

/* Button hover */

[data-testid="stFileUploaderDropzone"] button:hover{

    transform: scale(1.03);

    background: linear-gradient(
        to right,
        #1d4ed8,
        #6d28d9
    ) !important;
}
/* =====================================================
TEXT INPUT FIX
===================================================== */

/* Target the wrapper element */
[data-testid="stTextInputRootElement"] {
    background-color: rgba(255, 255, 255, 0.06) !important;
    border: 1px solid rgba(255, 255, 255, 0.15) !important;
    border-radius: 14px !important;
    padding: 4px !important;
}

/* Target the input text, its active states, and nested wrappers */
[data-testid="stTextInputRootElement"] input,
[data-testid="stTextInputRootElement"] div,
[data-testid="stTextInputRootElement"] span {
    color: #FFFFFF !important;
    -webkit-text-fill-color: #FFFFFF !important;
    background: transparent !important;
}

/* Ensure placeholder is visible but distinct */
[data-testid="stTextInputRootElement"] input::placeholder {
    color: #94A3B8 !important; /* Lighter slate gray */
    opacity: 1 !important;
    -webkit-text-fill-color: #94A3B8 !important;
}

/* Highlighting the border when clicking into the input */
[data-testid="stTextInputRootElement"]:focus-within {
    border-color: #7c3aed !important;
    box-shadow: 0 0 0 1px #7c3aed !important;
}

/* =====================================================
BUTTONS
===================================================== */

.stButton > button{

    width: 100%;

    height: 3.2rem;

    border-radius: 14px;

    background: linear-gradient(
        to right,
        #2563eb,
        #7c3aed
    );

    color: white;

    border: none;

    font-weight: 700;

    font-size: 1rem;

    transition: 0.3s ease;
}

.stButton > button:hover{

    transform: scale(1.02);

    background: linear-gradient(
        to right,
        #1d4ed8,
        #6d28d9
    );
}

/* =====================================================
METRICS
===================================================== */

[data-testid="stMetricValue"]{
    color: white !important;

    font-size: 2rem !important;
}

[data-testid="stMetricLabel"]{
    color: #CBD5E1 !important;
}

/* =====================================================
ANSWER BOX
===================================================== */

.answer-box{

    background: linear-gradient(
        to right,
        rgba(37,99,235,0.15),
        rgba(124,58,237,0.15)
    );

    border: 1px solid rgba(255,255,255,0.08);

    padding: 25px;

    border-radius: 18px;

    font-size: 1.05rem;

    line-height: 1.9;

    color: white;
}

/* =====================================================
EXPANDER
===================================================== */

.streamlit-expanderHeader{
    color: white !important;
}

/* =====================================================
GENERAL TEXT FIXES
===================================================== */

p, label, span, div{
    color: white;
}

/* =====================================================
FOOTER
===================================================== */

.footer{

    text-align:center;

    color:#94a3b8;

    margin-top:50px;

    padding-bottom:20px;

    font-size: 0.95rem;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# Load Environment Variables
# =====================================================

load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHROMA_PATH = os.path.join(BASE_DIR, "chroma-db")

# =====================================================
# Embedding Model
# =====================================================

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# =====================================================
# LLM
# =====================================================

llm = ChatMistralAI(
    model="mistral-small-2506"
)

# =====================================================
# Prompt Template
# =====================================================

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
"""
You are an expert AI research assistant.

Answer the question in a detailed, well-structured, and educational manner using ONLY the provided context.

Explain concepts clearly with:
- definitions,
- working principles,
- advantages,
- limitations,
- examples when available.

If the answer is not present in the context, say:
'I could not find the answer in the uploaded document.'
"""
        ),
        (
            "human",
            """
Context:
{context}

Question:
{question}
            """
        )
    ]
)

# =====================================================
# Sidebar
# =====================================================

with st.sidebar:

    st.markdown("## ⚡ AI PDF Assistant")

    st.markdown(
        """
Upload a PDF document and ask intelligent questions using Retrieval-Augmented Generation (RAG).
        """
    )

    st.divider()

    st.markdown("### 🛠 Tech Stack")

    st.markdown(
        """
- LangChain
- ChromaDB
- HuggingFace Embeddings
- Mistral AI
- Streamlit
        """
    )

    st.divider()

    st.markdown("### 🚀 Features")

    st.markdown(
        """
✅ PDF Upload

✅ Semantic Search

✅ AI-Powered Answers

✅ Vector Database

✅ RAG Pipeline
        """
    )

# =====================================================
# Hero Section
# =====================================================

st.markdown("""
<div class='hero-title'>
📚 AI PDF Research Assistant
</div>

<div class='hero-subtitle'>
Upload research papers, books, notes, and interact with them using Retrieval-Augmented Generation (RAG).
</div>
""", unsafe_allow_html=True)

# =====================================================
# Upload Section
# =====================================================
st.markdown("<div class='glass-card upload-box'>", unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "Upload your PDF",
    type=["pdf"]
)

st.markdown("</div>", unsafe_allow_html=True)

# =====================================================
# Process PDF
# =====================================================

if uploaded_file:

    with st.spinner("Processing PDF and creating embeddings..."):

        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file.read())
            temp_pdf_path = tmp_file.name

        # Load PDF
        loader = PyPDFLoader(temp_pdf_path)
        docs = loader.load()

        # Split Documents
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )

        chunks = splitter.split_documents(docs)

        # Create Vector Store
        vectorstore = Chroma.from_documents(
            documents=chunks,
            embedding=embedding_model,
            persist_directory=CHROMA_PATH
        )

        # Retriever
        retriever = vectorstore.as_retriever(
            search_type="mmr",
            search_kwargs={
                "k": 4,
                "fetch_k": 10,
                "lambda_mult": 0.5
            }
        )

    st.success("✅ PDF processed successfully!")

    # =====================================================
    # Stats Section
    # =====================================================

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Pages Loaded", len(docs))

    with col2:
        st.metric("Chunks Created", len(chunks))

    with col3:
        st.metric("Embedding Model", "MiniLM")

    st.divider()

    # =====================================================
    # Query Section
    # =====================================================

    query = st.text_input(
        "Ask a question about the uploaded document"
    )

    ask_button = st.button("Generate Answer")

    # =====================================================
    # Generate Response
    # =====================================================

    if ask_button and query:

        with st.spinner("Generating AI response..."):

            docs = retriever.invoke(query)

            context = "\n\n".join(
                [doc.page_content for doc in docs]
            )

            final_prompt = prompt.invoke(
                {
                    "context": context,
                    "question": query
                }
            )

            response = llm.invoke(final_prompt)

            # =============================================
            # Answer Box
            # =============================================

            st.markdown("## 🤖 AI Answer")

            st.markdown(
            f"""
           <div class='answer-box'>
           {response.content}
           </div>
           """,
           unsafe_allow_html=True
           )

            # =============================================
            # Retrieved Chunks
            # =============================================

            with st.expander("📄 Retrieved Context"):

                for i, doc in enumerate(docs):
                    st.markdown(f"### Chunk {i+1}")
                    st.write(doc.page_content)
                    st.divider()

# =====================================================
# Footer
# =====================================================

st.divider()

st.markdown("""
<div class='footer'>
Built with LangChain • ChromaDB • HuggingFace • Mistral AI • Streamlit
</div>
""", unsafe_allow_html=True)
