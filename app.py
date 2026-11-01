import streamlit as st

# 頁面基本設定
st.set_page_config(
    page_title="微光樹洞 Glimmer Treehole",
    page_icon="🌿",
    layout="wide"
)

# 莫蘭迪暗色調與玻璃擬態 CSS
st.markdown("""
<style>
    .stApp {
        background-color: #2b3336;
        color: #e0e6e8;
    }
    .sticky-note {
        background-color: #3d4a4d;
        border-left: 4px solid #8ba89c;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 12px;
    }
</style>
""", unsafe_allow_html=True)

# 頂部標題
st.title("🌿 微光樹洞 Glimmer Treehole")
st.caption("專屬於青少年與年輕人的情緒 sanctuary ‧ 在這裡放開所有負擔與不安。")

# 側邊欄導覽
st.sidebar.title("🧭 樹洞導覽")
choice = st.sidebar.radio(
    "選擇目的地：", 
    ["🌱 傾訴樹洞 (AI 夥伴)", "💌 暖心續航貼牆", "📊 今日情緒小測驗", "🧘 解壓小角", "🚨 緊急求助 SOS"]
)

# 1. 傾訴樹洞
if choice == "🌱 傾訴樹洞 (AI 夥伴)":
    st.subheader("🌱 傾訴樹洞")
    st.write("把煩惱或說不出口的心事留在這裡，樹洞會溫柔陪伴你。")
    user_input = st.text_area("寫下你現在的想法...", height=150, placeholder="今天過得好累，感覺沒人理解我...")
    
    if st.button("送信給樹洞 ✨"):
        if user_input.strip():
            st.success("樹洞收到你的心聲了。你不孤單，你已經做得很好。")
            st.info("💡 溫馨迴響：生活偶爾會有陰天，但微光一直在這裡陪伴你。記得給自己一個擁抱！")
        else:
            st.warning("請先寫點什麼再傳送給樹洞喔！")

# 2. 暖心續航貼牆
elif choice == "💌 暖心續航貼牆":
    st.subheader("💌 暖心續航貼牆")
    st.write("來自其他旅人的溫暖留言：")
    notes = [
        "「今天的你也辛苦了，記得好好呼吸。」",
        "「不完美也沒關係，你本身就很值得被愛。」",
        "「慢慢來，比較快。給自己一點時間。」",
        "「允許自己難過，也是一種勇敢。」"
    ]
    for note in notes:
        st.markdown(f'<div class="sticky-note">{note}</div>', unsafe_allow_html=True)

# 3. 今日情緒小測驗
elif choice == "📊 今日情緒小測驗":
    st.subheader("📊 今日情緒測驗")
    mood = st.select_slider("你今天的心情指數？", options=["🌧️ 沉重", "☁️ 陰天", "⛅ 微光", "☀️ 晴朗"])
    st.write(f"你今天選擇的心情狀態是：**{mood}**")
    if mood == "🌧️ 沉重":
        st.write("抱抱你，今天過得不容易吧？去『解壓小角』做個深呼吸吧。")
    elif mood == "☀️ 晴朗":
        st.write("太棒了！希望這份好心情能陪伴你一整天✨")

# 4. 解壓小角
elif choice == "🧘 解壓小角":
    st.subheader("🧘 4-7-8 呼吸放鬆法")
    st.write("吸氣 4 秒 ➔ 憋氣 7 秒 ➔ 吐氣 8 秒，重複幾次讓大腦放鬆。")
    if st.button("開始放鬆引導 🍃"):
        st.write("1. 慢慢吸氣... (1, 2, 3, 4)")
        st.write("2. 保持憋氣... (1, 2, 3, 4, 5, 6, 7)")
        st.write("3. 緩緩吐氣... (1, 2, 3, 4, 5, 6, 7, 8)")
        st.balloons()

# 5. SOS 資源
elif choice == "🚨 緊急求助 SOS":
    st.subheader("🚨 緊急求助資源")
    st.error("如果目前感受極度痛苦或有急迫危險，請立即聯繫以下專業求助管道：")
    st.write("• **衛福部安心專線**：1925 (依舊愛我)")
    st.write("• **生命線協談專線**：1995")
    st.write("• **張老師專線**：1980")