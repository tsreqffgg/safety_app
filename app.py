import streamlit as st
import pandas as pd

# إعدادات الصفحة وتصميم الواجهة الواسع
st.set_page_config(
    page_title="منصة خبراء السلامة الذكية", 
    page_icon="🛡️", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# تخصيص التصميم عبر CSS لإعطاء مظهر عصري واحترافي
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stTextInput > div > div > input {
        border-radius: 10px;
        border: 2px solid #0e6655;
        padding: 10px;
    }
    .metric-card {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        text-align: center;
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

# --- القائمة الجانبية المحدثة (Sidebar) ---
with st.sidebar:
    st.image("https://img.icons8.com/color/96/experimental-shield-secured-flat.png", width=80)
    st.title("لوحة التحكم")
    st.write("---")
    st.info("💡 **عن المنصة:**\nمساعدك المعتمد للبحث الفوري في التشريعات الأردنية ومعايير السلامة الدولية (OSHA, ISO, NFPA).")
    
    if not df.empty:
        st.success(f"🟢 حالة النظام: متصل بقاعدة المعرفة")
        st.metric(label="إجمالي التشريعات والمعايير", value=len(df))
    else:
        st.error("🔴 تنبيه: قاعدة البيانات غير متصلة")
        
    st.write("---")
    st.caption("تم تطوير المنصة خصيصاً لخبراء ومشرفي السلامة والصحة المهنية وإدارة الأزمات.")

# --- الواجهة الرئيسية ---
st.title("🛡️ منصة خبراء السلامة والصحة المهنية الذكية")
st.markdown("##### مرجعك الفوري والقانوني المعتمد للسلامة المهنية وإدارة الأزمات (أردن ودولي)")
st.write("")

# نافذة البحث الرئيسية بتصميم بارز
user_query = st.text_input("🔍 ابحث عن أي تشريع، خطر، صيف، طوارئ، حفريات، كيميائي، أو إجراء سلامة:", placeholder="اكتب كلمة البحث هنا (مثلاً: ارتفاع، حريق، LOTO)...")

if user_query:
    with st.spinner("⏳ جارٍ البحث في قاعدة المعرفة المعتمدة..."):
        if not df.empty:
            # بحث مرن داخل كافة الأعمدة
            results = df[df.astype(str).apply(lambda x: x.str.contains(user_query, case=False, na=False)).any(axis=1)]
            
            if not results.empty:
                st.success(f"✨ تم العثور على ({len.results if 'len.results' else len(results)}) نتيجة مطابقة لبحثك:")
                st.write("")
                
                for index, row in results.iterrows():
                    cat = row.get('Category', '')
                    country = row.get('Country', '')
                    comp_level = row.get('Compliance Level', '')
                    title = row.get('Legislation Title', 'مرجع قانوني')
                    article = row.get('Article / Section', '')
                    requirement = row.get('Requirement', '')
                    app = row.get('Practical Application', '')
                    
                    # عرض كل نتيجة داخل صندوق أنيق ومميز
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
    # شاشة ترحيبية عند عدم وجود بحث
    st.info("👈 ابدأ بكتابة كلمة مفتاحية في خانة البحث بالأعلى لعرض المعايير والتشريعات المطلوبة فوراً.")
    
    # عرض أقسام سريعة مقترحة
    st.write("### ⚡ مواضيع شائعة يمكنك البحث عنها:")
    cols = st.columns(4)
    with cols[0]:
        if st.button("🔥 السلامة من الحريق"):
            pass
    with cols[1]:
        if st.button("☀️ الإجهاد الحراري وصيفاً"):
            pass
    with cols[2]:
        if st.button("🚨 الطوارئ والأزمات"):
            pass
    with cols[3]:
        if st.button("🏗️ الإنشاءات والحفريات"):
            pass
