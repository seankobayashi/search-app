import streamlit as st
import urllib.parse
import re

# アプリ設定
st.set_page_config(page_title="簡易検索", layout="centered")
st.title("🔍 簡易検索")

# 入力フォーム（順：名前 → 住所 → 補足）
name = st.text_input("👤 名前（例：山田太郎）")
address = st.text_input("🏠 住所（例：千葉県市川市御南行徳）")
keyword = st.text_input("📝 その他補足")

if name:
    quoted = f'"{name}"'

    # 住所の都道府県と市区町村の抽出（例：千葉県市川市）
    prefecture = ""
    city = ""

    if address:
        # 都道府県
        match_pref = re.search(r'(.*?[都道府県])', address)
        if match_pref:
            prefecture = match_pref.group(1)
            rest = address[len(prefecture):]

            # 市区町村（市だけを取る）
            match_city = re.search(r'(.*?[市区町村])', rest)
            if match_city:
                city = match_city.group(1)

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

    # 他の検索サービス
    search_urls.update({
        "J-GLOBAL（Google経由）": f"https://www.google.com/search?q=site:jglobal.jst.go.jp+{urllib.parse.quote(quoted)}",
        "Facebook": f"https://www.facebook.com/search/people/?q={urllib.parse.quote(quoted)}",
        "Eight名刺（Google経由）": f"https://www.google.com/search?q=site:8card.net+{urllib.parse.quote(quoted)}"
    })

    # リンク表示
    st.markdown("## 🔗 検索リンク（クリックで開く）")
    for label, url in search_urls.items():
        st.markdown(f'<a href="{url}" target="_blank">{label}</a>', unsafe_allow_html=True)
