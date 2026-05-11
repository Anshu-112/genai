import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables
load_dotenv()

# Gemini Model
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

# Prompt Template
prompt = ChatPromptTemplate.from_messages([

("system", """

You are a professional Information Extraction Assistant.

Your task:
Extract useful structured information from the given paragraph
and present it in a clean, readable format.

Rules:
- Do NOT add explanations
- Do NOT add extra commentary
- Follow the exact format
- If information is missing -> write NULL
- Keep summary short (2-3 lines max)
- Do NOT guess unknown facts
- Extract only information clearly available in the text
- Keep the response concise but informative

Output Format:

Movie Title:
Category / Type:
Genre:
Release Year:
Director:
Writer:
Producer:
Main Cast:
Supporting Cast:
Main Characters:
Story / Plot:
Main Theme:
Ratings / Recognition:
Notable Features:

Short Summary:

"""),

("human", """

Analyze the following paragraph and extract the information.

{paragraph}

""")

])

# Streamlit UI
st.set_page_config(
    page_title="Information Extractor",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 Information Extraction Assistant")

paragraph = st.text_area(
    "Enter your paragraph",
    height=250,
    placeholder="Paste your paragraph here..."
)

if st.button("Extract Information"):

    if paragraph.strip() == "":
        st.warning("Please enter a paragraph.")
    
    else:
        with st.spinner("Extracting information..."):

            final_prompt = prompt.invoke({
                "paragraph": paragraph
            })

            response = model.invoke(final_prompt)

            st.subheader("Extracted Information")
            st.text(response.content)