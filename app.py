import streamlit as st
import pandas as pd

# إعدادات الصفحة وتصميم الواجهة الواسع
st.set_page_config(
    page_title="SAFETY 360 | قيادة السلامة وإدارة الأزمات", 
    page_icon="🛡️", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# تخصيص التصميم المتطور (Cyber-Glassmorphism مع توهجات نيون)
st.markdown("""
    <style>
    /* إخفاء خلفية Streamlit الأصلية */
    .stApp {
        background: transparent !important;
    }
    
    /* خلفية شبكية نيون متحركة ببطء */
    body {
        background-color: #030712;
        background-image: 
            linear-gradient(rgba(255, 123, 0, 0.04) 1px, transparent 1px),
            linear-gradient(90deg, rgba(255, 123, 0, 0.04) 1px, transparent 1px);
        background-size: 50px 50px;
        animation: gridMove 25s linear infinite;
    }

    @keyframes gridMove {
        0% { background-position: 0 0; }
        100% { background-position: 50px 50px; }
    }
    
    /* القائمة الجانبية بتصميم تكتيكي معتم وزجاجي */
    section[data-testid="stSidebar"] {
        background-color: rgba(6, 11, 22, 0.95) !important;
        border-right: 1px solid rgba(255, 123, 0, 0.3);
    }
    section[data-testid="stSidebar"] * {
        color: #ffffff !important;
    }
    
    /* خانة البحث: خلفية كحلي داكن، كتابة بيضاء ناصحة، وتوهج برتقالي سايبر */
    .stTextInput > div > div > input {
        background-color: rgba(11, 19, 43, 0.95) !important;
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
        border-radius: 14px;
        border: 2px solid #ff7b00;
        padding: 16px;
        font-size: 16px;
        box-shadow: 0 0 20px rgba(255, 123, 0, 0.25);
        transition: all 0.4s ease;
    }
    .stTextInput > div > div > input:focus {
        border-color: #00ffff;
        box-shadow: 0 0 30px rgba(0, 255, 255, 0.5);
    }
    
    /* تنسيق العنوان الرئيسي بنبض تكتيكي */
    .main-title {
        font-size: 2.3rem;
        font-weight: 800;
        color: #ffffff;
        text-shadow: 0 0 20px rgba(255, 123, 0, 0.5);
        margin-bottom: 0px;
    }
    
    /* حركة ظهور العناصر بشكل ناعم وسلس */
    @keyframes tacticalFade {
        from { opacity: 0; transform: translateY(15px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .element-container, .stExpander {
        animation: tacticalFade 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }
    
    /* صندوق النتائج بتصميم زجاجي عالي التقنية */
    .streamlit-expanderHeader {
        background: rgba(15, 23, 42, 0.85) !important;
        color: #ffffff !important;
        border-radius: 12px;
        border: 1px solid rgba(255, 123, 0, 0.35) !important;
        transition: all 0.3s ease;
    }
    .streamlit-expanderHeader:hover {
        border-color: #00ffff !important;
        box-shadow: 0 0 20px rgba(0, 255, 255, 0.3);
        background: rgba(22, 33, 62, 0.95) !important;
    }
    
    /* تنسيق النصوص العامة */
    p, span, label, h3, h4, h5 {
        color: #e2e8f0 !important;
    }
    
    /* تنبيهات النظام */
    div.stAlert {
        background: rgba(11, 19, 43, 0.9) !important;
        color: #ffffff !important;
        border: 1px solid #ff7b00 !important;
        border-radius: 12px;
    }
    </style>
""", unsafe_allow_html=True)

# رابط جدول البيانات الخاص بك بصيغة التصدير المباشر
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

# --- القائمة الجانبية لمنصة SAFETY 360 ---
with st.sidebar:
    st.image("logo.png", use_container_width=True)
    st.markdown("---")
    st.markdown("### 🌐 نظام القيادة 360")
    st.info("💡 **عن المنصة:**\nمحطة القيادة الذكية للتشريعات الأردنية ومعايير السلامة الدولية (OSHA, ISO, NFPA).")
    
    if not df.empty:
        st.success(f"🟢 الخادم الأمني: متصل")
        st.metric(label="📊 إجمالي المعايير", value=len(df))
    else:
        st.error("🔴 الخادم: جاري إعادة الاتصال...")
        
    st.markdown("---")
    st.caption("Designed & Developed by T.S.S\nDisaster & Crisis Management")

# --- الواجهة الرئيسية بتصميم SAFETY 360 المطور ---
st.markdown('<p class="main-title">🌐 SAFETY 360 — منصة السلامة وإدارة الأزمات الذكية</p>', unsafe_allow_html=True)
st.markdown("##### 🛡️ محطة القيادة والتحكم التكتيكية لاستعراض التشريعات وتحليل المخاطر (أردن ودولي)")
st.write("")

# نافذة البحث الرئيسية (كتابة بيضاء ناصحة وتوهج سيبراني)
user_query = st.text_input("🔍 رادار البحث الفوري (ابحث عن أي تشريع، خطر، صيف، طوارئ، كيميائي، حفريات):", placeholder="أدخل مصطلح البحث هنا (مثلاً: ارتفاع، حريق، طوارئ، LOTO)...")

if user_query:
    with st.spinner("⚡ جاري مسح قاعدة البيانات واستخراج النتائج التكتيكية..."):
        if not df.empty:
            results = df[df.astype(str).apply(lambda x: x.str.contains(user_query, case=False, na=False)).any(axis=1)]
            
            if not results.empty:
                st.success(f"🎯 تم رصد ({len(results)}) مطابقة دقيقة في منظومة SAFETY 360:")
                st.write("")
                
                for index, row in results.iterrows():
                    cat = row.get('Category', '')
                    country = row.get('Country', '')
                    comp_level = row.get('Compliance Level', '')
                    title = row.get('Legislation Title', 'مرجع قانوني')
                    article = row.get('Article / Section', '')
                    requirement = row.get('Requirement', '')
                    app = row.get('Practical Application', '')
                    
                    with st.expander(f"📌 [{cat}] — {title} ({country})"):
                        col1, col2 = st.columns(2)
                        with col1:
                            st.markdown(f"**🏛️ مستوى الإلزام:** `{comp_level}`")
                            st.markdown(f"**📜 المادة / البند:** `{article}`")
                        with col2:
                            st.markdown(f"**🌍 النطاق / الدولة:** `{country}`")
                            
                        st.markdown("---")
                        st.markdown(f"**📋 المتطلب القانوني:**\n> {requirement}")
                        st.markdown(f"**🛠️ التطبيق العملي لمشرف السلامة:**\n> {app}")
            else:
                st.warning("⚠️ لم يتم رصد نتائج مطابقة، جرب كلمات بحث أخرى (مثل: صيف، طوارئ، حريق، ارتفاع).")
        else:
            st.error("⚠️ خطأ في الاتصال بقاعدة البيانات، يرجى مراجعة الرابط.")
else:
    st.info("👈 نظام SAFETY 360 في وضع الاستعداد. أدخل أي مصطلح بحثي في الأعلى لاستعراض البيانات وتحليلها فوراً.")
