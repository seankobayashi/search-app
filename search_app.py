import streamlit as st
import urllib.parse

st.set_page_config(page_title="簡易検索", layout="centered")
st.title("🔍 簡易検索")

name = st.text_input("👤 名前（例：山田太郎）")
keyword = st.text_input("📍 キーワード（例：住所、職種など）")

if name:
    quoted = f'"{name}"'
    search_urls = {
        "Google": f"https://www.google.com/search?q={urllib.parse.quote(quoted)}",
        "Google + キーワード": f"https://www.google.com/search?q={urllib.parse.quote(quoted + ' ' + keyword)}",
        "J-GLOBAL": f"https://www.google.com/search?q=site:jglobal.jst.go.jp+{urllib.parse.quote(name)}",
        "Facebook": f"https://www.facebook.com/search/people/?q={urllib.parse.quote(name)}",
        "Eight名刺": f"https://www.google.com/search?q=site:8card.net+{urllib.parse.quote(name)}"
    }

    st.markdown("## 🔗 検索リンク（クリックで開く）")

    for label, url in search_urls.items():
        st.markdown(f'<a href="{url}" target="_blank">{label}</a>', unsafe_allow_html=True)
