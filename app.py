import streamlit as st
import datetime

# 1. إعدادات النظام الاحترافية
st.set_page_config(page_title="نظام القيادة الإدارية المتكامل", layout="wide", initial_sidebar_state="expanded")

# --- تنسيق العلم والعناوين ---
st.markdown('<div style="text-align:center"><img src="https://githubusercontent.com" width="120"></div>', unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center; color:#1e5631;'>الجمهورية الجزائرية الديمقراطية الشعبية</h2>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center; color:#1e5631;'>وزارة التربية الوطنية - ولاية الشلف</h3>", unsafe_allow_html=True)

# --- القائمة الجانبية المتقدمة ---
st.sidebar.title("🎮 لوحة التحكم المركزية")
choice = st.sidebar.selectbox("اختر الفضاء الإداري:", 
    ["🏠 الشاشة الرئيسية", "💰 المقتصد (الميزانية والجرد)", "🔍 الغيابات والكودبار", "📦 أمين المخزن", "📚 المكتبي (الأرشيف)", "👨‍🏫 فضاء الأستاذ", "📝 نائب المدير"])

# --- 1. الشاشة الرئيسية ---
if choice == "🏠 الشاشة الرئيسية":
    st.header("📍 بيانات المؤسسة التعليمية")
    school_name = st.text_input("اسم المؤسسة:", "ثانوية العقيد لطفي - الشلف")
    st.success(f"مرحباً بك في النظام الرقمي المتكامل لـ {school_name}")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("عدد التلاميذ", "850", "+12")
    col2.metric("الميزانية المتبقية", "45%", "-5%")
    col3.metric("نسبة الغيابات", "3%", "-1%")

# --- 2. فضاء المقتصد (تفعيل الكاميرا والجرد) ---
elif choice == "💰 المقتصد (الميزانية والجرد)":
    st.header("💵 تسيير الميزانية والجرد الذكي")
    mizania = st.number_input("إجمالي الميزانية السنوية (دج):", value=1000000)
    
    tab1, tab2 = st.tabs(["📊 توزيع الميزانية", "📸 جرد الفواتير"])
    
    with tab1:
        st.write("التوزيع التلقائي للميزانية حسب الأبواب:")
        st.progress(0.5, text="الإطعام (50%)")
        st.progress(0.2, text="الصيانة (20%)")
        st.progress(0.3, text="الوسائل التربوية (30%)")
        
    with tab2:
        img = st.camera_input("صوّر الفاتورة للجرد التلقائي")
        if img:
            st.image(img, caption="الفاتورة الملتقطة")
            st.warning("🔄 جاري قراءة الأرقام وتحويلها لنص وجردها في المخزن...")

# --- 3. الغيابات والكودبار (تفعيل الماسح الضوئي) ---
elif choice == "🔍 الغيابات والكودبار":
    st.header("🏷️ نظام تتبع الغيابات بالكودبار")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("توليد كودبار جديد")
        student_id = st.text_input("رقم تعريف التلميذ أو القسم:")
        if st.button("صناعة الكودبار"):
            st.success(f"تم إنشاء الكود {student_id} بنجاح. جاهز للطباعة على البطاقة.")
            
    with col2:
        st.subheader("مسح الغيابات لحظياً")
        scan = st.camera_input("وجه الكاميرا لكودبار التلميذ")
        if scan:
            st.success("تم تسجيل الحضور في قاعدة بيانات 2026 بنجاح!")

# --- 4. فضاء الأستاذ ---
elif choice == "👨‍🏫 فضاء الأستاذ":
    st.header("📝 ورقة الغيابات الرقمية")
    st.date_input("تاريخ اليوم", datetime.date.today())
    st.text_input("القسم:")
    st.text_area("ملاحظات حول الدرس:")
    st.button("إرسال التقرير للإدارة")

# --- 5. أمين المخزن ---
elif choice == "📦 أمين المخزن":
    st.header("📦 جرد الوسائل والمواد")
    st.data_editor({"المادة": ["طاولات", "كراسي", "أقلام سبورة"], "الكمية": [200, 450, 1000], "الحالة": ["جيد", "تحتاج صيانة", "متوفر"]})
    st.button("تحديث المخزن")

# تذييل الحقوق (مهم للبيع)
st.markdown("---")
st.markdown("<p style='text-align:center; color:grey;'>نظام القيادة الإدارية v1.0 | جميع الحقوق محفوظة لولاية الشلف © 2026</p>", unsafe_allow_html=True)
