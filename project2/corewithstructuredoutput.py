from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser
import streamlit as st

# Load environment variables
load_dotenv()

# Streamlit Page Config
st.set_page_config(
    page_title="Movie Information Extractor",
    page_icon="🎬",
    layout="centered"
)

# Title
st.title("🎬 Movie Information Extractor")
st.write("Enter a movie paragraph and extract structured information using Gemini + LangChain")

# Initialize model
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

# Pydantic Schema
class Movie(BaseModel):
    title: str
    release_year: Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str

# Output parser
parser = PydanticOutputParser(pydantic_object=Movie)

# Prompt Template
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
Extract movie information from the paragraph.

{format_instructions}
"""
    ),
    (
        "human",
        """
{paragraph}
"""
    )
])

# User Input
para = st.text_area(
    "Enter Movie Paragraph",
    height=200,
    placeholder="Example: Interstellar is a 2014 science fiction movie directed by Christopher Nolan..."
)

# Button
if st.button("Extract Information"):

    if para.strip() == "":
        st.warning("Please enter a paragraph.")
    else:

        with st.spinner("Extracting information..."):

            # Final Prompt
            final_prompt = prompt.invoke({
                "paragraph": para,
                "format_instructions": parser.get_format_instructions()
            })

            # Model Response
            response = model.invoke(final_prompt)

            # Parse Output
            try:
                parsed_output = parser.parse(response.content)

                st.success("Information Extracted Successfully!")

                # Display Results
                st.subheader("🎥 Extracted Information")

                st.write(f"**Title:** {parsed_output.title}")
                st.write(f"**Release Year:** {parsed_output.release_year}")
                st.write(f"**Genre:** {', '.join(parsed_output.genre)}")
                st.write(f"**Director:** {parsed_output.director}")
                st.write(f"**Cast:** {', '.join(parsed_output.cast)}")
                st.write(f"**Rating:** {parsed_output.rating}")
                st.write(f"**Summary:** {parsed_output.summary}")

                # JSON View
                st.subheader("📦 JSON Output")
                st.json(parsed_output.model_dump())

            except Exception as e:
                st.error("Failed to parse the response.")
                st.code(response.content)
                st.exception(e)