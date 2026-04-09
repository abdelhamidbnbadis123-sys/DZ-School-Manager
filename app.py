import streamlit as st
import pandas as pd
import datetime

# --- 1. الإعدادات الأساسية والمعاملات الرسمية ---
st.set_page_config(page_title="نظام القيادة الإدارية 2026", layout="wide")

COEFFICIENTS = {
    "الرياضيات": 5, "اللغة العربية": 5, "الفيزياء": 2, "العلوم الطبيعية": 2,
    "التاريخ": 2, "الجغرافيا": 2, "التربية الاسلامية": 2, "التربية المدنية": 2,
    "التربية التشكيلية": 1, "الرسم": 1, "الموسيقى": 1, "الامازيغية": 2
}

# تهيئة مخزن البيانات (Session State)
if 'auth' not in st.session_state: st.session_state['auth'] = False
if 'school_name' not in st.session_state: st.session_state['school_name'] = "المؤسسة التعليمية"
if 'teachers' not in st.session_state: st.session_state['teachers'] = []
if 'grades' not in st.session_state: st.session_state['grades'] = {}

# --- 2. واجهة 2026 (CSS) ---
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    * { font-family: 'Cairo', sans-serif; text-align: right; }
    .main-header { background: linear-gradient(to left, #1e5631, #a7282e); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 32px; font-weight: bold; text-align: center; }
    .doc-box { border: 2px solid #000; padding: 30px; background: white; color: black; }
    .sms-box { background: #fff5f5; border: 1px solid #a7282e; padding: 10px; border-radius: 10px; color: #a7282e; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. بوابة الحماية ---
if not st.session_state['auth']:
    st.markdown('<div style="text-align:center"><img src="https://githubusercontent.com" width="150"></div>', unsafe_allow_html=True)
    st.markdown("<h1 class='main-header'>نظام القيادة الإدارية المتكامل</h1>", unsafe_allow_html=True)
    key = st.text_input("🔑 كود تفعيل النسخة (2026/2027):", type="password")
    if st.button("🚀 فتح النظام"):
        if key == "CHLEF-2026":
            st.session_state['auth'] = True
            st.rerun()
        else: st.error("المفتاح غير صحيح")
else:
    # --- 4. لوحة التحكم الجانبية ---
    with st.sidebar:
        st.image("https://githubusercontent.com", width=100)
        st.write(f"🏫 {st.session_state['school_name']}")
        choice = st.radio("🛂 الأقسام:", ["🏠 الرئيسية", "📂 الأمانة (الشهادات)", "👨‍🏫 فضاء الأساتذة والنقاط", "📊 كشوف التلاميذ", "💰 المقتصد والمالية", "📦 المخزن والأرشيف"])
        if st.button("🔴 خروج"):
            st.session_state['auth'] = False
            st.rerun()

    st.markdown(f"<div class='main-header'>{choice}</div>", unsafe_allow_html=True)

    # --- القسم 1: الرئيسية ---
    if choice == "🏠 الرئيسية":
        st.subheader("⚙️ إعدادات الموسم الدراسي 2026/2027")
        st.session_state['school_name'] = st.text_input("اسم المؤسسة الحالي:", value=st.session_state['school_name'])
        col1, col2 = st.columns(2)
        col1.metric("الأساتذة المسجلون", len(st.session_state['teachers']))
        col2.metric("التلاميذ المسجلون", len(st.session_state['grades']))

    # --- القسم 2: الأمانة (الشهادات و SMS) ---
    elif choice == "📂 الأمانة (الشهادات)":
        t1, t2 = st.tabs(["📄 الشهادة المدرسية", "📩 استدعاء SMS"])
        with t1:
            st.subheader("توليد شهادة مدرسية رسمية")
            c_name = st.text_input("اسم التلميذ:")
            c_birth = st.text_input("تاريخ ومكان الازدياد:")
            c_lvl = st.text_input("القسم:")
            if st.button("🖨️ عرض الشهادة"):
                st.markdown(f"""<div class="doc-box"><p style="text-align:center;"><b>الجمهورية الجزائرية الديمقراطية الشعبية</b><br>المؤسسة: {st.session_state['school_name']}</p><h2 style="text-align:center;">شهادة مدرسية</h2><p>يشهد مدير المؤسسة أن التلميذ(ة): <b>{c_name}</b> المولود في: {c_birth} يتابع دراسته بانتظام في قسم: {c_lvl}.</p></div>""", unsafe_allow_html=True)
        with t2:
            st.subheader("إرسال استدعاء رسمي للولي")
            p_phone = st.text_input("رقم هاتف الولي:")
            if st.button("📤 إرسال SMS"): st.success("تم إرسال الاستدعاء بنجاح.")

    # --- القسم 3: فضاء الأساتذة ---
    elif choice == "👨‍🏫 فضاء الأساتذة والنقاط":
        st.subheader("تسجيل الأستاذ وإدخال العلامات")
        with st.expander("➕ تسجيل أستاذ جديد"):
            t_name = st.text_input("اسم الأستاذ:")
            t_sub = st.selectbox("المادة:", list(COEFFICIENTS.keys()))
            if st.button("حفظ الأستاذ"):
                st.session_state['teachers'].append({"الاسم": t_name, "المادة": t_sub})
                st.success(f"تم تسجيل {t_name}")
        
        st.write("---")
        if st.session_state['teachers']:
            active_t = st.selectbox("الأستاذ الحالي:", [t['الاسم'] for t in st.session_state['teachers']])
            active_sub = next(t['المادة'] for t in st.session_state['teachers'] if t['الاسم'] == active_t)
            st.warning(f"مادة: {active_sub} | المعامل: {COEFFICIENTS[active_sub]}")
            
            st_name = st.text_input("اسم التلميذ للنقطة:")
            grade = st.number_input("النقطة / 20:", 0.0, 20.0, 10.0)
            if st.button("💾 حفظ النقطة"):
                if st_name not in st.session_state['grades']: st.session_state['grades'][st_name] = {}
                st.session_state['grades'][st_name][active_sub] = grade
                st.success("تم الحفظ.")

    # --- القسم 4: كشوف التلاميذ ---
    elif choice == "📊 كشوف التلاميذ":
        st.subheader("كشف النقاط والمعدل الآلي")
        target_st = st.selectbox("اختر التلميذ:", list(st.session_state['grades'].keys()))
        if target_st:
            marks = st.session_state['grades'][target_st]
            points, coeffs = 0, 0
            for m, g in marks.items():
                points += g * COEFFICIENTS[m]
                coeffs += COEFFICIENTS[m]
            st.table(pd.DataFrame([{"المادة": m, "النقطة": g, "المعامل": COEFFICIENTS[m]} for m, g in marks.items()]))
            if coeffs > 0: st.metric("المعدل العام", f"{points/coeffs:.2f} / 20")

    # --- القسم 5: المقتصد ---
    elif choice == "💰 المقتصد والمالية":
        st.subheader("تسيير الميزانية والجرد")
        miz = st.number_input("الميزانية (دج):", value=1000000)
        st.info(f"الإطعام (50%): {miz*0.5:,} دج")
        st.camera_input("📸 تصوير فاتورة للجرد")

st.markdown("---")
st.markdown(f"<p style='text-align:center; color:grey;'>نظام القيادة الإدارية الذكي v12.0 | {st.session_state['school_name']} | 2026/2027</p>", unsafe_allow_html=True)
    
