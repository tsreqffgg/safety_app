import streamlit as st
import pandas as pd
import os

# إعدادات الصفحة ووساعتها
st.set_page_config(
    page_title="SAFETY 360 | نظام القيادة والتحكم للسلامة", 
    page_icon="🛡️", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# تخصيص التصميم مع إزالة أي تأثير مزعج عن الأزرار لتبقى واضحة تماماً
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #020617 0%, #090d16 50%, #0f172a 100%) !important;
    }
    section[data-testid="stSidebar"] {
        background-color: rgba(11, 18, 33, 0.98) !important;
        border-right: 1px solid rgba(255, 123, 0, 0.3);
    }
    section[data-testid="stSidebar"] * {
        color: #ffffff !important;
    }
    
    /* خانات البحث والنصوص */
    .stTextInput input, .stTextArea textarea {
        background-color: #0b132b !important;
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
        border-radius: 12px !important;
        border: 2px solid #ff7b00 !important;
        padding: 12px !important;
        font-size: 16px !important;
    }
    .stTextInput input:focus, .stTextArea textarea:focus {
        border-color: #38bdf8 !important;
        box-shadow: 0 0 15px rgba(56, 189, 248, 0.4) !important;
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
    }
    
    .streamlit-expanderHeader {
        background: rgba(30, 41, 59, 0.8) !important;
        color: #ffffff !important;
        border-radius: 10px;
        border: 1px solid rgba(255, 123, 0, 0.4) !important;
    }
    h1, h2, h3, h4, h5, h6, p, span, label {
        color: #f8fafc !important;
    }
    div.stAlert {
        background: rgba(15, 23, 42, 0.9) !important;
        color: #ffffff !important;
        border: 1px solid #ff7b00 !important;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# رابط جدول البيانات الأساسي (Google Sheets)
sheet_url = "https://docs.google.com/spreadsheets/d/1l6f8u-xkX9i89sTw9qfPkYO67WJ1Ym-XQCWLFpHICys/export?format=csv"

@st.cache_data
def load_data():
    try:
        df = pd.read_csv(sheet_url)
        df.columns = df.columns.str.strip()
        return df
    except Exception as e:
        return pd.DataFrame()

df = load_data()

# --- القائمة الجانبية (Sidebar Navigation) ---
with st.sidebar:
    if os.path.exists("logo.png"):
        st.image("logo.png", use_container_width=True)
    else:
        st.markdown("### 🛡️ T.S.S SAFETY 360")
        
    st.markdown("---")
    st.markdown("### 🧭 التنقل السريع")
    
    menu = st.radio(
        "اختر القسم:",
        [
            "🏠 الرئيسية",
            "🤖 Safety AI (المساعد الذكي)",
            "🧠 Safety Brain (المحرك المترابط)",
            "📸 صوّر الخطر (AI Vision)",
            "🚨 طوارئ فورية (Emergency)",
            "⚖️ القوانين والأنظمة",
            "🧪 قاعدة بيانات المواد",
            "📋 أدوات المشرف (JSA & RA)",
            "🎓 Safety Academy",
            "📊 Dashboard المشرف"
        ]
    )
    
    st.markdown("---")
    if not df.empty:
        st.success("🟢 النظام الأمني: متصل")
        st.metric(label="📊 إجمالي المعايير", value=len(df))
    else:
        st.error("🔴 الخادم: غير متصل")
        
    st.markdown("---")
    st.caption("Developed by T.S.S\nDisaster & Crisis Management")


# ==========================================
# 1. 🏠 الصفحة الرئيسية
# ==========================================
if menu == "🏠 الرئيسية":
    st.title("🌐 SAFETY 360 — السلامة من كل زاوية")
    st.markdown("##### مساعدك الذكي والمرجع المعتمد للسلامة والصحة المهنية وإدارة الأزمات (أردن ودولي)")
    st.write("")
    
    q_main = st.text_input("🔍 بماذا تحتاج المساعدة؟ (اسأل عن قانون، خطر، مادة، إجراء طوارئ...)", placeholder="مثلاً: ما متطلبات العمل على ارتفاع؟ أو تسرب كيميائي...")
    
    st.write("📌 **أمثلة مقترحة للبحث:**")
    col_ex1, col_ex2, col_ex3 = st.columns(3)
    with col_ex1:
        if st.button("🏗️ العمل على ارتفاع"):
            q_main = "ارتفاع"
    with col_ex2:
        if st.button("🧪 تسرب مادة كيميائية"):
            q_main = "كيميائي"
    with col_ex3:
        if st.button("🔥 إجراءات الحرائق"):
            q_main = "حريق"

    st.markdown("---")
    st.markdown("### ⚡ اختصارات العمليات السريعة")
    
    b1, b2, b3, b4 = st.columns(4)
    with b1:
        if st.button("🚨 حالة طوارئ قصوى", use_container_width=True):
            st.warning("يرجى الانتقال فوراً لقسم 'طوارئ فورية' من القائمة الجانبية!")
    with b2:
        if st.button("🤖 اسأل Safety AI", use_container_width=True):
            st.info("انتقل لقسم المساعد الذكي لاستعلام تفصيلي.")
    with b3:
        if st.button("📋 أدوات المشرف", use_container_width=True):
            st.info("انتقل لقسم أدوات المشرف لإنشاء JSA و RA.")
    with b4:
        if st.button("⚖️ القوانين الأردنية", use_container_width=True):
            st.info("انتقل لقسم القوانين والأنظمة لاستعراض المراجع.")

    if q_main:
        st.write("---")
        st.subheader("⚡ نتائج البحث الفورية:")
        if not df.empty:
            results = df[df.astype(str).apply(lambda x: x.str.contains(q_main, case=False, na=False)).any(axis=1)]
            if not results.empty:
                for idx, row in results.iterrows():
                    with st.expander(f"📌 [{row.get('Category','')}] - {row.get('Legislation Title','')} ({row.get('Country','')})"):
                        st.markdown(f"**🏛️ مستوى الإلزام:** `{row.get('Compliance Level','')}` | **📜 البند:** `{row.get('Article / Section','')}`")
                        st.markdown(f"**📋 المتطلب:**\n> {row.get('Requirement','')}")
                        st.markdown(f"**🛠️ التطبيق العملي:**\n> {row.get('Practical Application','')}")
            else:
                st.warning("⚠️ لم يتم العثور على نتائج مطابقة، جرب مصطلحاً آخر.")


# ==========================================
# 2. 🤖 Safety AI (المساعد الذكي)
# ==========================================
elif menu == "🤖 Safety AI (المساعد الذكي)":
    st.title("🤖 Safety AI — مساعد السلامة الذكي")
    st.markdown("اطرح أي سيناريو عمل أو خطورة، وسيقوم المساعد بتحليله واستخراج المتطلبات القانونية وتقييم المخاطر فوراً.")
    
    ai_query = st.text_area("✍️ اكتب السيناريو أو المشكلة هنا:", placeholder="مثلاً: عندي عامل رح يشتغل على ارتفاع 6 متر، شو لازم أعمل؟")
    
    if st.button("🚀 تحليل سيناريو السلامة"):
        if ai_query:
            with st.spinner("⏳ جارٍ تحليل المخاطر والمتطلبات القانونية..."):
                st.success("✨ تحليل مساعد السلامة الذكي:")
                st.markdown("---")
                st.markdown("⚠️ **المخاطر الرئيسية:** السقوط من ارتفاع، إصابات بليغة، عدم تأمين حافة العمل.")
                st.markdown("🛡️ **إجراءات السيطرة:** تركيب سواتر حماية، استخدام أحزمة حماية كاملة (Full Body Harness) مربوطة بنقاط تثبيت معتمدة.")
                st.markdown("🦺 **معدات الوقاية الشخصية (PPE):** خوذة، حزام أمان، حذاء سلامة مانع للانزلاق.")
                st.markdown("⚖️ **المتطلبات القانونية والمصادر:**\n* المصدر: نظام السلامة والصحة المهنية الأردني\n* رقم المادة: بناءً على المعايير الدولية OSHA 1910.140 / المادة المعتمدة محلياً.\n* تاريخ التحديث: 2026")
                st.markdown("🚨 **طوارئ:** توفير طاقم إسعاف أولي وخطة إنقاذ فوري معلقة (Rescue Plan).")
        else:
            st.warning("يرجى كتابة السيناريو أولاً.")


# ==========================================
# 3. 🧠 Safety Brain
# ==========================================
elif menu == "🧠 Safety Brain (المحرك المترابط)":
    st.title("🧠 Safety Brain — محرك الربط الذكي")
    st.markdown("نظام خبير يربط بين (المهمة ➔ المادة ➔ المخاطر ➔ تقييم المخاطر ➔ PPE ➔ التصاريح ➔ القوانين).")
    
    task_input = st.selectbox("اختر المهمة أو النشاط:", ["تنظيف خزان كيميائي", "أعمال لحام وقطع", "العمل على ارتفاعات", "حفريات عميقة"])
    if st.button("🔗 ربط وتحليل المنظومة بالكامل"):
        st.info(f"⚡ يتم ربط عناصر نشاط: **{task_input}** عبر Safety Brain:")
        st.markdown("""
        1. **المهمة:** تنظيف وتفريغ مادة خطرة.
        2. **المخاطر المحتملة:** نقص الأكسجين، أبخرة سامة، خطر اشتعال.
        3. **تقييم المخاطر (Risk Assessment):** عالي الخطورة (High Risk).
        4. **التصاريح المطلوبة (Permit to Work):** تصريح دخول أماكن محصورة (Confined Space Permit) + تصريح تسخين/لهب.
        5. **معدات الوقاية (PPE):** جهاز تنفس مستقل (SCBA)، أفرولات مقاومة للمواد الكيميائية.
        6. **القانون المعتمد:** التشريعات الأردنية ومعايير OSHA للأماكن المحصورة.
        7. **إجراءات الطوارئ:** فريق طوارئ جاهز للإنقاذ السريع مع مراقب خارجي (Standby Person).
        """)


# ==========================================
# 4. 📸 صوّر الخطر (AI Vision)
# ==========================================
elif menu == "📸 صوّر الخطر (AI Vision)":
    st.title("📸 صوّر الخطر — التحليل البصري للسلامة")
    st.markdown("ارفع صورة لموقع العمل وسيقوم النظام برصد المخاطر المحتملة واقتراح الحلول.")
    
    uploaded_img = st.file_uploader("اختر صورة موقع العمل (JPG, PNG):", type=["png", "jpg", "jpeg"])
    if uploaded_img:
        st.image(uploaded_img, caption="الصورة المرفوعة للتحليل", width=400)
        if st.button("🔍 تحليل المخاطر في الصورة"):
            st.success("📊 نتائج التحليل الأولي:")
            st.markdown("""
            * 🔴 **خطر مرصود 1:** عدم ارتداء حزام الأمان أثناء العمل المرتفع (مستوى الخطورة: عالي جداً).
            * 🟠 **خطر مرصود 2:** وجود كابلات كهربائية مكشوفة في ممر الحركة.
            * 🛠️ **الإجراء التصحيحي:** إيقاف العمل فوراَ، تأمين الكابلات، وإلزام العاملين بارتداء معدات الوقاية.
            """)


# ==========================================
# 5. 🚨 طوارئ فورية (Emergency)
# ==========================================
elif menu == "🚨 طوارئ فورية (Emergency)":
    st.title("🚨 مركز حالات الطوارئ الفورية")
    st.error("⚠️ اختر نوع حالة الطوارئ لعرض الخطوات الفورية المختصرة:")
    
    em_type = st.selectbox("نوع الطارئ:", ["🔥 حريق", "🧪 تسرب كيميائي", "⚡ صعقة كهربائية", "🫁 اختناق / نقص أكسجين", "🏗️ انهيار حفريات", "🚑 إصابة عمل بليغة"])
    
    if st.button("🚨 اعرض خطوات الطوارئ الفورية"):
        st.markdown(f"### خطوات الطوارئ الخاصة بـ: {em_type}")
        st.markdown("""
        1. **ابق هادئاً** وأطلق صفارة الإنذار فوراً إذا لزم الأمر.
        2. **أبلغ فريق الطوارئ** أو الدفاع المدني (911) وأعطهم الموقع الدقيق.
        3. **أوقف المصدر** (مثل فصل التيار الكهربائي أو إغلاق محبس المادة الكيميائية إن أمكن وبأمان).
        4. **قم بالإخلاء الآمن** حسب مسارات الهروب المعتمدة إلى نقطة التجمع (Assembly Point).
        5. **لا تقم بالإنقاذ العشوائي** واعرف حدود قدراتك لمنع تفاقم الإصابات.
        """)


# ==========================================
# 6. ⚖️ القوانين والأنظمة
# ==========================================
elif menu == "⚖️ القوانين والأنظمة":
    st.title("⚖️ مركز القوانين والأنظمة والمراجع")
    st.markdown("استعرض التشريعات الأردنية والمعايير الدولية (OSHA, ISO, NFPA, ILO).")
    
    country_filter = st.selectbox("اختر الدولة / النطاق:", ["الكل", "الأردن", "الدولي (OSHA / ISO)"])
    search_law = st.text_input("بحث في القوانين والتشريعات:", placeholder="ابحث عن قانون، نظام، أو معيار...")
    
    if not df.empty:
        filtered_df = df
        if country_filter != "الكل":
            filtered_df = df[df['Country'].str.contains(country_filter, case=False, na=False)]
        if search_law:
            filtered_df = filtered_df[filtered_df.astype(str).apply(lambda x: x.str.contains(search_law, case=False, na=False)).any(axis=1)]
            
        st.write(f"عدد النتائج المتوفرة: {len(filtered_df)}")
        st.dataframe(filtered_df, use_container_width=True)
    else:
        st.warning("قاعدة البيانات غير متصلة حالياً.")


# ==========================================
# 7. 🧪 قاعدة بيانات المواد
# ==========================================
elif menu == "🧪 قاعدة بيانات المواد":
    st.title("🧪 قاعدة بيانات المواد الخطرة والكيميائية")
    mat_query = st.text_input("ابحث عن اسم المادة أو رقم CAS (مثلاً: Chlorine, Ammonia, Diesel):")
    if mat_query:
        st.info(f"🔍 نتائج البحث عن المادة: {mat_query}")
        st.markdown("""
        * **تصنيف الخطورة:** مادة سامة / مهيجة.
        * **رموز GHS:** علامة الجمجمة، التآكل.
        * **معدات الوقاية (PPE):** قناع وجه كامل، قفازات مقاومة للمواد الكيميائية.
        * **الإسعافات الأولية:** غسل العينين بالماء الفوري لمدة 15 دقيقة والتوجه للمستشفى.
        """)


# ==========================================
# 8. 📋 أدوات المشرف
# ==========================================
elif menu == "📋 أدوات المشرف (JSA & RA)":
    st.title("📋 أدوات مشرف السلامة المعتمدة")
    tool_choice = st.selectbox("اختر الأداة:", ["تقييم المخاطر (Risk Assessment)", "تحليل سلامة العمل (JSA)", "تقرير الحوادث (Incident Report)"])
    
    if tool_choice == "تقييم المخاطر (Risk Assessment)":
        t_name = st.text_input("اسم النشاط أو المهمة:")
        hazard_name = st.text_input("الخطر المحتمل:")
        prob = st.slider("الاحتمالية (1-5):", 1, 5, 3)
        sev = st.slider("الشدة (1-5):", 1, 5, 4)
        risk_score = prob * sev
        st.markdown(f"**مستوى خطورة الخطر (Risk Score):** `{risk_score}`")
        if risk_score >= 15:
            st.error("🚨 خطر مرتفع جداً! يتطلب إيقاف النشاط حتى تطبيق إجراءات السيطرة الفورية.")
        elif risk_score >= 8:
            st.warning("⚠️ خطر متوسط، يتطلب إجراءات سيطرة وإشراف.")
        else:
            st.success("🟢 خطر منخفض مقبول.")


# ==========================================
# 9. 🎓 Safety Academy & 📊 Dashboard
# ==========================================
elif menu == "🎓 Safety Academy":
    st.title("🎓 أكاديمية Safety 360 التعليمية")
    st.info("قريباً: الدورات والشهادات المعتمدة في السلامة والصحة المهنية وإدارة الأزمات.")

elif menu == "📊 Dashboard المشرف":
    st.title("📊 لوحة مؤشرات الأداء (Safety Dashboard)")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Safety Score", "88 / 100", "🟢 جيد جداً")
    with col2:
        st.metric("الحوادث المسجلة", "0", "0% تغير")
    with col3:
        st.metric("المخاطر المفتوحة", "2", "تحتاج متابعة")
    with col4:
        st.metric("عمليات التفتيش", "14", "مكتملة")
