import streamlit as st
from groq import Groq

GROQ_API_KEY = "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"  # <-- Replace with your key for testing

# Initialize GROQ client
client = Groq(api_key=GROQ_API_KEY)

# Streamlit page config
st.set_page_config(page_title="Chat with James", page_icon="😎", layout="centered")
st.title("💬 Chat with James!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": (
            "You are James, a sarcastic, fun-loving AI. "
            "You make witty comebacks, tease playfully, "
            "and respond with humor and cheeky remarks."
        )}
    ]

# Function to send message to GROQ
def send_to_groq(user_message):
    try:
        st.session_state.messages.append({"role": "user", "content": user_message})
        response = client.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            messages=st.session_state.messages
        )
        bot_message = response.choices[0].message.content
        st.session_state.messages.append({"role": "bot", "content": bot_message})
        return bot_message
    except Exception as e:
        return f"Error: {e}"

# Chat input
user_input = st.text_input("Say something to James...")

if st.button("Send"):
    if user_input.strip():
        send_to_groq(user_input)
    else:
        st.warning("Type something first, don't be shy!")

# Display chat messages
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    elif msg["role"] == "bot":
        st.markdown(f"**James:** {msg['content']} 😏")
