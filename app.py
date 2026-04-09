import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="نظام القيادة الإدارية - فضاء الأستاذ", layout="wide")

# --- الواجهة الرسمية ---
st.markdown('<div style="text-align:center"><img src="https://githubusercontent.com" width="120"></div>', unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center;'>فضاء الأستاذ والوثائق التربوية</h2>", unsafe_allow_html=True)

# القائمة الجانبية للأقسام
menu = ["🏠 الرئيسية", "👨‍🏫 فضاء الأستاذ المخصص", "⚖️ القانون الداخلي والمناشور", "📊 تتبع غيابات تلاميذي"]
choice = st.sidebar.selectbox("القائمة الإدارية", menu)

# --- 1. فضاء الأستاذ المخصص ---
if choice == "👨‍🏫 فضاء الأستاذ المخصص":
    st.header("📚 الحقيبة البيداغوجية للأستاذ")
    
    col1, col2 = st.columns(2)
    with col1:
        subject = st.selectbox("اختر المادة:", ["الرياضيات", "العلوم الطبيعية", "الفيزياء", "اللغة العربية", "تاريخ وجغرافيا"])
        class_level = st.selectbox("المستوى:", ["1 ثانوي", "2 ثانوي", "3 ثانوي"])
    
    st.divider()
    
    # أقسام الملفات
    tab1, tab2, tab3 = st.tabs(["📝 مذكرات الأستاذ", "📖 ملخصات الدروس", "📂 تطبيقات وتمارين"])
    
    with tab1:
        st.subheader("إدارة المذكرات التربوية")
        st.file_uploader("رفع مذكرة جديدة (PDF)", type=['pdf'])
        st.info("المذكرات الحالية: مذكرة الوحدة الأولى، مذكرة التخطيط السنوي.")

    with tab2:
        st.subheader("ملخصات الدروس المدعومة")
        st.write("هنا تظهر ملخصات الدروس الموجهة للتلاميذ:")
        st.button(f"تحميل ملخصات مادة {subject}")
        
    with tab3:
        st.subheader("بنك التطبيقات والتمارين")
        st.write("سلسلة تمارين الدعم والتقويم المستمر.")
        st.button("إرسال التمارين لقسم التلاميذ")

# --- 2. القانون الداخلي والمناشور الوزارية ---
elif choice == "⚖️ القانون الداخلي والمناشور":
    st.header("⚖️ المرجعية القانونية للمؤسسة")
    
    with st.expander("📄 القانون الداخلي للمدرسة"):
        st.write("""
        1. الالتزام بالوقت الرسمي للدخول والخروج.
        2. منع التدخين داخل الحرم المدرسي.
        3. الالتزام بالهندام الرسمي.
        """)
        st.download_button("تحميل القانون الداخلي PDF", "data", "law.pdf")

    with st.expander("📜 القانون الأساسي لعمال التربية"):
        st.write("تفاصيل الحقوق والواجبات المهنية للأستاذ.")
        st.button("الاطلاع على المنشور الوزاري 2026")

# --- 3. تتبع الغيابات ---
elif choice == "📊 تتبع غيابات تلاميذي":
    st.header("🔍 سجل الحضور والغياب بالكودبار")
    with st.expander("📸 فتح ماسح الكودبار لتسجيل غياب الحصة"):
        st.camera_input("امسح كود التلميذ")

# تذييل الحقوق
st.markdown("---")
st.markdown("<p style='text-align:center; color:grey;'>نظام القيادة الإدارية v3.0 | تصميم تجاري محمي © 2026</p>", unsafe_allow_html=True)
