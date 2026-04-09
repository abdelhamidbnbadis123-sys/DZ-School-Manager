import streamlit as st
import pandas as pd
from PIL import Image

# 1. إعدادات الواجهة المتطورة
st.set_page_config(page_title="نظام القيادة الإدارية 2026", layout="wide")

# 2. لمسات 2026 (CSS الشامل)
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    * { font-family: 'Cairo', sans-serif; text-align: right; }
    
    /* ستايل العناوين */
    .main-header {
        background: linear-gradient(to left, #1e5631, #ffffff, #a7282e);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 35px; font-weight: bold; text-align: center;
        padding: 20px;
    }
    
    /* تصميم الأزرار */
    .stButton>button {
        background: linear-gradient(45deg, #1e5631, #a7282e) !important;
        color: white !important;
        border-radius: 15px !important;
        font-weight: bold !important;
        width: 100%; border: none !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. نظام الحماية
if 'auth' not in st.session_state:
    st.session_state['auth'] = False

if not st.session_state['auth']:
    st.markdown('<div style="text-align:center"><img src="https://githubusercontent.com" width="180"></div>', unsafe_allow_html=True)
    st.markdown("<div class='main-header'>الجمهورية الجزائرية الديمقراطية الشعبية</div>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center;'>نظام القيادة الإدارية للمتوسطات والثانويات</h3>", unsafe_allow_html=True)
    st.write("---")
    key = st.text_input("🔑 أدخل مفتاح التفعيل للمؤسسة:", type="password")
    if st.button("🚀 دخول للنظام"):
        if key == "CHLEF-2026":
            st.session_state['auth'] = True
            st.balloons()
            st.rerun()
else:
    # 4. القائمة الجانبية الشاملة (كل ما كان ناقصاً)
    with st.sidebar:
        st.markdown('<div style="text-align:center"><img src="https://githubusercontent.com" width="100"></div>', unsafe_allow_html=True)
        st.write("---")
        choice = st.radio("🛂 اختر الفضاء الإداري:", [
            "🏢 مدير المؤسسة", 
            "💰 المقتصد والمالية", 
            "📝 نائب المدير", 
            "👨‍🏫 فضاء الأستاذ", 
            "📋 الكودبار والتلاميذ", 
            "📦 أمين المخزن", 
            "📚 المكتبة والأرشيف", 
            "👷 العمال والخدمات"
        ])
        if st.button("🔴 تسجيل خروج"):
            st.session_state['auth'] = False
            st.rerun()

    # 5. محتوى الأقسام (تفعيل كل الأزرار)
    st.markdown(f"<div class='main-header'>{choice}</div>", unsafe_allow_html=True)

    if choice == "🏢 مدير المؤسسة":
        col1, col2 = st.columns(2)
        col1.metric("إحصائيات الحضور", "98%", "+2%")
        col2.metric("جاهزية المؤسسة", "100%", "مثالي")
        st.info("📢 إشعار للمدير: تم تحديث قوائم التلاميذ السنوية آلياً.")

    elif choice == "💰 المقتصد والمالية":
        st.subheader("💵 تسيير الميزانية والجرد الذكي")
        miz = st.number_input("الميزانية الكلية (دج):", value=3000000)
        st.write(f"🔹 الإطعام: {miz*0.5:,} | 🔹 الصيانة: {miz*0.2:,}")
        st.camera_input("📸 صوّر الفاتورة للجرد التلقائي")

    elif choice == "👨‍🏫 فضاء الأستاذ":
        tab1, tab2, tab3 = st.tabs(["📝 المذكرات", "📖 الدروس", "⚖️ القانون الداخلي"])
        with tab1: st.file_uploader("رفع مذكرة الأستاذ PDF")
        with tab2: st.button("تحميل ملخصات المواد")
        with tab3: st.write("📜 **القانون الداخلي:** مادة 01: الالتزام بالوقت الرسمي والواجب التربوي.")

    elif choice == "📋 الكودبار والتلاميذ":
        st.subheader("🏷️ أتمتة الكودبار والأرشفة")
        st.camera_input("📸 صوّر القائمة الورقية لاستخراج الكودبار")
        st.write("سوف يتم إنشاء كودبار لكل تلميذ بجانب اسمه آلياً.")

    elif choice == "📦 أمين المخزن":
        st.subheader("📦 جرد الوسائل")
        st.data_editor({"الوسيلة": ["طاولات", "كراسي", "حواسيب"], "الكمية": [200, 400, 15], "الحالة": ["جيد", "صيانة", "جديد"]})

    elif choice == "📝 نائب المدير":
        st.subheader("🗓️ تنظيم الجداول والغيابات")
        st.button("توليد جدول الحراسة الأسبوعي")
        st.camera_input("📸 مسح غياب التلاميذ بالكودبار")

    elif choice == "📚 المكتبة والأرشيف":
        st.subheader("📚 إعارة الكتب والأرشفة الرقمية")
        st.text_input("ابحث عن كتاب أو ملف أرشيف (سنة 2024-2026):")
        st.button("جرد المكتبة السنوي")

st.markdown("---")
st.markdown("<p style='text-align:center; color:grey;'>نظام القيادة الإدارية الذكي v6.0 | ولاية الشلف © 2026</p>", unsafe_allow_html=True)
