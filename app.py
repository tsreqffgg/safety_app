import streamlit as st
import pandas as pd

# إعدادات الصفحة وتصميم الواجهة الواسع
st.set_page_config(
    page_title="SAFETY 360 | TSS", 
    page_icon="🛡️", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# تخصيص التصميم بالهوية البصرية (خلفية كحلي كاملة مع عناصر برتقالية وبيضاء)
st.markdown("""
    <style>
    /* خلفية الموقع باللون الكحلي الداكن الفخم */
    .stApp {
        background-color: #0b132b !important;
    }
    
    /* القائمة الجانبية */
    section[data-testid="stSidebar"] {
        background-color: #1c2541 !important;
    }
    section[data-testid="stSidebar"] * {
        color: #ffffff !important;
    }
    
    /* لون النصوص العامة باللون الأبيض لتباين واضح مع الكحلي */
    h1, h2, h3, h4, h5, h6, p, span, label {
        color: #ffffff !important;
    }
    
    /* تنسيق خانة البحث بحدود برتقالية بارزة وخلفية كحلية */
    .stTextInput > div > div > input {
        background-color: #1c2541 !important;
        color: #ffffff !important;
        border-radius: 10px;
        border: 2px solid #ff7b00;
        padding: 10px;
    }
    
    /* تنسيق مربعات النتائج (Expanders) لتتوافق مع الهوية الكحلي والبرتقالي */
    .streamlit-expanderHeader {
        background-color: #1c2541 !important;
        color: #ffffff !important;
        border-radius: 8px;
        border: 1px solid #ff7b00 !important;
    }
    
    /* تنسيق الصناديق والتحذيرات */
    div.stAlert {
        background-color: #1c2541 !important;
        color: #ffffff !important;
        border: 1px solid #ff7b00 !important;
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
    st.title("لوحة التحكم")
    st.info("💡 **عن المنصة:**\nمساعدك المعتمد للبحث الفوري في التشريعات الأردنية ومعايير السلامة الدولية (OSHA, ISO, NFPA).")
    
    if not df.empty:
        st.success(f"🟢 حالة النظام: متصل بقاعدة المعرفة")
        st.metric(label="إجمالي التشريعات والمعايير", value=len(df))
    else:
        st.error("🔴 تنبيه: قاعدة البيانات غير متصلة")
        
    st.markdown("---")
    st.caption("تم تطوير المنصة خصيصاً لخبراء ومشرفي السلامة والصحة المهنية وإدارة الأزمات.")

# --- الواجهة الرئيسية ---
st.title("🛡️ منصة خبراء السلامة والصحة المهنية الذكية")
st.markdown("##### مرجعك الفوري والقانوني المعتمد للسلامة المهنية وإدارة الأزمات (أردن ودولي)")
st.write("")

# نافذة البحث الرئيسية
user_query = st.text_input("🔍 ابحث عن أي تشريع، خطر، صيف، طوارئ، حفريات، كيميائي، أو إجراء سلامة:", placeholder="اكتب كلمة البحث هنا (مثلاً: ارتفاع، حريق، LOTO)...")

if user_query:
    with st.spinner("⏳ جارٍ البحث في قاعدة المعرفة المعتمدة..."):
        if not df.empty:
            results = df[df.astype(str).apply(lambda x: x.str.contains(user_query, case=False, na=False)).any(axis=1)]
            
            if not results.empty:
                st.success(f"✨ تم العثور على ({len(results)}) نتيجة مطابقة لبحثك:")
                st.write("")
                
                for index, row in results.iterrows():
                    cat = row.get('Category', '')
                    country = row.get('Country', '')
                    comp_level = row.get('Compliance Level', '')
                    title = row.get('Legislation Title', 'مرجع قانوني')
                    article = row.get('Article / Section', '')
                    requirement = row.get('Requirement', '')
                    app = row.get('Practical Application', '')
                    
                    with st.expander(f"📌 [{cat}] - {title} ({country})"):
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
                st.warning("⚠️ لم يتم العثور على مطابقة دقيقة، جرب كلمات أخرى مثل: (صيف، طوارئ، ارتفاع، حريق، كهرباء).")
        else:
            st.error("⚠️ تعذر قراءة جدول البيانات، يرجى التأكد من أن الرابط عام وقابل للقراءة.")
else:
    st.info("👈 ابدأ بكتابة كلمة مفتاحية في خانة البحث بالأعلى لعرض المعايير والتشريعات المطلوبة فوراً.")
