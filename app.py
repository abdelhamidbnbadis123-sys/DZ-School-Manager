import streamlit as st
import pandas as pd

# --- 1. الإعدادات والمعاملات وروابط dzexams الذكية ---
st.set_page_config(page_title="نظام القيادة الإدارية 2026", layout="wide")

COEFFICIENTS = {
    "الرياضيات": 5, "اللغة العربية": 5, "الفيزياء": 2, "العلوم الطبيعية": 2,
    "التاريخ": 2, "الجغرافيا": 2, "التربية الاسلامية": 2, "التربية المدنية": 2,
    "الامازيغية": 2, "الانجليزية": 2, "الفرنسية": 2
}

# خريطة الروابط (Slugs) لموقع dzexams
DZ_EXAMS_MAP = {
    "الرياضيات": "math", "اللغة العربية": "arabe", "الفيزياء": "physique",
    "العلوم الطبيعية": "sciences-naturelles", "التاريخ": "histoire-geographie",
    "الجغرافيا": "histoire-geographie", "التربية الاسلامية": "islamique",
    "التربية المدنية": "civique", "الامازيغية": "tamazight",
    "الانجليزية": "anglais", "الفرنسية": "francais"
}

# تهيئة الذاكرة السحابية للتطبيق
if 'auth' not in st.session_state: st.session_state['auth'] = False
if 'school_name' not in st.session_state: st.session_state['school_name'] = "المؤسسة التعليمية"
if 'school_type' not in st.session_state: st.session_state['school_type'] = "moyen" # الافتراضي متوسط
if 'teachers' not in st.session_state: st.session_state['teachers'] = []
if 'grades' not in st.session_state: st.session_state['grades'] = {}

# --- 2. واجهة 2026 (CSS) ---
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    * { font-family: 'Cairo', sans-serif; text-align: right; }
    .main-header { background: linear-gradient(to left, #1e5631, #a7282e); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 32px; font-weight: bold; text-align: center; }
    .dz-card { background-color: #f8f9fa; border-radius: 15px; padding: 20px; border-right: 8px solid #1e5631; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

# --- 3. بوابة الحماية ---
if not st.session_state['auth']:
    st.markdown('<div style="text-align:center"><img src="https://githubusercontent.com" width="150"></div>', unsafe_allow_html=True)
    st.markdown("<h1 class='main-header'>نظام القيادة الإدارية المتكامل</h1>", unsafe_allow_html=True)
    key = st.text_input("🔑 كود تفعيل النسخة:", type="password")
    if st.button("🚀 فتح النظام"):
        if key == "CHLEF-2026": st.session_state['auth'] = True; st.rerun()
        else: st.error("المفتاح غير صحيح")
else:
    # --- 4. لوحة التحكم الجانبية ---
    with st.sidebar:
        st.image("https://githubusercontent.com", width=100)
        choice = st.radio("🛂 القائمة الرئيسية:", ["🏠 الإعدادات والصفحة الرئيسية", "👨‍🏫 فضاء الأساتذة والموارد", "📊 كشوف النقاط", "📂 الأمانة والشهادات"])
        if st.button("🔴 تسجيل الخروج"): st.session_state['auth'] = False; st.rerun()

    # --- القسم 1: الإعدادات (تحديد متوسط أو ثانوي) ---
    if choice == "🏠 الإعدادات والصفحة الرئيسية":
        st.markdown("<h1 class='main-header'>إعدادات المؤسسة التعليمية</h1>", unsafe_allow_html=True)
        st.session_state['school_name'] = st.text_input("اسم المؤسسة:", value=st.session_state['school_name'])
        
        # الميزة الجديدة: تحديد الطور التعليمي
        st.session_state['school_type'] = st.selectbox(
            "تحديد الطور التعليمي للمؤسسة:",
            options=["moyen", "secondaire"],
            format_func=lambda x: "متوسطة" if x == "moyen" else "ثانوية"
        )
        st.success(f"تم ضبط النظام ليعمل كـ: {'متوسطة' if st.session_state['school_type'] == 'moyen' else 'ثانوية'}")

    # --- القسم 2: فضاء الأساتذة مع التوجيه الذكي لموقع dzexams ---
    elif choice == "👨‍🏫 فضاء الأساتذة والموارد":
        st.markdown(f"<h1 class='main-header'>فضاء الأستاذ والبنك الرقمي</h1>", unsafe_allow_html=True)
        
        # إضافة أستاذ (إذا كان جديداً)
        with st.expander("➕ تسجيل أستاذ جديد في النظام"):
            t_name = st.text_input("الاسم واللقب:")
            t_sub = st.selectbox("المادة:", list(COEFFICIENTS.keys()))
            if st.button("حفظ الأستاذ"):
                st.session_state['teachers'].append({"الاسم": t_name, "المادة": t_sub})
                st.success("تم التسجيل بنجاح.")

        if st.session_state['teachers']:
            active_t = st.selectbox("أنت الأستاذ(ة):", [t['الاسم'] for t in st.session_state['teachers']])
            active_sub = next(t['المادة'] for t in st.session_state['teachers'] if t['Name'] == active_t) # تصحيح صغير هنا
            active_sub = [t['المادة'] for t in st.session_state['teachers'] if t['الاسم'] == active_t][0]
            
            tab1, tab2 = st.tabs(["📚 موارد dzexams الذكية", "📉 إدخال النقاط"])
            
            with tab1:
                st.subheader("🌐 البنك الوطني للفروض والاختبارات")
                st.markdown(f"""
                <div class='dz-card'>
                    مرحباً أستاذ مادة <b>{active_sub}</b>. <br>
                    تم ضبط مسار البحث تلقائياً ليتوافق مع طور مؤسستكم (<b>{'المتوسط' if st.session_state['school_type'] == 'moyen' else 'الثانوي'}</b>).
                </div>
                """, unsafe_allow_html=True)
                
                # بناء الرابط الذكي
                cycle = st.session_state['school_type']
                slug = DZ_EXAMS_MAP.get(active_sub, "")
                final_url = f"https://dzexams.com{cycle}/subjects/{slug}"
                
                st.link_button(f"🚀 فتح بنك اختبارات مادة {active_sub}", final_url)

            with tab2:
                st.subheader(f"تسجيل نقاط مادة {active_sub}")
                st_name = st.text_input("اسم التلميذ:")
                grade = st.number_input("العلامة / 20:", 0.0, 20.0, 10.0)
                if st.button("حفظ"):
                    if st_name not in st.session_state['grades']: st.session_state['grades'][st_name] = {}
                    st.session_state['grades'][st_name][active_sub] = grade
                    st.success("تم الحفظ.")

st.markdown("---")
st.markdown(f"<p style='text-align:center; color:grey;'>نظام القيادة الإدارية 2026 | مؤسسة: {st.session_state['school_name']}</p>", unsafe_allow_html=True)
