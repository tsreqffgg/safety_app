import streamlit as st
import pandas as pd

# إعدادات الصفحة
st.set_page_config(page_title="منصة خبراء السلامة الذكية", page_icon="🛡️", layout="wide")

st.title("🛡️ منصة خبراء السلامة الذكية (MVP)")
st.write("مساعدك القانوني والفني المعتمد للسلامة والصحة المهنية (أردن ودولي)")

# رابط جدول البيانات الخاص بك بصيغة التصدير المباشر
https://docs.google.com/spreadsheets/d/1l6f8u-xkX9i89sTw9qfPkYO67WJ1Ym-XQCWLFpHICys/edit?usp=sharing

@st.cache_data
def load_data():
    try:
        df = pd.read_csv(sheet_url)
        return df
    except Exception as e:
        return pd.DataFrame()

df = load_data()

# نافذة البحث والدردشة مع المشرف
user_query = st.text_input("🔍 ابحث عن أي تشريع، خطر، أو إجراء سلامة (مثلاً: ارتفاع، حريق، GHS، غذائي):")

if user_query:
    st.info("جارٍ البحث في قاعدة المعرفة المعتمدة...")
    
    if not df.empty:
        # تنظيف وتعديل بيانات البحث لتجنب أخطاء الفراغات في الأعمدة
        df.columns = df.columns.str.strip()
        
        # بحث مرن داخل كافة الأعمدة
        results = df[df.astype(str).apply(lambda x: x.str.contains(user_query, case=False, na=False)).any(axis=1)]
        
        if not results.empty:
            st.success(f"✔ تم العثور على نتائج مطابقة لبحثك:")
            for index, row in results.iterrows():
                # جلب البيانات بحذر حسب أسماء الأعمدة في جدولك
                cat = row.get('Category', '')
                country = row.get('Country', '')
                comp_level = row.get('Compliance Level', '')
                title = row.get('Legislation Title', 'مرجع قانوني')
                article = row.get('Article / Section', '')
                requirement = row.get('Requirement', '')
                app = row.get('Practical Application', '')
                
                with st.expander(f"📌 {title} ({cat})"):
                    st.write(f"**الدولة / النطاق:** {country}")
                    st.write(f"**مستوى الإلزام:** {comp_level}")
                    st.write(f"**المادة / البند:** {article}")
                    st.write(f"**المتطلب القانوني:** {requirement}")
                    st.markdown(f"**🛠️ التطبيق العملي لمشرف السلامة:**\n{app}")
        else:
            st.warning("⚠️ لم يتم العثور على مطابقة، جرب كلمات أخرى مثل: (ارتفاع، حفريات، حريق، كيميائي).")
    else:
        st.error("⚠️ تعذر قراءة جدول البيانات، يرجى التأكد من أن الرابط عام وقابل للقراءة.")
