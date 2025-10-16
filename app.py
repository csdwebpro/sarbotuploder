import streamlit as st
import requests
import os

# ========== CONFIG ==========
BOT_TOKEN = "8432820657:AAHJTUIjxEuDEb647sZq8oYVUS5sdl23zdE"
CHAT_ID = "1599595167"
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/"
DOWNLOAD_DIR = "downloads"
# ============================

os.makedirs(DOWNLOAD_DIR, exist_ok=True)

st.set_page_config(page_title="Telegram Uploader Bot", page_icon="📤", layout="centered")

st.title("📤 Telegram Uploader Bot (Advanced Mode)")
st.caption("Upload any file or video to send directly to Telegram via your bot.")

uploaded_file = st.file_uploader("Choose a file to upload", type=None)

if uploaded_file is not None:
    # Save locally
    local_path = os.path.join(DOWNLOAD_DIR, uploaded_file.name)
    with open(local_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f"✅ File saved locally: {local_path}")

    # Send to Telegram
    with open(local_path, "rb") as file_data:
        files = {"document": (uploaded_file.name, file_data)}
        payload = {"chat_id": CHAT_ID, "caption": f"📦 Uploaded via Streamlit Bot\nFile: {uploaded_file.name}"}
        response = requests.post(API_URL + "sendDocument", data=payload, files=files)

    if response.status_code == 200:
        st.success("📨 File sent to Telegram successfully!")
    else:
        st.error(f"❌ Failed to send file. Response: {response.text}")

st.markdown("---")
st.subheader("🔧 Bot Configuration")
st.write(f"**Bot Token:** `{BOT_TOKEN}`")
st.write(f"**Chat ID:** `{CHAT_ID}`")
st.write("Make sure your bot has permission to send messages to the chat or channel.")
