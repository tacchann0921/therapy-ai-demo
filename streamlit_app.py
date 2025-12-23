import streamlit as st

st.set_page_config(page_title="Psychotherapy AI Demo")

st.title("精神療法 AI 記録支援（試作）")

st.write("Streamlit Cloud デプロイ確認用アプリです。")

if st.button("動作テスト"):
    st.success("Streamlit は正常に動作しています")
    
