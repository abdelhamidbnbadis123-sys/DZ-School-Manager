import streamlit as st

# 1. إعدادات الصفحة والجماليات
st.set_page_config(page_title="نظام القيادة الإدارية 2026", layout="wide")

# 2. تحسينات الواجهة (CSS) لتصحيح الألوان وإضافة الفخامة
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    * { font-family: 'Cairo', sans-serif; text-align: right; }
    
    .main-title {
        background: linear-gradient(to left, #1e5631, #a7282e);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 45px; font-weight: bold; text-align: center;
        margin-bottom: 20px;
    }
    
    .stButton>button {
        background: linear-gradient(45deg, #1e5631, #a7282e) !important;
        color: white !important;
        border-radius: 30px !important;
        font-weight: bold !important;
        border: none !important;
        padding: 15px 40px !important;
        width: 100%;
        transition: 0.3s;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. نظام الحماية
if 'auth' not in st.session_state:
    st.session_state['auth'] = False

if not st.session_state['auth']:
    # --- تصحيح العلم الجزائري (رابط جديد ومباشر) ---
    st.markdown(
        """
        <div style="text-align:center;">
            <img src="https://giphy.com" width="160">
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    st.markdown("<div class='main-title'>نظام القيادة الإدارية المتكامل</div>", unsafe_allow_html=True)
    st.write("---")
    
    st.subheader("🔑 تفعيل النسخة المعتمدة")
    key = st.text_input("أدخل مفتاح الترخيص الخاص بالمؤسسة:", type="password", placeholder="اكتب الكود هنا...")
    
    if st.button("🚀 فتح النظام "):
        if key == "CHLEF-2026":
            st.session_state['auth'] = True
            st.balloons()
            st.rerun()
        else:
            st.error("❌ المفتاح غير صحيح! يرجى التواصل مع الإدارة التقنية.")
else:
    # القائمة الجانبية بعد الدخول
    st.sidebar.markdown("### 🛂 لوحة التحكم")
    choice = st.sidebar.radio("القائمة:", ["💰 المقتصد والمالية", "👨‍🏫 فضاء الأستاذ", "📋 الكودبار والتلاميذ"])
    
    st.markdown(f"<div class='main-title'>{choice}</div>", unsafe_allow_html=True)
    
    if st.sidebar.button("🔴 خروج"):
        st.session_state['auth'] = False
        st.rerun()

st.markdown("---")
st.markdown("<p style='text-align:center; color:grey;'>نظام القيادة الإدارية الذكي v5.2 | جميع الحقوق محفوظة © 2026</p>", unsafe_allow_html=True)
