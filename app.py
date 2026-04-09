import streamlit as st
import pandas as pd
import datetime

# 1. إعدادات الواجهة والجماليات
st.set_page_config(page_title="نظام القيادة الإدارية 2026/2027", layout="wide")

st.markdown("""
    <style>
    @import url('https://googleapis.com');
    * { font-family: 'Cairo', sans-serif; text-align: right; }
    .main-header { background: linear-gradient(to left, #1e5631, #a7282e); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 35px; font-weight: bold; text-align: center; padding: 10px; }
    .official-doc { border: 2px solid black; padding: 30px; background: white; color: black; width: 100%; margin: auto; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
    .report-card { border: 3px double #1e5631; padding: 20px; background: #fdfdfd; color: black; }
    </style>
    """, unsafe_allow_html=True)

# 2. نظام الحماية
if 'auth' not in st.session_state:
    st.session_state['auth'] = False

if not st.session_state['auth']:
    st.markdown('<div style="text-align:center"><img src="https://githubusercontent.com" width="150"></div>', unsafe_allow_html=True)
    st.markdown("<div class='main-header'>نظام القيادة الإدارية المتكامل</div>", unsafe_allow_html=True)
    key = st.text_input("🔑 كود تفعيل المؤسسة:", type="password")
    if st.button("🚀 الدخول للنظام"):
        if key == "CHLEF-2026":
            st.session_state['auth'] = True
            st.rerun()
else:
    # 3. القائمة الجانبية المتطورة
    with st.sidebar:
        st.image("https://githubusercontent.com", width=100)
        choice = st.sidebar.selectbox("🛂 اختر الخدمة الإدارية:", [
            "🏠 الرئيسية",
            "📄 استخراج الشهادة المدرسية", 
            "📊 كشوف النقاط (المعدلات)", 
            "🆕 تسجيل التلاميذ والبطاقات",
            "💰 فضاء المقتصد",
            "👨‍🏫 فضاء الأستاذ"
        ])
        if st.sidebar.button("🔴 تسجيل خروج"):
            st.session_state['auth'] = False
            st.rerun()

    st.markdown(f"<div class='main-header'>{choice}</div>", unsafe_allow_html=True)

    # --- 1. قسم الشهادة المدرسية ---
    if choice == "📄 استخراج الشهادة المدرسية":
        st.subheader("📝 توليد شهادة مدرسية فورية")
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("الاسم واللقب:")
            birth_info = st.text_input("تاريخ ومكان الازدياد:")
        with col2:
            level = st.selectbox("السنة الدراسية:", ["1 ثانوي", "2 ثانوي", "3 ثانوي", "متوسط"])
            school_year = "2026 / 2027"

        if st.button("🖨️ معاينة وطباعة الشهادة"):
            st.markdown(f"""
            <div class="official-doc">
                <p style="text-align:center; font-weight:bold;">الجمهورية الجزائرية الديمقراطية الشعبية<br>وزارة التربية الوطنية</p>
                <div style="display:flex; justify-content:space-between;">
                    <span>مديرية التربية لولاية الشلف</span>
                    <span>المؤسسة: ....................</span>
                </div>
                <h2 style="text-align:center; text-decoration: underline;">شهادة مدرسية</h2>
                <p style="font-size:18px; line-height:2;">
                يشهد مدير المؤسسة المذكورة أعلاه أن التلميذ(ة): <b>{name}</b><br>
                المولود(ة) في: <b>{birth_info}</b><br>
                يتابع دراسته بالمؤسسة بانتظام في قسم: <b>{level}</b><br>
                للسنة الدراسية: <b>{school_year}</b> تحت رقم: <b>{datetime.datetime.now().strftime('%H%M%S')}</b>
                </p>
                <br>
                <div style="text-align:left;">
                    حرر بـ: الشلف في {datetime.date.today()}<br>
                    <b>إمضاء ومدير المؤسسة</b>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # --- 2. قسم كشوف النقاط ---
    elif choice == "📊 كشوف النقاط (المعدلات)":
        st.subheader("📉 حساب المعدل الفصلي واستخراج الكشف")
        col1, col2 = st.columns(2)
        with col1:
            st_name = st.text_input("اسم التلميذ:")
            math = st.number_input("الرياضيات:", 0.0, 20.0, 10.0)
            physics = st.number_input("الفيزياء:", 0.0, 20.0, 10.0)
        with col2:
            st_level = st.text_input("القسم:", "3 ثانوي")
            arabic = st.number_input("اللغة العربية:", 0.0, 20.0, 10.0)
            science = st.number_input("العلوم الطبيعية:", 0.0, 20.0, 10.0)

        # حساب المعدل البسيط
        total = (math + physics + arabic + science) / 4
        
        if st.button("📊 توليد كشف النقاط"):
            st.markdown(f"""
            <div class="report-card">
                <h3 style="text-align:center; color:#1e5631;">كشف نقاط الفصل الأول 2026/2027</h3>
                <p><b>التلميذ:</b> {st_name} | <b>القسم:</b> {st_level}</p>
                <table style="width:100%; border-collapse: collapse; text-align:center;">
                    <tr style="background:#1e5631; color:white;">
                        <th style="border:1px solid #ddd; padding:8px;">المادة</th>
                        <th style="border:1px solid #ddd; padding:8px;">النقطة</th>
                    </tr>
                    <tr><td>الرياضيات</td><td>{math}</td></tr>
                    <tr><td>الفيزياء</td><td>{physics}</td></tr>
                    <tr><td>اللغة العربية</td><td>{arabic}</td></tr>
                    <tr><td>العلوم الطبيعية</td><td>{science}</td></tr>
                    <tr style="background:#eee; font-weight:bold;">
                        <td>المعدل الفصلي</td>
                        <td style="color:{'green' if total >= 10 else 'red'};">{total:.2f} / 20</td>
                    </tr>
                </table>
                <p style="text-align:center; margin-top:10px;"><b>الملاحظة:</b> {'ناجح' if total >= 10 else 'راسب'}</p>
            </div>
            """, unsafe_allow_html=True)

    # --- باقي الأقسام ---
    elif choice == "🆕 تسجيل التلاميذ والبطاقات":
        st.subheader("📝 تسجيل وتوليد البطاقات")
        st.info("هذا القسم مربوط بنظام الكودبار الذي صممناه سابقاً.")

    elif choice == "🏠 الرئيسية":
        st.markdown("<h2 style='text-align:center;'>مرحباً بك في لوحة تحكم القيادة الإدارية</h2>", unsafe_allow_html=True)
        st.write("استخدم القائمة الجانبية لإدارة المؤسسة واستخراج الوثائق.")

st.markdown("---")
st.markdown("<p style='text-align:center; color:grey;'>نظام القيادة الإدارية v8.0 | وثائق رسمية 2026/2027 | ولاية الشلف</p>", unsafe_allow_html=True)
    
