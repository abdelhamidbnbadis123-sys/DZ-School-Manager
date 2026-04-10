import streamlit as st
import pandas as pd
import json
import os
from datetime import datetime

# --- 1. وظائف الحفظ المحلي (للعمل بدون إنترنت) ---
DB_FILE = "school_data_2026.json"

def save_data():
    data = {
        'school_info': st.session_state.get('school_info', {}),
        'staff_db': st.session_state.get('staff_db', {}),
        'chat_to_manager': st.session_state.get('chat_to_manager', []),
        'init_setup': st.session_state.get('init_setup', False),
        'staff_locations': st.session_state.get('staff_locations', [])
    }
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def load_data():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return None

# --- 2. إعدادات الواجهة والجماليات ---
st.set_page_config(page_title="نظام القيادة الإدارية 2026", layout="wide")

# استعادة البيانات عند بدء التشغيل
saved_data = load_data()
if saved_data and 'init_setup' not in st.session_state:
    st.session_state.update(saved_data)

# تهيئة المتغيرات إذا كانت فارغة
if 'page' not in st.session_state: st.session_state['page'] = "main"
if 'init_setup' not in st.session_state: st.session_state['init_setup'] = False
if 'staff_db' not in st.session_state: st.session_state['staff_db'] = {}
if 'chat_to_manager' not in st.session_state: st.session_state['chat_to_manager'] = []
if 'staff_locations' not in st.session_state: st.session_state['staff_locations'] = []

st.markdown("""
    <style>
    @import url('https://googleapis.com');
    * { font-family: 'Cairo', sans-serif; text-align: right; }
    .stApp { background-color: #f4f7f6; }
    .main-card {
        background: white; padding: 20px; border-radius: 15px;
        border-right: 10px solid #1e5631; shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center; transition: 0.3s;
    }
    .news-ticker {
        background: #a7282e; color: white; padding: 10px; border-radius: 8px;
        overflow: hidden; white-space: nowrap; font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- شريط الأخبار ---
st.markdown('<div class="news-ticker">📢 نظام القيادة الإدارية لولاية الشلف - وضع العمل المحلي (Offline) مفعل بنجاح</div>', unsafe_allow_html=True)

# --- 3. بوابة التنشيط ---
if not st.session_state['init_setup']:
    st.markdown("<h2 style='text-align:center;'>🔐 تنشيط النظام لأول مرة</h2>", unsafe_allow_html=True)
    with st.form("activation"):
        s_name = st.text_input("اسم المؤسسة التعليمية:")
        m_nom = st.text_input("لقب المدير:")
        if st.form_submit_button("✅ تفعيل النظام وحفظه محلياً"):
            st.session_state['school_info'] = {"اسم": s_name, "مدير": m_nom}
            st.session_state['init_setup'] = True
            save_data()
            st.rerun()

# --- 4. الواجهة المركزية ---
elif st.session_state['page'] == "main":
    st.title(f"🏢 {st.session_state['school_info'].get('اسم', 'المؤسسة')}")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="main-card"><h3>🏢 المدير</h3></div>', unsafe_allow_html=True)
        if st.button("دخول الإدارة", use_container_width=True): st.session_state['page'] = "manager"; st.rerun()
    with col2:
        st.markdown('<div class="main-card"><h3>📝 النائب</h3></div>', unsafe_allow_html=True)
        if st.button("دخول الأمانة", use_container_width=True): st.session_state['page'] = "vice"; st.rerun()
    with col3:
        st.markdown('<div class="main-card"><h3>🔑 الموظفين</h3></div>', unsafe_allow_html=True)
        if st.button("دخول الطاقم", use_container_width=True): st.session_state['page'] = "staff"; st.rerun()

# --- 5. فضاء المدير (مع الخريطة GPS) ---
elif st.session_state['page'] == "manager":
    if st.button("🔙 عودة"): st.session_state['page'] = "main"; st.rerun()
    st.header("📊 لوحة قيادة المدير")
    
    tab1, tab2, tab3 = st.tabs(["📍 خريطة الموظفين (GPS)", "📩 البريد الوارد", "⚙️ الإعدادات"])
    
    with tab1:
        st.subheader("مواقع الموظفين الحالية (داخل المؤسسة)")
        if st.session_state['staff_locations']:
            df_map = pd.DataFrame(st.session_state['staff_locations'])
            st.map(df_map) # عرض الخريطة
        else:
            st.info("لا توجد بيانات موقع حالياً. يجب على الموظفين تفعيل الموقع من حساباتهم.")

    with tab2:
        for m in st.session_state['chat_to_manager']:
            st.info(m)

# --- 6. فضاء الموظفين (مع ميزة إرسال الموقع) ---
elif st.session_state['page'] == "staff":
    if st.button("🔙 عودة"): st.session_state['page'] = "main"; st.rerun()
    code = st.text_input("كود الدخول:", type="password")
    if code in st.session_state['staff_db']:
        user = st.session_state['staff_db'][code]
        st.success(f"مرحباً {user['اسم']}")
        
        # ميزة الـ GPS للموظف
        st.write("🛰️ تحديث موقعك في الخريطة الإدارية:")
        if st.button("إرسال موقعي الحالي للمدير"):
            # إحداثيات افتراضية لولاية الشلف (كمثال)
            new_loc = {"lat": 36.16, "lon": 1.33, "name": user['اسم']}
            st.session_state['staff_locations'].append(new_loc)
            save_data()
            st.success("تم تحديث موقعك على خريطة المدير.")

# --- 7. فضاء النائب (إضافة حفظ تلقائي) ---
elif st.session_state['page'] == "vice":
    if st.button("🔙 عودة"): st.session_state['page'] = "main"; st.rerun()
    # (نفس كودك السابق مع إضافة save_data بعد كل عملية تسجيل)
    with st.form("add_staff"):
        n = st.text_input("اسم الموظف:")
        c = st.text_input("كود مخصص:")
        if st.form_submit_button("تسجيل"):
            st.session_state['staff_db'][c] = {"اسم": n}
            save_data() # حفظ في الملف المحلي
            st.success("تم الحفظ في قاعدة البيانات المحلية.")

st.markdown("---")
st.caption("نظام القيادة الذكية v26.0 - يعمل بالكامل بدون إنترنت")
