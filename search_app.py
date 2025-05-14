import streamlit as st
import urllib.parse
import re

st.set_page_config(page_title="簡易検索", layout="centered")
st.title("🔍 簡易検索")

# 入力フォーム
name = st.text_input("👤 名前")
address = st.text_input("🏠 住所")
keyword = st.text_input("📝 その他補足")

if name:
    quoted = f'"{name}"'

    prefecture = ""
    city = ""
    base_address = ""
    address_for_shataku = ""

    if address:
        # 都道府県抽出
        match_pref = re.search(r'(.*?[都道府県])', address)
        if match_pref:
            prefecture = match_pref.group(1)
            rest = address[len(prefecture):].strip()

            # 市区町村抽出（市・区・町・村）
            match_city = re.search(r'(.*?[市区町村])', rest)
            if match_city:
                city = match_city.group(1)
                after_city = rest[len(city):].strip()

                # 社宅確認用の住所（番地まで含めて、部屋番号を除去）
                match_address = re.search(r'([^\s\d]*\d{1,3}[-－]\d{1,3}(?:[-－]\d{1,3})?)', after_city)
                if match_address:
                    address_core = match_address.group(1)
                    address_for_shataku = f"{prefecture}{city}{address_core}"

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

    if address_for_shataku:
        search_urls["🏠 社宅確認"] = f"https://www.google.com/search?q={urllib.parse.quote(address_for_shataku + ' 社宅')}"

    # 外部サイト
    search_urls.update({
        "J-GLOBAL（Google経由）": f"https://www.google.com/search?q=site:jglobal.jst.go.jp+{urllib.parse.quote(quoted)}",
        "Facebook": f"https://www.facebook.com/search/people/?q={urllib.parse.quote(quoted)}",
        "Eight名刺（Google経由）": f"https://www.google.com/search?q=site:8card.net+{urllib.parse.quote(quoted)}"
    })

    # 表示
    st.markdown("## 🔗 検索リンク（クリックで開く）")
    for label, url in search_urls.items():
        st.markdown(f'<a href="{url}" target="_blank">{label}</a>', unsafe_allow_html=True)
