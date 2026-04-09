import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة والجماليات (ستايل 2026 الرسمي)
st.set_page_config(page_title="نظام القيادة الإدارية 2026", layout="wide")

# 2. حقن صورة الخلفية والجماليات (CSS)
# استخدمت الرابط المباشر للصورة التي أرسلتها مع إضافة طبقة شفافة
st.markdown(f"""
    <style>
    @import url('https://googleapis.com');
    
    .stApp {{
        background-image: linear-gradient(rgba(255, 255, 255, 0.85), rgba(255, 255, 255, 0.85)), 
        url("https://top4top.io");
        background-size: cover;
        background-attachment: fixed;
    }}

    * {{ font-family: 'Cairo', sans-serif; text-align: right; }}

    /* شريط الأخبار المتحرك الفاخر */
    .news-ticker {{
        background: #a7282e; color: white; padding: 12px;
        overflow: hidden; white-space: nowrap; border-radius: 8px;
        margin-bottom: 25px; font-weight: bold; font-size: 16px;
        box-shadow: 0 4px 15px rgba(167, 40, 46, 0.3);
    }}
    .news-ticker span {{
        display: inline-block; padding-left: 100%;
        animation: ticker 35s linear infinite;
    }}
    @keyframes ticker {{
        0% {{ transform: translate(0, 0); }}
        100% {{ transform: translate(100%, 0); }}
    }}
    
    .main-header {{
        background: linear-gradient(to left, #1e5631, #a7282e);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 30px; font-weight: bold; text-align: center;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- شريط الأخبار العاجلة ---
st.markdown("""
    <div class="news-ticker">
        <span>
            📢 وزارة التربية الوطنية: انطلاق التسجيلات الأولية للسنة الدراسية 2026/2027 عبر المنصة الرقمية ... 
            🔴 مديرية التربية لولاية الشلف: ندوة تربوية حول آليات التقييم المستمر للأساتذة يوم الثلاثاء ... 
            ✅ حصري: نظام القيادة الإدارية يطلق خاصية استخراج الشهادات المدرسية والبطاقات التعريفية بنظام الكودبار
        </span>
    </div>
    """, unsafe_allow_html=True)

# 3. نظام الحماية والذاكرة
if 'auth' not in st.session_state: st.session_state['auth'] = False
if 'school_name' not in st.session_state: st.session_state['school_name'] = "المؤسسة التعليمية"

if not st.session_state['auth']:
    st.markdown('<div style="text-align:center"><img src="https://githubusercontent.com" width="130"></div>', unsafe_allow_html=True)
    st.markdown("<div class='main-header'>نظام القيادة الإدارية المتكامل</div>", unsafe_allow_html=True)
    key = st.text_input("🔑 كود تفعيل النسخة المعتمدة:", type="password")
    if st.button("🚀 فتح النظام"):
        if key == "CHLEF-2026": st.session_state['auth'] = True; st.rerun()
        else: st.error("المفتاح غير صحيح")
else:
    # القائمة الجانبية
    with st.sidebar:
        st.image("https://githubusercontent.com", width=100)
        st.markdown("### 🛂 لوحة التحكم")
        choice = st.radio("اختر الفضاء:", ["🏠 الرئيسية", "👨‍🏫 فضاء الأساتذة", "📂 الأمانة العامة", "💰 المقتصد والمالية"])
        if st.button("🔴 تسجيل خروج"): st.session_state['auth'] = False; st.rerun()

    # محتوى الأقسام
    st.markdown(f"<div class='main-header'>{choice}</div>", unsafe_allow_html=True)
    
    if choice == "🏠 الرئيسية":
        st.write(f"🏫 **المؤسسة:** {st.session_state['school_name']}")
        st.session_state['school_name'] = st.text_input("تغيير اسم المؤسسة:", value=st.session_state['school_name'])
        st.info("مرحباً بك في لوحة تحكم عام 2026. الخلفية الرسمية مفعلة الآن.")

st.markdown("---")
st.markdown(f"<p style='text-align
