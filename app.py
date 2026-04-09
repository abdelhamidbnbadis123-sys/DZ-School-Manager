import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة والجماليات
st.set_page_config(page_title="نظام القيادة الإدارية 2026", layout="wide", initial_sidebar_state="expanded")

# 2. حقن كود CSS لتغيير شكل التطبيق جذرياً (واجهة 2026)
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    
    html, body, [class*="css"] {
        font-family: 'Cairo', sans-serif;
        text-align: right;
    }
    
    /* خلفية زجاجية للكروت */
    .stMetric {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 15px;
        padding: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    }
    
    /* تصميم الأزرار */
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3em;
        background: linear-gradient(45deg, #1e5631, #a7282e);
        color: white;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    }
    
    /* تنسيق الهيدر */
    .header-style {
        background: linear-gradient(to left, #1e5631, #ffffff, #a7282e);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
        font-size: 35px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. نظام الحماية (مفتاح التفعيل)
if 'auth' not in st.session_state:
    st.session_state['auth'] = False

if not st.session_state['auth']:
    st.markdown('<div style="text-align:center"><img src="https://githubusercontent.com" width="180"></div>', unsafe_allow_html=True)
    st.markdown("<h1 class='header-style'>نظام القيادة الإدارية المتكامل</h1>", unsafe_allow_html=True)
    
    with st.container():
        st.write("---")
        st.subheader("🔑 تفعيل النسخة المعتمدة")
        key = st.text_input("أدخل مفتاح الترخيص الخاص بالمؤسسة:", type="password")
        if st.button("🚀 فتح النظام"):
            if key == "CHLEF-2026":
                st.session_state['auth'] = True
                st.balloons()
                st.rerun()
            else:
                st.error("المفتاح غير صحيح. يرجى مراجعة المبرمج.")
else:
    # 4. لوحة التحكم الجانبية (Glassmorphism Sidebar)
    with st.sidebar:
        st.image("https://githubusercontent.com", width=120)
        st.markdown("### 🛂 الصلاحيات")
        choice = st.radio("", ["🏠 لوحة التحكم", "💰 المقتصد والمالية", "👨‍🏫 فضاء الأستاذ", "📋 الكودبار والتلاميذ", "⚖️ المكتبة والأرشيف"])
        st.write("---")
        if st.button("🔴 خروج"):
            st.session_state['auth'] = False
            st.rerun()

    # 5. محتوى الأقسام
    st.markdown(f"<h1 class='header-style'>{choice}</h1>", unsafe_allow_html=True)

    if choice == "🏠 لوحة التحكم":
        st.write("📍 **المؤسسة:** ثانوية العقيد لطفي - ولاية الشلف")
        col1, col2, col3 = st.columns(3)
        with col1: st.metric("التلاميذ", "1,240", "+12")
        with col2: st.metric("الميزانية", "45%", "-2%")
        with col3: st.metric("الحضور", "98%", "+1%")
        
        st.markdown("### 📢 إعلانات المديرية")
        st.info("إعلان: انطلاق عملية الجرد السنوي للوسائل التربوية ابتداءً من الأسبوع القادم.")

    elif choice == "💰 المقتصد والمالية":
        tab1, tab2 = st.tabs(["💵 تسيير الميزانية", "📸 جرد الفواتير"])
        with tab1:
            st.write("توزيع الميزانية (دج):")
            miz = st.number_input("الميزانية الكلية:", value=2500000)
            st.write(f"🔹 الإطعام: {miz*0.5:,} | 🔹 الصيانة: {miz*0.2:,}")
        with tab2:
            st.camera_input("التقط صورة الفاتورة للجرد الآلي")

    elif choice == "👨‍🏫 فضاء الأستاذ":
        st.subheader("📝 مذكرات وملخصات الأستاذ")
        col1, col2 = st.columns(2)
        with col1: st.button("📁 تحميل المذكرات الوزارية")
        with col2: st.button("📖 رفع ملخصات الدروس")
        st.markdown("---")
        st.write("📜 **القانون الداخلي:** الالتزام بالهندام والوقت الرسمي.")

    elif choice == "📋 الكودبار والتلاميذ":
        st.subheader("🏷️ أتمتة الكودبار")
        cam = st.camera_input("صوّر القائمة الورقية لاستخراج التلاميذ")
        if cam:
            st.success("تم تحليل القائمة وتوليد الأكواد بنجاح!")
            st.table(pd.DataFrame({"الاسم": ["محمد بوضياف", "أحمد زبانة"], "الكود": ["1001", "1002"]}))

    st.markdown("---")
    st.markdown("<p style='text-align:center; color:grey;'>نظام القيادة الإدارية الذكي v5.0 | جميع الحقوق محفوظة © 2026</p>", unsafe_allow_html=True)
    
