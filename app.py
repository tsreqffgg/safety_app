import streamlit as st
import pandas as pd

# إعدادات الصفحة
st.set_page_config(page_title="منصة خبراء السلامة الذكية", page_icon="🛡️", layout="wide")

st.title("🛡️ منصة خبراء السلامة الذكية (MVP)")
st.write("مساعدك القانوني والفني المعتمد للسلامة والصحة المهنية (أردن ودولي)")

# رابط جدول البيانات (Google Sheets) المؤقت أو الافتراضي
# سنقوم لاحقاً بربطه بالجدول الذي أنشأته
sheet_url = "https://docs.google.com/spreadsheets/d/1l6f8u-xkX9i89sTw9qfPkYO67WJ1Ym-XQCWLFpHICys/edit?usp=sharing" # رابط تجريبي

@st.cache_data
def load_data():
    try:
        csv_url = sheet_url.replace("/edit?usp=sharing", "/export?format=csv").replace("/edit", "/export?format=csv")
        df = pd.read_csv(csv_url)
        return df
    except:
        return pd.DataFrame()

df = load_data()

# نافذة البحث والدردشة مع المشرف
user_query = st.text_input("🔍 ابحث عن أي تشريع، خطر، أو إجراء سلامة (مثلاً: العمل على ارتفاع، طفايات الحريق، GHS):")

if user_query:
    st.info("جارٍ البحث في قاعدة المعرفة المعتمدة...")
    
    if not df.empty:
        # بحث مبدئي بسيط داخل البيانات
        results = df[df.astype(str).apply(lambda x: x.str.contains(user_query, case=False)).any(axis=1)]
        
        if not results.empty:
            st.success(f"✔ تم العثور على {len.results if 'len' in locals() else len(results)} نتيجة مطابقة:") if False else st.success(f"✔ تم العثور على نتائج مطابقة لبحثك:")
            for index, row in results.iterrows():
                with st.expander(f"📌 {row.get('Legislation Title', 'مرجع قانوني')} ({row.get('Category', '')})"):
                    st.write(f"**الدولة / النطاق:** {row.get('Country', '')}")
                    st.write(f"**مستوى الإلزام:** {row.get('Compliance Level', '')}")
                    st.write(f"**المادة / البند:** {row.get('Article / Section', '')}")
                    st.write(f"**المتطلب القانوني:** {row.get('Requirement', '')}")
                    st.markdown(f"**🛠️ التطبيق العملي لمشرف السلامة:**\n{row.get('Practical Application', '')}")
        else:
            st.warning("⚠️ لم يتم العثور على مطابقة حرفية، يرجى تجربة كلمات بحث أخرى (مثل: كيميائي، حرائق، أردن).")
    else:
        st.error("⚠️ يرجى ربط جدول بيانات Google Sheets الصحيح لعرض النتائج.")
