import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode

st.set_page_config(page_title="Psychotherapy AI Demo")

st.title("精神療法 AI 記録支援（試作）")
st.write("② マイク使用許可の確認テスト")

st.info("下の Start を押すと、マイク使用許可が表示されます。")

webrtc_streamer(
    key="mic-test",
    mode=WebRtcMode.SENDONLY,
    media_stream_constraints={"audio": True, "video": False},
)
