import streamlit as st
import urllib.parse

# アプリ設定
st.set_page_config(page_title="簡易検索", layout="centered")
st.title("🔍 簡易検索")

# 入力フォーム
name = st.text_input("👤 名前（例：山田太郎）")
keyword = st.text_input("📍 キーワード（例：住所、職種など）")
address = st.text_input("🏠 住所（例：東京都八王子市中町）")

if name:
    quoted = f'"{name}"'

    # 都道府県・市区町村の抽出（単純分割）
    address_parts = address.strip().split()
    prefecture = ""
    city = ""
    if address:
        # 住所文字列を都道府県＋市区町村に分ける（空白がない場合も対応）
        if "都" in address or "道" in address or "府" in address or "県" in address:
            for mark in ["都", "道", "府", "県"]:
                if mark in address:
                    index = address.index(mark)
                    prefecture = address[:index + 1]
                    city = address[index + 1:].strip().split()[0] if len(address[index + 1:].strip().split()) > 0 else ""
                    break

    # 検索URL作成
    search_urls = {
        "Google": f"https://www.google.com/search?q={urllib.parse.quote(quoted)}",
    }

    if prefecture:
        search_urls["Google + 住所①（都道府県）"] = f"https://www.google.com/search?q={urllib.parse.quote(quoted + ' ' + prefecture)}"
    if city:
        search_urls["Google + 住所②（市区町村）"] = f"https://www.google.com/search?q={urllib.parse.quote(quoted + ' ' + city)}"

    if keyword:
        search_urls["Google + キーワード"] = f"https://www.google.com/search?q={urllib.parse.quote(quoted + ' ' + keyword)}"

    # その他の検索リンク
    search_urls.update({
        "J-GLOBAL（Google経由）": f"https://www.google.com/search?q=site:jglobal.jst.go.jp+{urllib.parse.quote(quoted)}",
        "Facebook": f"https://www.facebook.com/search/people/?q={urllib.parse.quote(quoted)}",
        "Eight名刺（Google経由）": f"https://www.google.com/search?q=site:8card.net+{urllib.parse.quote(quoted)}"
    })

    # 表示
    st.markdown("## 🔗 検索リンク（クリックで開く）")
    for label, url in search_urls.items():
        st.markdown(f'<a href="{url}" target="_blank">{label}</a>', unsafe_allow_html=True)
