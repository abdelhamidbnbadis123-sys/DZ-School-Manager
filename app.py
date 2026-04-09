import streamlit as st
import pandas as pd

# --- 1. الإعدادات والمعاملات وروابط dzexams ---
st.set_page_config(page_title="نظام القيادة الإدارية 2026", layout="wide")

COEFFICIENTS = {
    "الرياضيات": 5, "اللغة العربية": 5, "الفيزياء": 2, "العلوم الطبيعية": 2,
    "التاريخ": 2, "الجغرافيا": 2, "التربية الاسلامية": 2, "التربية المدنية": 2,
    "الامازيغية": 2, "الانجليزية": 2, "الفرنسية": 2
}

DZ_EXAMS_MAP = {
    "الرياضيات": "math", "اللغة العربية": "arabe", "الفيزياء": "physique",
    "العلوم الطبيعية": "sciences-naturelles", "التاريخ": "histoire-geographie",
    "الجغرافيا": "histoire-geographie", "التربية الاسلامية": "islamique",
    "التربية المدنية": "civique", "الامازيغية": "tamazight",
    "الانجليزية": "anglais", "الفرنسية": "francais"
}

# تهيئة الذاكرة
if 'auth' not in st.session_state: st.session_state['auth'] = False
if 'school_name' not in st.session_state: st.session_state['school_name'] = "المؤسسة التعليمية"
if 'school_type' not in st.session_state: st.session_state['school_type'] = "moyen"
if 'teachers' not in st.session_state: st.session_state['teachers'] = []
if 'grades' not in st.session_state: st.session_state['grades'] = {}

# --- 2. واجهة 2026 مع شريط الأخبار (CSS) ---
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    * { font-family: 'Cairo', sans-serif; text-align: right; }
    
    /* ستايل شريط الأخبار المتحرك */
    .news-ticker {
        background: #a7282e; color: white; padding: 10px;
        overflow: hidden; white-space: nowrap; box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        border-radius: 5px; margin-bottom: 20px; font-weight: bold;
    }
    .news-ticker span {
        display: inline-block; padding-left: 100%;
        animation: ticker 25s linear infinite;
    }
    @keyframes ticker {
        0% { transform: translate(0, 0); }
        100% { transform: translate(100%, 0); }
    }
    .main-header { background: linear-gradient(to left, #1e5631, #a7282e); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 28px; font-weight: bold; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. شريط الأخبار في أعلى الصفحة ---
st.markdown("""
    <div class="news-ticker">
        <span>
            🔴 عاجل: وزارة التربية تعلن عن جدول العطل المدرسية لموسم 2026/2027 ... 
            📢 مديرية التربية لولاية الشلف: انطلاق عملية رقمنة الملفات الإدارية لجميع المؤسسات ... 
            ✅ تحديث: إضافة خاصية الجرد التلقائي بالفواتير في نظام القيادة الإدارية الذكي
        </span>
    </div>
    """, unsafe_allow_html=True)

# --- 4. بوابة الحماية ---
if not st.session_state['auth']:
    st.markdown('<div style="text-align:center"><img src="https://githubusercontent.com" width="130"></div>', unsafe_allow_html=True)
    key = st.text_input("🔑 كود تفعيل النسخة:", type="password")
    if st.button("🚀 فتح النظام"):
        if key == "CHLEF-2026": st.session_state['auth'] = True; st.rerun()
        else: st.error("المفتاح غير صحيح")
else:
    # القائمة الجانبية
    with st.sidebar:
        st.image("https://githubusercontent.com", width=100)
        choice = st.radio("🛂 القائمة:", ["🏠 الرئيسية", "👨‍🏫 فضاء الأساتذة", "📊 كشوف النقاط", "📂 الأمانة"])
        if st.button("🔴 خروج"): st.session_state['auth'] = False; st.rerun()

    # --- تصحيح الخطأ (الاسم بدلاً من Name) ---
    if choice == "👨‍🏫 فضاء الأساتذة":
        st.markdown("<h1 class='main-header'>فضاء الأستاذ والبنك الرقمي</h1>", unsafe_allow_html=True)
        
        with st.expander("➕ تسجيل أستاذ جديد"):
            t_name = st.text_input("الاسم واللقب:")
            t_sub = st.selectbox("المادة:", list(COEFFICIENTS.keys()))
            if st.button("حفظ"):
                st.session_state['teachers'].append({"الاسم": t_name, "المادة": t_sub})
                st.success("تم التسجيل.")

        if st.session_state['teachers']:
            active_t = st.selectbox("أنت الأستاذ(ة):", [t['الاسم'] for t in st.session_state['teachers']])
            # تصحيح الخطأ هنا (تم تغيير Name إلى الاسم)
            active_sub = next(t['المادة'] for t in st.session_state['teachers'] if t['الاسم'] == active_t)
            
            tab1, tab2 = st.tabs(["🌐 موارد dzexams", "📉 إدخال النقاط"])
            with tab1:
                cycle = st.session_state['school_type']
                slug = DZ_EXAMS_MAP.get(active_sub, "")
                st.link_button(f"🚀 فتح بنك اختبارات مادة {active_sub}", f"https://dzexams.com{cycle}/subjects/{slug}")
            with tab2:
                st_name = st.text_input("اسم التلميذ:")
                grade = st.number_input("العلامة:", 0.0, 20.0, 10.0)
                if st.button("حفظ العلامة"):
                    if st_name not in st.session_state['grades']: st.session_state['grades'][st_name] = {}
                    st.session_state['grades'][st_name][active_sub] = grade
                    st.success("تم الحفظ.")

    elif choice == "🏠 الرئيسية":
        st.markdown("<h1 class='main-header'>إعدادات المؤسسة التعليمية</h1>", unsafe_allow_html=True)
        st.session_state['school_name'] = st.text_input("اسم المؤسسة:", value=st.session_state['school_name'])
        st.session_state['school_type'] = st.selectbox("الطور:", options=["moyen", "secondaire"], format_func=lambda x: "متوسطة" if x == "moyen" else "ثانوية")

st.markdown("---")
st.markdown(f"<p style='text-align:center; color:grey;'>نظام القيادة الإدارية 2026 | {st.session_state['school_name']}</p>", unsafe_allow_html=True)
