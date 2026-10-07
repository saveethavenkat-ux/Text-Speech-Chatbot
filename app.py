
import streamlit as st

from chatbot import ChatBot
from text_analysis import analyze_text, most_common_words
from speech import listen_to_speech, speak_text


# ==================== PAGE CONFIG ====================

st.set_page_config(
    page_title="Nova AI | Text & Speech Analysis",
    page_icon="🤖",
    layout="wide"
)


# ==================== SESSION STATE ====================

if "bot" not in st.session_state:
    st.session_state.bot = ChatBot()

if "messages" not in st.session_state:
    st.session_state.messages = []

if "analysis_text" not in st.session_state:
    st.session_state.analysis_text = ""


# ==================== PROFESSIONAL LIGHT UI ====================

st.markdown("""
<style>

    /* =========================
       MAIN APPLICATION
       ========================= */

    .stApp {
        background-color: #F5F7FB;
        color: #1F2937;
    }

    .main .block-container {
        max-width: 1450px;
        padding: 2rem 2rem 3rem;
    }


    /* =========================
       SIDEBAR
       ========================= */

    section[data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
        border-right: 1px solid #E5E7EB;
    }

    section[data-testid="stSidebar"] * {
        color: #1F2937 !important;
    }

    section[data-testid="stSidebar"] p {
        color: #4B5563 !important;
    }

    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        color: #111827 !important;
    }

    section[data-testid="stSidebar"] .stCaption {
        color: #6B7280 !important;
    }


    /* Sidebar buttons */

    section[data-testid="stSidebar"] .stButton > button {
        background-color: #FFFFFF !important;
        color: #374151 !important;
        border: 1px solid #D1D5DB !important;
    }

    section[data-testid="stSidebar"] .stButton > button:hover {
        background-color: #EFF6FF !important;
        color: #2563EB !important;
        border-color: #93C5FD !important;
    }


    /* =========================
       HEADER
       ========================= */

    .brand {
        font-size: 27px;
        font-weight: 750;
        color: #2563EB !important;
        margin-bottom: 4px;
    }

    .muted {
        color: #6B7280 !important;
        font-size: 13px;
    }

    .page-title {
        font-size: 32px;
        font-weight: 750;
        color: #111827 !important;
        margin-bottom: 4px;
    }

    .page-subtitle {
        color: #6B7280 !important;
        font-size: 14px;
        margin-bottom: 25px;
    }


    /* =========================
       PANELS
       ========================= */

    .panel {
        background-color: #FFFFFF;
        border: 1px solid #E5E7EB;
        border-radius: 16px;
        padding: 22px;
        margin-bottom: 18px;
        box-shadow: 0 3px 12px rgba(15, 23, 42, 0.035);
    }

    .panel-title {
        font-size: 19px;
        font-weight: 700;
        color: #111827 !important;
    }

    .panel-subtitle {
        color: #6B7280 !important;
        font-size: 12px;
        margin-top: 4px;
        margin-bottom: 18px;
    }


    /* =========================
       CHAT
       ========================= */

    .chat-user {
        background: #EAF2FF;
        border: 1px solid #D5E4FF;
        color: #1E40AF !important;
        padding: 13px 16px;
        border-radius: 14px 14px 4px 14px;
        margin: 12px 0 12px 12%;
        overflow-wrap: anywhere;
    }

    .chat-bot {
        background: #FFFFFF;
        border: 1px solid #E5E7EB;
        color: #374151 !important;
        padding: 13px 16px;
        border-radius: 14px 14px 14px 4px;
        margin: 12px 12% 12px 0;
        overflow-wrap: anywhere;
    }

    .chat-label {
        font-size: 10px;
        font-weight: 700;
        color: #6B7280 !important;
        letter-spacing: 0.8px;
        margin-bottom: 5px;
    }


    /* =========================
       WELCOME
       ========================= */

    .welcome {
        text-align: center;
        padding: 65px 15px;
    }

    .welcome-icon {
        font-size: 43px;
    }

    .welcome-heading {
        color: #111827 !important;
        font-size: 21px;
        font-weight: 700;
        margin-top: 12px;
    }

    .welcome-text {
        color: #6B7280 !important;
        font-size: 13px;
        margin-top: 8px;
        line-height: 1.7;
    }


    /* =========================
       METRIC CARDS
       ========================= */

    .metric-card {
        background: #F8FAFC;
        border: 1px solid #E5E7EB;
        border-radius: 12px;
        padding: 17px 10px;
        text-align: center;
    }

    .metric-value {
        color: #2563EB !important;
        font-size: 27px;
        font-weight: 750;
    }

    .metric-label {
        color: #6B7280 !important;
        font-size: 12px;
        margin-top: 4px;
    }


    /* =========================
       RESULT CARDS
       ========================= */

    .result-card {
        background: #F8FAFC;
        border: 1px solid #E5E7EB;
        border-radius: 12px;
        padding: 15px;
        margin-top: 12px;
    }

    .result-label {
        font-size: 11px;
        color: #6B7280 !important;
        text-transform: uppercase;
        letter-spacing: 0.7px;
    }

    .result-value {
        font-size: 18px;
        font-weight: 700;
        color: #111827 !important;
        margin-top: 5px;
    }


    /* =========================
       STREAMLIT TEXT
       ========================= */

    .stMarkdown,
    .stMarkdown p,
    .stMarkdown span {
        color: #1F2937;
    }


    /* =========================
       INPUT BOX
       ========================= */

    .stTextArea textarea {
        background-color: #FFFFFF !important;
        color: #111827 !important;
        border: 1px solid #D1D5DB !important;
        border-radius: 10px !important;
    }

    .stTextArea textarea::placeholder {
        color: #9CA3AF !important;
    }

    .stChatInput textarea {
        background-color: #FFFFFF !important;
        color: #111827 !important;
    }

    .stChatInput textarea::placeholder {
        color: #9CA3AF !important;
    }


    /* =========================
       BUTTONS
       ========================= */

    .stButton > button {
        border-radius: 9px;
        font-weight: 600;
        min-height: 42px;
        background-color: #FFFFFF !important;
        color: #374151 !important;
        border: 1px solid #D1D5DB !important;
    }

    .stButton > button:hover {
        background-color: #EFF6FF !important;
        color: #2563EB !important;
        border-color: #93C5FD !important;
    }


    /* =========================
       HEADINGS
       ========================= */

    h1, h2, h3, h4, h5, h6 {
        color: #111827 !important;
    }


    /* =========================
       FOOTER
       ========================= */

    .footer {
        text-align: center;
        color: #9CA3AF !important;
        font-size: 12px;
        padding: 20px 0 0;
    }


    /* =========================
       HIDE STREAMLIT BRANDING
       ========================= */

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

</style>
""", unsafe_allow_html=True)


