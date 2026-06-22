import streamlit as st
from chatbot import ask_ai
from url_chat import answer_from_url

# -----------------------------------
# PAGE CONFIG
# -----------------------------------
st.set_page_config(
    page_title=" AI ChatBot",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------------
# CUSTOM CSS
# -----------------------------------
st.markdown("""
<style>
/* Main background */
.stApp {
    background-color: #F7E7CE;
}

/* Top white header */
header {
    background-color: #CD7F32 !important;
}

/* Main toolbar */
[data-testid="stHeader"] {
    background-color: #343541 !important;
}

/* Chat input area */
[data-testid="stChatInput"] {
    background-color: #FFFFFF !important;
    border-radius: 15px;
}

/* Text input boxes */
.stTextInput input {
    background-color: #FBCEB1 !important;
    color: white !important;
    border: 1px solid #334155 !important;
}

/* Buttons */
.stButton button {
    background-color: #001F3F !important;
    color: white !important;
    border: 1px solid #334155 !important;
    border-radius: 10px !important;
}

/* Button hover */
.stButton button:hover {
    background-color:F28500 # !important;
}

/* Chat input text box */
textarea {
    background-color: #FFFFFF !important;
    color: white !important;
}

/* Remove light sections */
section[data-testid="stSidebar"] {
    background-color: #F28500 !important;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------------
# SESSION STATE
# -----------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------------
# SIDEBAR
# -----------------------------------
with st.sidebar:

    st.title("🤖 YOUR AI BUDDY")

    if st.button("➕ New Chat💬", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.divider()

    url = st.text_input(
        "🌐 Website URL",
        placeholder="https://example.com"
    )

    if url:
        st.success("Website Connected")
    else:
        st.info("AI Chat Mode")

    st.divider()

    st.markdown("### Features")
    st.markdown("""
    - AI Chat
    - Website Analysis
    - URL Question Answering
    """)

# -----------------------------------
# HEADER
# -----------------------------------
st.markdown("""
<div class="main-header">
    <h1> 💻 AI Assistant</h1>
    <p>Ask questions, analyze websites,
and get instant answers powered by AI.</p>
</div>
""", unsafe_allow_html=True)

# -----------------------------------
# WELCOME CARDS
# -----------------------------------
if len(st.session_state.messages) == 0:

    col1, col2 = st.columns(2)

    with col1:
        if st.button("📄 Summarize Website", use_container_width=True):

            if url:
                summary = answer_from_url(
                    url,
                    "Give a detailed summary of this website."
                )

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": summary
                    }
                )

                st.rerun()

    with col2:
        if st.button("🔍 Extract Key Points", use_container_width=True):

            if url:
                keypoints = answer_from_url(
                    url,
                    "List the most important points from this website."
                )

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": keypoints
                    }
                )

                st.rerun()
# -----------------------------------
# DISPLAY CHAT HISTORY
# -----------------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -----------------------------------
# CHAT INPUT
# -----------------------------------
prompt = st.chat_input("Type your message or queries...")

if prompt:

    # User Message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    try:

        with st.spinner("Thinking..."):

            if url.strip():
                answer = answer_from_url(url, prompt)
            else:
                answer = ask_ai(prompt)

    except Exception as e:
        answer = f"Error: {e}"

    with st.chat_message("assistant"):
        st.markdown(answer)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })