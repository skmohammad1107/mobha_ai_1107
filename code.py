import os
import requests
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

# 1. Page Configuration (Must be the first Streamlit command)
st.set_page_config(
    page_title="AI Teacher Classroom",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# 2. Professional Custom Styling (Injecting CSS)
st.markdown(
    """
    <style>
    /* Main background and text colors */
    .stApp {
        background-color: #FAFAFA;
        color: #1E293B;
    }
    /* Main Header styling */
    .main-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1E3A8A; /* Professional Deep Blue */
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        font-size: 1.1rem;
        color: #64748B; /* Slate Grey */
        text-align: center;
        margin-bottom: 2rem;
    }
    /* Chat response box */
    .response-box {
        background-color: #FFFFFF;
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 5px solid #2563EB; /* Bright Blue Accent */
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        margin-top: 1.5rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 3. Initialize API Clients
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("🔑 GROQ_API_KEY not found. Please check your .env file.")
    st.stop()

client = Groq(api_key=api_key)


# 4. LLM Function
def ask_llm(prompt):
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are a helpful AI teacher."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.3,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error connecting to AI: {str(e)}"


# 5. Website UI Layout
st.markdown(
    "<h1 class='main-title'>🤖 AI Teacher Assistant</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p class='subtitle'>Ask any educational question and get clear, simple answers instantly.</p>",
    unsafe_allow_html=True,
)

# Search Bar Component
search_query = st.text_input(
    label="Search Bar",
    placeholder="Type your question here (e.g., 'Explain AI Agent in simple words')...",
    label_visibility="collapsed",  # Hides the default label for a cleaner look
)

# Trigger Action on Search
if search_query:
    with st.spinner("🧠 Thinking..."):
        answer = ask_llm(search_query)

    # Display Answer in a Styled Container
    st.markdown(
        f"""
        <div class="response-box">
            <h4 style="color: #2563EB; margin-top: 0;">👨‍🏫 Teacher's Answer:</h4>
            {answer}
        </div>
        """,
        unsafe_allow_html=True,
    )

# Footer
st.markdown(
    "<p style='text-align: center; color: #94A3B8; margin-top: 5rem; font-size: 0.8rem;'>Powered by Groq & Llama 3.1</p>",
    unsafe_allow_html=True,
)



