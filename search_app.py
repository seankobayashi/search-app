import streamlit as st
import urllib.parse

# アプリ設定
st.set_page_config(page_title="簡易検索", layout="centered")
st.title("🔍 簡易検索")

# 入力フォーム（順番：名前 → 住所 → キーワード）
name = st.text_input("👤 名前（例：山田太郎）")
address = st.text_input("🏠 住所（例：東京都八王子市中町）")
keyword = st.text_input("📝 その他補足（例：代表取締役、不動産など）")

if name:
    quoted = f'"{name}"'

    # 住所の都道府県と市区町村を抽出
    prefecture = ""
    city = ""
    if address:
        if "都" in address or "道" in address or "府" in address or "県" in address:
            for mark in ["都", "道", "府", "県"]:
                if mark in address:
                    index = address.index(mark)
                    prefecture = address[:index + 1]
                    rest = address[index + 1:].strip()
                    city = rest.split()[0] if rest else ""
                    break

    # 検索リンク生成
    search_urls = {
        "名前": f"https://www.google.com/search?q={urllib.parse.quote(quoted)}"
    }

    if keyword:
        search_urls["名前 + その他補足"] = f"https://www.google.com/search?q={urllib.parse.quote(quoted + ' ' + keyword)}"

    if prefecture:
        search_urls["名前 + 住所①（都道府県）"] = f"https://www.google.com/search?q={urllib.parse.quote(quoted + ' ' + prefecture)}"
    if city:
        search_urls["名前 + 住所②（市区町村）"] = f"https://www.google.com/search?q={urllib.parse.quote(quoted + ' ' + city)}"

    # その他検索サイト（固定）
    search_urls.update({
        "J-GLOBAL（Google経由）": f"https://www.google.com/search?q=site:jglobal.jst.go.jp+{urllib.parse.quote(quoted)}",
        "Facebook": f"https://www.facebook.com/search/people/?q={urllib.parse.quote(quoted)}",
        "Eight名刺（Google経由）": f"https://www.google.com/search?q=site:8card.net+{urllib.parse.quote(quoted)}"
    })

    # 検索リンク表示
    st.markdown("## 🔗 検索リンク（クリックで開く）")
    for label, url in search_urls.items():
        st.markdown(f'<a href="{url}" target="_blank">{label}</a>', unsafe_allow_html=True)
