import streamlit as st

# 1. إعدادات النظام التجارية
st.set_page_config(page_title="نظام القيادة الإدارية v1.0", layout="wide")

# دالة حماية النظام (التحقق من التفعيل)
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

def check_license(user_key):
    # يمكنك تغيير هذا الكود لكل مؤسسة تبيعها
    # مثال: مؤسسة الشلف 1 لها كود: CHLEF-01-2026
    licenses = ["CHLEF-01-2026", "ALGER-2026", "DEMO-123"]
    return user_key in licenses

# --- شاشة الدخول والحماية ---
if not st.session_state['authenticated']:
    st.markdown('<div style="text-align:center"><img src="https://githubusercontent.com" width="150"></div>', unsafe_allow_html=True)
    st.title("🛡️ نظام القيادة الإدارية - ولاية الشلف")
    st.subheader("يرجى إدخال مفتاح التفعيل لفتح النظام")
    
    license_input = st.text_input("مفتاح الترخيص (License Key):", type="password")
    if st.button("تفعيل ونشر النظام"):
        if check_license(license_input):
            st.session_state['authenticated'] = True
            st.success("تم تفعيل النسخة بنجاح للمؤسسة!")
            st.balloons()
            st.rerun()
        else:
            st.error("مفتاح التفعيل خاطئ! يرجى التواصل مع المبرمج للحصول على نسخة مدفوعة.")
            st.info("للتواصل وطلب التفعيل: [ضع رقم هاتفك هنا]")
else:
    # --- الواجهة الاحترافية بعد التفعيل ---
    st.sidebar.success("✅ نسخة مرخصة")
    if st.sidebar.button("تسجيل الخروج"):
        st.session_state['authenticated'] = False
        st.rerun()

    st.markdown("<h2 style='text-align:center; color:#1e5631;'>الجمهورية الجزائرية الديمقراطية الشعبية</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center; color:#1e5631;'>وزارة التربية الوطنية - ولاية الشلف</h3>", unsafe_allow_html=True)
    
    st.write("---")
    
    menu = ["💰 فضاء المقتصد", "🔍 نظام الكودبار", "📦 أمين المخزن", "🏢 إدارة المؤسسة"]
    choice = st.sidebar.selectbox("اختر فضاء العمل:", menu)

    if choice == "💰 فضاء المقتصد":
        st.header("💵 تسيير الميزانية وجرد الفواتير الذكي")
        mizania = st.number_input("إجمالي الميزانية السنوية (دج):", min_value=0)
        
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("📸 تصوير الفواتير")
            img = st.camera_input("التقط صورة للفاتورة للجرد التلقائي")
            if img:
                st.image(img, caption="تم استلام الفاتورة")
                st.warning("جاري تحليل البيانات واستخراج المصاريف...")
        
        with col2:
            st.subheader("📊 توزيع الميزانية")
            if mizania > 0:
                st.write(f"🔹 الإطعام (50%): {mizania*0.5:,.2f} دج")
                st.write(f"🔹 الصيانة (20%): {mizania*0.2:,.2f} دج")
                st.write(f"🔹 الوسائل (30%): {mizania*0.3:,.2f} دج")

    elif choice == "🔍 نظام الكودبار":
        st.header("🏷️ نظام الكودبار والأرشفة")
        st.write("هذا القسم مخصص لتوليد بطاقات التلاميذ وتتبع الغيابات.")
        name = st.text_input("اسم التلميذ أو رقم الملف:")
        if st.button("توليد كودبار للطباعة"):
            st.success(f"تم إنشاء الكود الخاص بـ {name}")

    st.markdown("---")
    st.markdown("<p style='text-align:center; color:grey;'>نظام القيادة الإدارية v1.0 | جميع الحقوق محفوظة © 2026</p>", unsafe_allow_html=True)
                
