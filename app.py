import streamlit as st
import pandas as pd
import datetime

# --- 1. إعدادات الواجهة والجماليات الفاخرة 2026 ---
st.set_page_config(page_title="نظام القيادة الإدارية 2026", layout="wide")

st.markdown("""
    <style>
    @import url('https://googleapis.com');
    .stApp {
        background-image: linear-gradient(rgba(255, 255, 255, 0.94), rgba(255, 255, 255, 0.94)), 
        url("https://top4top.io");
        background-size: cover; background-attachment: fixed;
    }
    * { font-family: 'Cairo', sans-serif; text-align: right; }
    
    /* تصميم الأزرار المركزية */
    .main-card {
        background: white; padding: 25px; border-radius: 20px;
        border-right: 8px solid #1e5631; box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        text-align: center; margin-bottom: 20px; transition: 0.3s;
    }
    .main-card:hover { transform: translateY(-5px); box-shadow: 0 15px 30px rgba(0,0,0,0.2); }
    .card-title { color: #1e5631; font-size: 20px; font-weight: bold; }
    
    /* شريط الأخبار المتحرك */
    .news-ticker {
        background: #a7282e; color: white; padding: 10px; border-radius: 8px;
        overflow: hidden; white-space: nowrap; font-weight: bold; margin-bottom: 20px;
    }
    .news-ticker span { display: inline-block; padding-left: 100%; animation: ticker 30s linear infinite; }
    @keyframes ticker { 0% { transform: translate(0, 0); } 100% { transform: translate(100%, 0); } }
    </style>
    """, unsafe_allow_html=True)

# --- 2. تهيئة مخزن البيانات السحابي ---
if 'page' not in st.session_state: st.session_state['page'] = "main"
if 'init_setup' not in st.session_state: st.session_state['init_setup'] = False
if 'school_info' not in st.session_state: st.session_state['school_info'] = {}
if 'staff_db' not in st.session_state: st.session_state['staff_db'] = {}
if 'chat_to_manager' not in st.session_state: st.session_state['chat_to_manager'] = []

# --- شريط الأخبار العلوي ---
st.markdown('<div class="news-ticker"><span>📢 وزارة التربية: رقمنة شاملة للمؤسسات لعام 2026/2027 ... مديرية التربية لولاية الشلف ترحب بكم ... نظام القيادة الإدارية جاهز للتشغيل</span></div>', unsafe_allow_html=True)

# --- 3. بوابة التنشيط (للمدير فقط لأول مرة) ---
if not st.session_state['init_setup']:
    st.markdown("<h2 style='text-align:center;'>🔐 تنشيط النظام (للمدير فقط)</h2>", unsafe_allow_html=True)
    with st.form("activation"):
        col1, col2 = st.columns(2)
        with col1:
            s_name = st.text_input("اسم المؤسسة التعليمية:")
            m_nom = st.text_input("لقب المدير:")
        with col2:
            s_type = st.selectbox("طور المؤسسة:", ["moyen", "secondaire"], format_func=lambda x: "متوسطة" if x=="moyen" else "ثانوية")
            m_phone = st.text_input("رقم هاتف المدير:")
        if st.form_submit_button("✅ تفعيل النظام"):
            if s_name and m_nom:
                st.session_state['school_info'] = {"اسم": s_name, "نوع": s_type, "مدير": m_nom}
                st.session_state['init_setup'] = True
                st.rerun()

# --- 4. الواجهة المركزية (أزرار 2026) ---
elif st.session_state['page'] == "main":
    st.markdown(f"<h2 style='text-align:center; color:#1e5631;'>{st.session_state['school_info']['اسم']}</h2>", unsafe_allow_html=True)
    st.write("---")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="main-card"><div class="card-title">🏢 فضاء المدير</div><small>الرقابة والقرار</small></div>', unsafe_allow_html=True)
        if st.button("دخول المدير", key="mgr", use_container_width=True): st.session_state['page'] = "manager"; st.rerun()
    with col2:
        st.markdown('<div class="main-card"><div class="card-title">📝 فضاء النائب</div><small>الهندسة والأساتذة</small></div>', unsafe_allow_html=True)
        if st.button("دخول النائب", key="vce", use_container_width=True): st.session_state['page'] = "vice"; st.rerun()
    with col3:
        st.markdown('<div class="main-card"><div class="card-title">🔑 فضاء الموظفين</div><small>البوابات الشخصية</small></div>', unsafe_allow_html=True)
        if st.button("دخول العائلة الإدارية", key="stf", use_container_width=True): st.session_state['page'] = "staff"; st.rerun()

# --- 5. فضاء المدير المالك ---
elif st.session_state['page'] == "manager":
    if st.button("🔙 عودة"): st.session_state['page'] = "main"; st.rerun()
    st.header("🏢 لوحة تحكم المدير")
    m_key = st.text_input("أدخل الكود السري للمدير:", type="password")
    if m_key == "ADMIN-2026":
        st.success(f"أهلاً سيادة المدير {st.session_state['school_info']['مدير']}")
        t1, t2 = st.tabs(["📩 بريد النائب", "📊 تسجيل نائب المدير"])
        with t2:
            v_name = st.text_input("اسم نائب المدير:")
            v_code = st.text_input("كود دخول النائب المخصص:")
            if st.button("اعتماد النائب"):
                st.session_state['vice_info'] = {"اسم": v_name, "كود": v_code}
                st.success("تم الحفظ.")
        with t1:
            st.write(st.session_state['chat_to_manager'])

# --- 6. فضاء نائب المدير (المهندس) ---
elif st.session_state['page'] == "vice":
    if st.button("🔙 عودة"): st.session_state['page'] = "main"; st.rerun()
    st.header("📝 مهندس النظام - نائب المدير")
    v_key = st.text_input("أدخل كودك التعريفي:", type="password")
    if 'vice_info' in st.session_state and v_key == st.session_state['vice_info']['كود']:
        t1, t2, t3 = st.tabs(["👥 تسجيل الموظفين", "📸 الأرشفة", "💬 مراسلة المدير"])
        with t1:
            with st.form("staff"):
                n = st.text_input("الاسم واللقب:")
                r = st.selectbox("الوظيفة:", ["أستاذ", "مقتصد", "أمين مخزن", "أمانة"])
                c = st.text_input("كود الدخول الممنوح:")
                if st.form_submit_button("توليد الهوية"):
                    st.session_state['staff_db'][c] = {"اسم": n, "رتبة": r}
                    st.success(f"تم تسجيل {n} بكود: {c}")
        with t3:
            msg = st.text_area("رسالة سرية للمدير:")
            if st.button("إرسال"): st.session_state['chat_to_manager'].append(msg); st.success("تم.")

# --- 7. فضاء الموظفين والأساتذة ---
elif st.session_state['page'] == "staff":
    if st.button("🔙 عودة"): st.session_state['page'] = "main"; st.rerun()
    st.header("🔑 بوابة الموظفين")
    code = st.text_input("أدخل كود الاشتراك الخاص بك:", type="password")
    if code in st.session_state['staff_db']:
        user = st.session_state['staff_db'][code]
        st.success(f"مرحباً {user['اسم']} | مصلحة: {user['رتبة']}")
        if user['رتبة'] == "أستاذ":
            st.link_button("🌐 بنك dzexams", "https://dzexams.com")
        elif user['رتبة'] == "مقتصد":
            st.camera_input("صوّر الفاتورة")

st.markdown("---")
st.markdown(f"<p style='text-align:center; color:grey;'>نظام القيادة الإدارية المتكامل v25.0 | 2026</p>", unsafe_allow_html=True)
