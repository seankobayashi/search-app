import streamlit as st
import urllib.parse

st.set_page_config(page_title="営業検索ツール", layout="centered")
st.title("🔍 営業用 検索ランチャー")

name = st.text_input("👤 名前（例：山田太郎）")
keyword = st.text_input("🔑 キーワード（例：不動産、代表取締役）")

if name:
    quoted = f'"{name}"'
    search_urls = {
        "Google": f"https://www.google.com/search?q={urllib.parse.quote(quoted)}",
        "Google + キーワード": f"https://www.google.com/search?q={urllib.parse.quote(quoted + ' ' + keyword)}",
        "J-GLOBAL": f"https://www.google.com/search?q=site:jglobal.jst.go.jp+{urllib.parse.quote(name)}",
        "Facebook": f"https://www.facebook.com/search/people/?q={urllib.parse.quote(name)}",
        "Eight": f"https://www.google.com/search?q=site:8card.net+{urllib.parse.quote(name)}"
    }

    st.markdown("## 🔗 検索リンク（クリックで開く）")
    for label, url in search_urls.items():
        st.markdown(f"- [{label}]({url})")
