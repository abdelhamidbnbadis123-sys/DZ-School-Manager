import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="نظام القيادة الإدارية 2026", layout="wide")

# 2. الخلفية والجماليات (الخلفية التي أرسلتها)
st.markdown("""
    <style>
    .stApp {
        background-image: linear-gradient(rgba(255,255,255,0.85), rgba(255,255,255,0.85)), 
        url("https://top4top.io");
        background-size: cover;
    }
    * { text-align: right; font-family: 'Cairo', sans-serif; }
    .ticker { background: #a7282e; color: white; padding: 10px; border-radius: 5px; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# 3. شريط الأخبار العاجلة
st.markdown('<div class="ticker">📢 عاجل: انطلاق التسجيلات المدرسية 2026/2027 ... مديرية التربية لولاية الشلف ترحب بكم</div>', unsafe_allow_html=True)

# 4. نظام الحماية
if 'auth' not in st.session_state: st.session_state['auth'] = False

if not st.session_state['auth']:
    st.image("https://githubusercontent.com", width=120)
    st.title("🔐 نظام القيادة الإدارية")
    key = st.text_input("كود التفعيل:", type="password")
    if st.button("دخول"):
        if key == "CHLEF-2026":
            st.session_state['auth'] = True
            st.rerun()
else:
    st.sidebar.title("🛂 القائمة")
    choice = st.sidebar.radio("اختر القسم:", ["🏠 الرئيسية", "👨‍🏫 الأستاذ", "💰 المقتصد", "📂 الأمانة"])
    st.header(f"✨ قسم {choice}")
    st.info("مرحباً بك في النسخة الاحترافية بالخلفية الرسمية.")

st.write("---")
st.caption("جميع الحقوق محفوظة © 2026")
