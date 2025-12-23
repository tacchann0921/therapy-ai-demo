import streamlit as st
import tempfile
import os
import datetime
import av
from streamlit_webrtc import webrtc_streamer, WebRtcMode

st.set_page_config(page_title="Psychotherapy AI Demo")

st.title("精神療法 AI 記録支援（試作）")
st.subheader("③ 録音 → 音声保存テスト")

audio_frames = []

class AudioProcessor:
    def recv(self, frame: av.AudioFrame):
        audio_frames.append(frame)
        return frame

ctx = webrtc_streamer(
    key="audio-save-test",
    mode=WebRtcMode.SENDONLY,
    audio_processor_factory=AudioProcessor,
    media_stream_constraints={"audio": True, "video": False},
)

if st.button("⏹ 録音終了・保存"):
    if not audio_frames:
        st.warning("まだ音声がありません")
    else:
        now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        with tempfile.NamedTemporaryFile(suffix=f"_{now}.wav", delete=False) as f:
            container = av.open(f.name, mode="w")
            stream = container.add_stream("pcm_s16le", rate=16000)

            for frame in audio_frames:
                for packet in stream.encode(frame):
                    container.mux(packet)

            container.close()

        st.success("音声を保存しました")
        st.write(f"保存先: {f.name}")