import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# Load environment variables
load_dotenv()

# Page config
st.set_page_config(
    page_title="AI Personality Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Personality Chatbot")

# AI Modes
modes = {
    "Angry AI 😠": "You are an angry AI agent. Reply in an angry and rude tone.",
    
    "Sad AI 😢": "You are a sad AI agent. Reply emotionally and sadly.",
    
    "Funny AI 😂": "You are a funny AI agent. Reply with humor and jokes.",
    
    "Therapist AI 🧠": "You are a calm and supportive therapist AI agent."
}

# Sidebar
st.sidebar.title("Choose AI Mode")

selected_mode = st.sidebar.radio(
    "Select Personality",
    list(modes.keys())
)

# Initialize model
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

# Initialize chat history
if (
    "messages" not in st.session_state or
    st.session_state.get("current_mode") != selected_mode
):
    st.session_state.current_mode = selected_mode

    st.session_state.messages = [
        SystemMessage(content=modes[selected_mode])
    ]

# Display selected mode
st.markdown(f"### Current Mode: {selected_mode}")

# Show previous messages
for message in st.session_state.messages:

    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.markdown(message.content)

    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(message.content)

# Chat input
prompt = st.chat_input("Type your message...")

if prompt:

    # Store user message
    st.session_state.messages.append(
        HumanMessage(content=prompt)
    )

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI response
    response = model.invoke(
        st.session_state.messages
    )

    # Store AI response
    st.session_state.messages.append(
        AIMessage(content=response.content)
    )

    # Display AI response
    with st.chat_message("assistant"):
        st.markdown(response.content)