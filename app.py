import streamlit as st
import pandas as pd
import datetime

# --- إعدادات النظام الأساسية ---
st.set_page_config(page_title="نظام القيادة الإدارية المتكامل", layout="wide")

# --- نظام الحماية والترخيص (للبيع) ---
if 'auth' not in st.session_state:
    st.session_state['auth'] = False

def check_license(key):
    # قائمة مفاتيح التفعيل للمؤسسات التي تدفع لك
    valid_keys = ["CHLEF-2026", "ALGER-EDU", "PRO-ADMIN-01"]
    return key in valid_keys

if not st.session_state['auth']:
    st.markdown('<div style="text-align:center"><img src="https://githubusercontent.com" width="150"></div>', unsafe_allow_html=True)
    st.title("🔐 بوابة نظام القيادة الإدارية")
    st.info("يرجى إدخال مفتاح التفعيل لفتح خدمات المؤسسة")
    license_key = st.text_input("مفتاح الترخيص:", type="password")
    if st.button("تفعيل النظام"):
        if check_license(license_key):
            st.session_state['auth'] = True
            st.success("تم تفعيل النسخة بنجاح!")
            st.rerun()
        else:
            st.error("مفتاح خاطئ! تواصل مع المالك للحصول على التفعيل.")
else:
    # --- الواجهة الرئيسية بعد التفعيل ---
    st.sidebar.image("https://githubusercontent.com", width=80)
    st.sidebar.title("🛂 لوحة التحكم")
    choice = st.sidebar.selectbox("اختر الفضاء الإداري:", 
        ["🏠 الرئيسية", "💰 المقتصد", "👨‍🏫 فضاء الأستاذ", "📋 إدارة التلاميذ والكودبار", "⚖️ القانون والأرشيف"])

    # العناوين الرسمية
    st.markdown("<h2 style='text-align:center; color:#1e5631;'>الجمهورية الجزائرية الديمقراطية الشعبية</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center; color:#1e5631;'>وزارة التربية الوطنية - ولاية الشلف</h3>", unsafe_allow_html=True)
    st.write("---")

    # --- 1. الشاشة الرئيسية ---
    if choice == "🏠 الرئيسية":
        st.header("📍 بيانات المؤسسة")
        school = st.text_input("اسم المؤسسة التعليمية:", "ثانوية العقيد لطفي")
        col1, col2, col3 = st.columns(3)
        col1.metric("إجمالي التلاميذ", "1240", "+5")
        col2.metric("الميزانية المستهلكة", "35%", "مستقر")
        col3.metric("نسبة الغيابات", "2.1%", "-0.5%")

    # --- 2. فضاء المقتصد ---
    elif choice == "💰 المقتصد":
        st.header("💵 تسيير الميزانية والجرد الذكي")
        mizania = st.number_input("الميزانية السنوية (دج):", value=2000000)
        
        tab1, tab2 = st.tabs(["📊 تقسيم الميزانية", "📸 جرد الفواتير"])
        with tab1:
            st.write("التوزيع حسب الأبواب:")
            st.info(f"إطعام (50%): {mizania*0.5:,} دج")
            st.info(f"صيانة (20%): {mizania*0.2:,} دج")
            st.info(f"أدوات تربوية (30%): {mizania*0.3:,} دج")
        with tab2:
            with st.expander("فتح كاميرا الجرد"):
                img = st.camera_input("صوّر الفاتورة")
                if img: st.success("تم الالتقاط! جاري استخراج البيانات للجرد التلقائي.")

    # --- 3. فضاء الأستاذ (الحقيبة الرقمية) ---
    elif choice == "👨‍🏫 فضاء الأستاذ":
        st.header("📚 الحقيبة البيداغوجية للأستاذ")
        sub = st.selectbox("المادة:", ["رياضيات", "علوم", "فيزياء", "لغة عربية"])
        
        tab1, tab2, tab3 = st.tabs(["📝 المذكرات", "📖 ملخصات الدروس", "📂 تطبيقات وتلاميذي"])
        with tab1:
            st.subheader("إدارة المذكرات")
            st.file_uploader("رفع مذكرة PDF")
            st.write("قائمة المذكرات الحالية متوفرة للتحميل.")
        with tab2:
            st.subheader("دروس مدعومة")
            st.button(f"تحميل ملخصات {sub}")
        with tab3:
            st.subheader("تطبيقات ونتائج")
            st.button("إرسال تمارين للقسم")

    # --- 4. إدارة التلاميذ والكودبار ---
    elif choice == "📋 إدارة التلاميذ والكودبار":
        st.header("📋 أتمتة قوائم التلاميذ")
        with st.expander("📸 تصوير القائمة الاسمية"):
            list_img = st.camera_input("صوّر قائمة القسم")
            if list_img:
                st.success("تم تحليل القائمة!")
                df = pd.DataFrame({
                    "اسم التلميذ": ["محمد. ب", "سارة. ج", "أمين. ك"],
                    "الكودبار": ["|||| 101", "|||| 102", "|||| 103"]
                })
                st.table(df)

    # --- 5. القانون والأرشيف ---
    elif choice == "⚖️ القانون والأرشيف":
        st.header("⚖️ المرجعية القانونية والأرشيف")
        with st.expander("📄 القانون الداخلي للمؤسسة"):
            st.write("تحميل واطلاع على بنود القانون الداخلي.")
        with st.expander("📜 القانون الأساسي لعمال التربية"):
            st.write("مرجع الحقوق والواجبات المهنية.")
        with st.expander("🗄️ الأرشيف السنوي"):
            year = st.selectbox("اختر السنة:", ["2024", "2025", "2026"])
            st.button(f"تحميل أرشيف سنة {year}")

    # تذييل الحقوق (لأغراض البيع)
    st.markdown("---")
    st.markdown("<p style='text-align:center; color:grey;'>نظام القيادة الإدارية v4.0 | تصميم تجاري محمي © 2026 | ولاية الشلف</p>", unsafe_allow_html=True)
    