# ==================== SIDEBAR ====================

with st.sidebar:

    st.markdown(
        '<div class="brand">🤖 Nova AI</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="muted">Text & Speech Intelligence</div>',
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown("### Workspace")

    if st.button("＋ New Conversation", use_container_width=True):
        st.session_state.messages = []
        st.session_state.analysis_text = ""
        st.rerun()

    st.markdown("### Features")

    st.markdown("""
    💬 Text Chat

    🎤 Speech Recognition

    🔊 Text-to-Speech

    😊 Sentiment Analysis

    🧠 Emotion Detection

    📊 Text Statistics
    """)

    st.divider()

    st.markdown("### About")

    st.markdown(
        '<div class="muted">'
        'Nova AI is a Python-based, rule-driven chatbot '
        'for text and speech analysis.'
        '</div>',
        unsafe_allow_html=True
    )


# ==================== HEADER ====================

st.markdown(
    '<div class="page-title">Conversation Studio</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="page-subtitle">'
    'Chat with Nova, analyze text, and explore emotional patterns.'
    '</div>',
    unsafe_allow_html=True
)


# ==================== MAIN LAYOUT ====================

chat_col, analysis_col = st.columns(
    [1.45, 1],
    gap="large"
)


# ==================== CHAT PANEL ====================

with chat_col:

    st.markdown(
        '<div class="panel-title">💬 Chat with Nova</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="panel-subtitle">'
        'Your personal text and speech assistant'
        '</div>',
        unsafe_allow_html=True
    )

    if not st.session_state.messages:

        st.markdown("""
        <div class="panel">
            <div class="welcome">
                <div class="welcome-icon">🤖</div>
                <div class="welcome-heading">
                    Welcome to Nova AI
                </div>
                <div class="welcome-text">
                    Start a conversation below.<br>
                    Ask a question or share how you feel.
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    else:

        for message in st.session_state.messages:

            content = (
                str(message["content"])
                .replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
                .replace("\n", "<br>")
            )

            if message["role"] == "user":

                st.markdown(
                    f"""
                    <div class="chat-user">
                        <div class="chat-label">YOU</div>
                        {content}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            else:

                st.markdown(
                    f"""
                    <div class="chat-bot">
                        <div class="chat-label">NOVA AI</div>
                        {content}
                    </div>
                    """,
                    unsafe_allow_html=True
                )


    user_input = st.chat_input("Type your message...")


    if user_input:

        st.session_state.messages.append({
            "role": "user",
            "content": user_input
        })

        response = st.session_state.bot.get_response(
            user_input
        )

        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })

        st.session_state.analysis_text = user_input

        st.rerun()


    # Speech input

    st.markdown('<div class="panel">', unsafe_allow_html=True)

    st.markdown(
        '<div class="panel-title">🎙 Speech Input</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="panel-subtitle">'
        'Speak into your microphone to start a conversation.'
        '</div>',
        unsafe_allow_html=True
    )

    if st.button("🎙 Start Listening", use_container_width=True):

        with st.spinner("Listening..."):

            speech_text = listen_to_speech()

        if speech_text:

            if speech_text in [
                "No speech detected.",
                "Could not understand the speech."
            ] or speech_text.startswith(
                ("Microphone error:", "Speech recognition service")
            ):

                st.warning(speech_text)

            else:

                st.session_state.messages.append({
                    "role": "user",
                    "content": speech_text
                })

                response = st.session_state.bot.get_response(
                    speech_text
                )

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": response
                })

                st.session_state.analysis_text = speech_text

                speak_text(response)

                st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)


