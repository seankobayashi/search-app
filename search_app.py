import streamlit as st
import urllib.parse
import re

st.set_page_config(page_title="簡易検索", layout="centered")
st.title("🔍 簡易検索")

name = st.text_input("👤 名前")
address = st.text_input("🏠 住所")
keyword = st.text_input("📝 その他補足")

if name:
    quoted = f'"{name}"'

    prefecture = ""
    city = ""
    base_address = ""  # 社宅検索用に部屋番号除去した住所

    if address:
        # 都道府県抽出
        match_pref = re.search(r'(.*?[都道府県])', address)
        if match_pref:
            prefecture = match_pref.group(1)
            rest = address[len(prefecture):].strip()

            # 市区町村抽出（市・区まで）
            match_city = re.search(r'(.*?[市区町村])', rest)
            if match_city:
                city = match_city.group(1)
                rest = rest[len(city):].strip()

                # base_address = 都道府県 + 市区町村 まで（残り削除）
                base_address = prefecture + city

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

        # 社宅確認リンク（市区町村まで + 社宅）
        search_urls["🏠 社宅確認"] = f"https://www.google.com/search?q={urllib.parse.quote(quoted + ' ' + base_address + '
