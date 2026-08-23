import streamlit as st
import pandas as pd

# إعدادات الصفحة وتصميم الواجهة الواسع
st.set_page_config(
    page_title="SAFETY 360 | قيادة السلامة وإدارة الأزمات", 
    page_icon="🌐", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# تخصيص التصميم مع خلفية متحركة وكتابة بيضاء صافية في البحث
st.markdown("""
    <style>
    /* خلفية متحركة بتدرجات رادارية عميقة (Animated Cyber Background) */
    .stApp {
        background: linear-gradient(270deg, #050b14, #0b132b, #1c2541, #080f1d);
        background-size: 800% 800%;
        animation: gradientAnimation 20s ease infinite;
    }
    
    @keyframes gradientAnimation {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* القائمة الجانبية بتصميم تكتيكي */
    section[data-testid="stSidebar"] {
        background-color: #070d1a !important;
        border-right: 1px solid rgba(255, 123, 0, 0.3);
    }
    section[data-testid="stSidebar"] * {
        color: #ffffff !important;
    }
    
    /* خانة البحث: خلفية كحلية، حدود برتقالية، والكتابة باللون الأبيض النقي */
    .stTextInput > div > div > input {
        background-color: #0b132b !important;
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
        border-radius: 12px;
        border: 2px solid #ff7b00;
        padding: 14px;
        font-size: 16px;
        box-shadow: 0 0 10px rgba(255, 123, 0, 0.2);
        transition: all 0.4s ease;
    }
    .stTextInput > div > div > input:focus {
        border-color: #ff9f1c;
        box-shadow: 0 0 20px rgba(255, 123, 0, 0.5);
    }
    
    /* حركة ظهور العناصر بشكل تكتيكي ناعم */
    @keyframes tacticalFade {
        from { opacity: 0; transform: translateY(15px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .element-container, .stExpander {
        animation: tacticalFade 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }
    
    /* تنسيق النصوص والعناوين */
    h1, h2, h3, h4, h5, h6, p, span, label {
        color: #e2e8f0 !important;
    }
    
    /* صندوق النتائج بتصميم زجاجي عالي التقنية */
    .streamlit-expanderHeader {
        background: rgba(17, 29, 50, 0.85) !important;
        color: #ffffff !important;
        border-radius: 10px;
        border: 1px solid rgba(255, 123, 0, 0.4) !important;
        transition: all 0.3s ease;
    }
    .streamlit-expanderHeader:hover {
        border-color: #ff7b00 !important;
        box-shadow: 0 0 15px rgba(255, 123, 0, 0.3);
        background: rgba(28, 37, 65, 0.95) !important;
    }
    
    /* تنبيهات النظام */
    div.stAlert {
        background: rgba(11, 19, 43, 0.9) !important;
        color: #ffffff !important;
        border: 1px solid #ff7b00 !important;
        border-radius: 10px;
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
    st.info("💡 **عن المنصة:**\nنظرة شاملة ومحطة استعلام فورية للتشريعات الأردنية ومعايير السلامة الدولية (OSHA, ISO, NFPA).")
    
    if not df.empty:
        st.success(f"🟢 الخادم الأمني: متصل بنجاح")
        st.metric(label="إجمالي المعايير والتشريعات", value=len(df))
    else:
        st.error("🔴 الخادم: جاري إعادة الاتصال...")
        
    st.markdown("---")
    st.caption("Designed & Developed by T.S.S\nDisaster & Crisis Management")

# --- الواجهة الرئيسيةSAFETY 360 ---
st.title("🌐 SAFETY 360 — منصة السلامة وإدارة الأزمات الذكية")
st.markdown("##### 🛡️ محطة القيادة والتحكم لاستعراض التشريعات وتحليل المخاطر (أردن ودولي)")
st.write("")

# نافذة البحث الرئيسية (مع كتابة بيضاء صافية)
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
