import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="نظام القيادة الإدارية المتكامل", layout="wide")

# العلم والعناوين الرسمية
st.markdown('<div style="text-align:center"><img src="https://githubusercontent.com" width="120"></div>', unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center; color:#1e5631;'>الجمهورية الجزائرية الديمقراطية الشعبية</h2>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center; color:#1e5631;'>وزارة التربية الوطنية - ولاية الشلف</h3>", unsafe_allow_html=True)

st.write("---")

# القائمة الجانبية الذكية للتنقل بين المصالح
st.sidebar.title("🛂 لوحة التحكم")
choice = st.sidebar.radio("اختر القسم العملي:", 
    ["🏠 الرئيسية", "💰 المقتصد", "🔍 الغيابات والكودبار", "📦 أمين المخزن", "📚 المكتبة", "👨‍🏫 فضاء الأستاذ", "📝 نائب المدير"])

if choice == "🏠 الرئيسية":
    st.info("مرحباً بك في النظام الرقمي المتكامل للمؤسسة")
    school = st.text_input("📍 اسم المؤسسة التعليمية:", "ثانوية العقيد لطفي")
    st.success(f"تم تسجيل الدخول لنظام: {school}")

elif choice == "💰 المقتصد":
    st.header("💵 تسيير الميزانية والجرد الآلي")
    mizania = st.number_input("إجمالي الميزانية السنوية (دج):", min_value=0)
    st.subheader("📸 تصوير الفواتير")
    img = st.camera_input("التقط صورة للفاتورة للجرد")
    if img: st.success("تم التقاط الفاتورة بنجاح")

elif choice == "🔍 الغيابات والكودبار":
    st.header("🏷️ نظام تتبع الغيابات بالأرشيف")
    st.subheader("توليد كودبار جديد")
    id_val = st.text_input("أدخل رقم التلميذ أو رمز القسم:")
    if st.button("توليد الكود"):
        st.success(f"تم إنشاء كودبار خاص بـ: {id_val} (جاهز للطباعة)")
    st.write("---")
    st.subheader("📷 ماسح الغيابات")
    st.camera_input("وجه كاميرا الجوال نحو كودبار التلميذ")

elif choice == "👨‍🏫 فضاء الأستاذ":
    st.header("📝 متابعة التلاميذ والغيابات")
    st.date_input("تاريخ اليوم")
    st.text_input("القسم (مثلاً: 3 ثانوي)")
    st.button("تأكيد سجل الحضور")

# تذييل الحقوق للبيع
st.markdown("---")
st.markdown("<p style='text-align:center; color:grey;'>نظام القيادة الإدارية v1.0 | جميع الحقوق محفوظة © 2026</p>", unsafe_allow_html=True)
                 
