import streamlit as st
import pandas as pd
import os

# إعدادات الصفحة
st.set_page_config(
    page_title="SAFETY 360 | نظام القيادة والتحكم للسلامة", 
    page_icon="🛡️", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# تصميم نظيف وآمن يمنع تداخل الألوان
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
    .stTextInput input, .stTextArea textarea {
        background-color: #0b132b !important;
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
        border-radius: 12px !important;
        border: 2px solid #ff7b00 !important;
        padding: 12px !important;
        font-size: 16px !important;
    }
    h1, h2, h3, h4, h5, h6, p, span, label {
        color: #f8fafc !important;
    }
    </style>
""", unsafe_allow_html=True)

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

# --- القائمة الجانبية ---
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

# --- الصفحة الرئيسية ---
if menu == "🏠 الرئيسية":
    st.title("🌐 SAFETY 360 — السلامة من كل زاوية")
    st.markdown("##### مساعدك الذكي والمرجع المعتمد للسلامة والصحة المهنية وإدارة الأزمات (أردن ودولي)")
    st.write("")
    
    q_main = st.text_input("🔍 بماذا تحتاج المساعدة؟ (اسأل عن قانون، خطر، مادة، إجراء طوارئ...)", placeholder="مثلاً: ما متطلبات العمل على ارتفاع؟ أو تسرب كيميائي...")
    
    st.write("📌 **أمثلة مقترحة للبحث السريع:**")
    
    # استبدال الأزرار التقليدية بطريقة تضمن ظهور النصوص بوضوح تام على خلفية ملونة واضحة
    col_ex1, col_ex2, col_ex3 = st.columns(3)
    
    selected_quick_query = ""
    with col_ex1:
        if st.button("🏗️ العمل على ارتفاع", key="b_high"):
            selected_quick_query = "ارتفاع"
    with col_ex2:
        if st.button("🧪 تسرب مادة كيميائية", key="b_chem"):
            selected_quick_query = "كيميائي"
    with col_ex3:
        if st.button("🔥 إجراءات الحرائق", key="b_fire"):
            selected_quick_query = "حريق"

    if selected_quick_query:
        q_main = selected_quick_query

    st.markdown("---")
    st.markdown("### ⚡ اختصارات العمليات السريعة")
    
    b1, b2, b3, b4 = st.columns(4)
    with b1:
        if st.button("🚨 حالة طوارئ", key="cmd_emergency"):
            st.warning("انتقل لقسم 'طوارئ فورية' من القائمة الجانبية.")
    with b2:
        if st.button("🤖 Safety AI", key="cmd_ai"):
            st.info("انتقل لقسم المساعد الذكي.")
    with b3:
        if st.button("📋 أدوات المشرف", key="cmd_tools"):
            st.info("انتقل لقسم أدوات المشرف.")
    with b4:
        if st.button("⚖️ القوانين", key="cmd_laws"):
            st.info("انتقل لقسم القوانين والأنظمة.")

    # تنفيذ البحث
    active_query = q_main if q_main else selected_quick_query
    if active_query:
        st.write("---")
        st.subheader(f"⚡ نتائج البحث عن: ({active_query})")
        if not df.empty:
            results = df[df.astype(str).apply(lambda x: x.str.contains(active_query, case=False, na=False)).any(axis=1)]
            if not results.empty:
                for idx, row in results.iterrows():
                    with st.expander(f"📌 [{row.get('Category','')}] - {row.get('Legislation Title','')} ({row.get('Country','')})"):
                        st.markdown(f"**🏛️ مستوى الإلزام:** `{row.get('Compliance Level','')}` | **📜 البند:** `{row.get('Article / Section','')}`")
                        st.markdown(f"**📋 المتطلب:**\n> {row.get('Requirement','')}")
                        st.markdown(f"**🛠️ التطبيق العملي:**\n> {row.get('Practical Application','')}")
            else:
                st.warning("⚠️ لم يتم العثور على نتائج مطابقة.")

# باقي الأقسام تبقى كما هي تماماً...
elif menu == "🤖 Safety AI (المساعد الذكي)":
    st.title("🤖 Safety AI — مساعد السلامة الذكي")
    ai_query = st.text_area("✍️ اكتب السيناريو أو المشكلة هنا:", placeholder="مثلاً: عندي عامل رح يشتغل على ارتفاع 6 متر...")
    if st.button("🚀 تحليل سيناريو السلامة"):
        if ai_query:
            st.success("✨ تحليل مساعد السلامة الذكي:")
            st.markdown("⚠️ **المخاطر:** السقوط من ارتفاع، عدم تأمين حافة العمل.")
            st.markdown("🛡️ **إجراءات السيطرة:** تركيب سواتر واستخدام حزام أمان.")
        else:
            st.warning("يرجى كتابة السيناريو أولاً.")

elif menu == "🚨 طوارئ فورية (Emergency)":
    st.title("🚨 مركز حالات الطوارئ الفورية")
    st.error("⚠️ اختر نوع حالة الطوارئ لعرض الخطوات الفورية:")
    em_type = st.selectbox("نوع الطارئ:", ["🔥 حريق", "🧪 تسرب كيميائي", "⚡ صعقة كهربائية"])
    if st.button("🚨 اعرض الخطوات"):
        st.markdown(f"**خطوات الطوارئ لـ ({em_type}):**\n1. أطلق الإنذار فوراً.\n2. أبلغ الدفاع المدني.\n3. قم بالإخلاء الآمن.")

elif menu == "⚖️ القوانين والأنظمة":
    st.title("⚖️ مركز القوانين والأنظمة والمراجع")
    if not df.empty:
        st.dataframe(df, use_container_width=True)
    else:
        st.warning("قاعدة البيانات غير متصلة.")

elif menu == "📋 أدوات المشرف (JSA & RA)":
    st.title("📋 أدوات مشرف السلامة المعتمدة")
    prob = st.slider("الاحتمالية (1-5):", 1, 5, 3)
    sev = st.slider("الشدة (1-5):", 1, 5, 4)
    st.markdown(f"**مستوى خطورة الخطر:** `{prob * sev}`")