# ==================== TEXT ANALYSIS ====================

with analysis_col:

    st.markdown(
        '<div class="panel-title">📊 Text Analysis</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="panel-subtitle">'
        'Understand sentiment, emotion, and word patterns.'
        '</div>',
        unsafe_allow_html=True
    )

    text_to_analyze = st.text_area(
        "Enter text",
        value=st.session_state.analysis_text,
        height=150,
        placeholder="Type or paste text here...",
        label_visibility="collapsed"
    )

    if st.button("Analyze Text  →", use_container_width=True):

        if text_to_analyze.strip():

            result = analyze_text(text_to_analyze)

            st.markdown("### Overview")

            metric1, metric2 = st.columns(2)

            with metric1:

                st.markdown(
                    f"""
                    <div class="metric-card">
                        <div class="metric-value">
                            {result['word_count']}
                        </div>
                        <div class="metric-label">
                            Total Words
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with metric2:

                st.markdown(
                    f"""
                    <div class="metric-card">
                        <div class="metric-value">
                            {result['unique_words']}
                        </div>
                        <div class="metric-label">
                            Unique Words
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )


            st.markdown(
                f"""
                <div class="result-card">
                    <div class="result-label">Sentiment</div>
                    <div class="result-value">
                        {result['sentiment']}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown(
                f"""
                <div class="result-card">
                    <div class="result-label">Detected Emotion</div>
                    <div class="result-value">
                        {result['emotion']}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )


            st.markdown("### Sentiment Breakdown")

            positive = result["positive_words"]
            negative = result["negative_words"]

            st.write(f"Positive words: **{positive}**")
            st.progress(min(positive / 5, 1.0))

            st.write(f"Negative words: **{negative}**")
            st.progress(min(negative / 5, 1.0))


            st.markdown("### Emotion Profile")

            for emotion, score in result["emotion_scores"].items():

                st.write(f"**{emotion}** — {score}")

                st.progress(min(score / 5, 1.0))


            st.markdown("### Common Words")

            common_words = most_common_words(
                text_to_analyze
            )

            if common_words:

                for word, count in common_words:

                    st.write(f"• **{word}** — {count}")

            else:

                st.caption("No common words to display.")

        else:

            st.warning("Please enter some text to analyze.")


# ==================== FOOTER ====================

st.markdown(
    '<div class="footer">'
    'Nova AI · Text & Speech Analysis · Built with Python'
    '</div>',
    unsafe_allow_html=True
)
