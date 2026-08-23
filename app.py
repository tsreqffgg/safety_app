import streamlit as st
import pandas as pd

# إعدادات الصفحة وتصميم الواجهة الواسع
st.set_page_config(
    page_title="منصة خبراء السلامة الذكية | TSS", 
    page_icon="🛡️", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# تخصيص تصميم CSS متطور جداً مع حركات وتأثيرات بصرية فخمة
st.markdown("""
    <style>
    /* خلفية النظام الكحلية العميقة المتدرجة */
    .stApp {
        background: linear-gradient(135deg, #050b14 0%, #0b132b 50%, #1c2541 100%) !important;
    }
    
    /* القائمة الجانبية بتصميم تكنولوجي فخم */
    section[data-testid="stSidebar"] {
        background-color: #080f1d !important;
        border-right: 1px solid rgba(255, 123, 0, 0.2);
    }
    section[data-testid="stSidebar"] * {
        color: #ffffff !important;
    }
    
    /* تأثير نبض وتوهج للشعار أو العناوين */
    @keyframes pulseGlow {
        0% { box-shadow: 0 0 5px rgba(255, 123, 0, 0.2); }
        50% { box-shadow: 0 0 20px rgba(255, 123, 0, 0.6); }
        100% { box-shadow: 0 0 5px rgba(255, 123, 0, 0.2); }
    }
    
    /* تنسيق خانة البحث مع حركات عند التفاعل */
    .stTextInput > div > div > input {
        background-color: #0b132b !important;
        color: #ffffff !important;
        border-radius: 12px;
        border: 2px solid #ff7b00;
        padding: 12px;
        font-size: 16px;
        transition: all 0.3s ease;
    }
    .stTextInput > div > div > input:focus {
        border-color: #ff9f1c;
        box-shadow: 0 0 15px rgba(255, 123, 0, 0.5);
    }
    
    /* حركة ظهور سلسة للعناصر (Fade In) */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .element-container, .stExpander {
        animation: fadeIn 0.5s ease-out forwards;
    }
    
    /* تنسيق العناوين والخطوط */
    h1, h2, h3, h4, h5, h6, p, span, label {
        color: #ffffff !important;
    }
    
    /* تنسيق صناديق النتائج (Expanders) بمظهر زجاجي عصري */
    .streamlit-expanderHeader {
        background-color: #111d32 !important;
        color: #ffffff !important;
        border-radius: 10px;
        border: 1px solid rgba(255, 123, 0, 0.4) !important;
        transition: all 0.3s ease;
    }
    .streamlit-expanderHeader:hover {
        border-color: #ff7b00 !important;
        background-color: #1c2541 !important;
    }
    
    /* تخصيص التحذيرات والتنبيهات */
    div.stAlert {
        background-color: #111d32 !important;
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

# --- القائمة الجانبية مع شعارك الرسمي TSS ---
with st.sidebar:
    st.image("logo.png", use_container_width=True)
    st.markdown("---")
    st.markdown("### ⚡ لوحة العمليات")
    st.info("💡 **عن المنصة:**\nنظام القيادة والتحكم الذكي للتشريعات الأردنية ومعايير السلامة الدولية (OSHA, ISO, NFPA).")
    
    if not df.empty:
        st.success(f"🟢 حالة النظام: متصل بالخادم الأمني")
        st.metric(label="إجمالي التشريعات المتاحة", value=len(df))
    else:
        st.error("🔴 تنبيه: جاري إعادة الاتصال...")
        
    st.markdown("---")
    st.caption("Developed by T.S.S | Disaster & Crisis Management")

# --- الواجهة الرئيسية بتصميم تفاعلي ---
st.title("🛡️ منصة خبراء السلامة والصحة المهنية الذكية")
st.markdown("##### 🌐 نظام البحث الفوري والتحليل التكتيكي للسلامة وإدارة الأزمات (أردن ودولي)")
st.write("")

# نافذة البحث الرئيسية بتصميم تكنولوجي متطور
user_query = st.text_input("🔍 ابحث عن أي تشريع، خطر، صيف، طوارئ، حفريات، كيميائي، أو إجراء سلامة:", placeholder="أدخل كلمة المفتاح للبحث السريع (مثلاً: ارتفاع، حريق، طوارئ)...")

if user_query:
    with st.spinner("⚡ جارٍ معالجة البيانات واستخراج النتائج التكتيكية..."):
        if not df.empty:
            results = df[df.astype(str).apply(lambda x: x.str.contains(user_query, case=False, na=False)).any(axis=1)]
            
            if not results.empty:
                st.success(f"🎯 تم رصد ({len(results)}) تطابق مباشر في قاعدة المعرفة:")
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
                st.warning("⚠️ لم يتم العثور على نتائج مطابقة، جرب استخدام كلمات مفتاحية أخرى (مثل: صيف، طوارئ، ارتفاع، حريق).")
        else:
            st.error("⚠️ خطأ في الاتصال بقاعدة البيانات، يرجى مراجعة الرابط.")
else:
    st.info("👈 نظام الاستعلام جاهز. ابدأ بكتابة أي مصطلح هندسي أو أمني في حقل البحث بالأعلى لاستعراض النتائج فوراً.")
