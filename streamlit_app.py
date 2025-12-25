import streamlit as st
import whisper
import tempfile
import os

st.set_page_config(page_title="精神療法 AI 記録支援（アップロード版）")
st.title("精神療法 AI 記録支援")

st.write("録音済み音声ファイルをアップロードしてください。")

uploaded_file = st.file_uploader(
    "音声ファイル（wav / mp3 / m4a）",
    type=["wav", "mp3", "m4a"]
)

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(uploaded_file.read())
        audio_path = tmp.name

    st.success("音声ファイルを受け取りました")

    st.info("文字起こし中…")
    model = whisper.load_model("tiny")
    result = model.transcribe(audio_path)
    transcript = result["text"]

    st.subheader("🗒 文字起こし")
    st.text_area("", transcript, height=200)

    st.subheader("📝 簡易要約")
    summary = " ".join(transcript.split("。")[:3])
    st.text_area("", summary, height=150)