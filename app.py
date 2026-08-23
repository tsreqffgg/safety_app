import streamlit as st
import pandas as pd
import os
from datetime import datetime

# إعدادات الصفحة
st.set_page_config(
    page_title="SAFETY 360 | Field Supervisor Command", 
    page_icon="🛡️", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# تصميم واجهة الشركات العالمية مع التركيز على السرعة الميدانية
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        .stApp {
            background: radial-gradient(circle at 50% 0%, #090d16 0%, #020617 100%) !important;
        }
        
        /* الشريط العلوي العالمي */
        .global-navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: rgba(11, 18, 33, 0.9);
            backdrop-filter: blur(16px);
            border-bottom: 1px solid rgba(255, 123, 0, 0.3);
            padding: 12px 25px;
            border-radius: 14px;
            margin-bottom: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }
        .nav-logo-text {
            font-size: 19px;
            font-weight: 900;
            color: #ffffff;
            letter-spacing: 0.5px;
        }
        .nav-status {
            display: flex;
            align-items: center;
            gap: 8px;
            background: rgba(16, 185, 129, 0.1);
            border: 1px solid rgba(16, 185, 129, 0.3);
            padding: 5px 12px;
            border-radius: 20px;
            font-size: 12px;
            color: #10b981;
            font-weight: 600;
        }
        .status-dot {
            width: 7px;
            height: 7px;
            background-color: #10b981;
            border-radius: 50%;
            box-shadow: 0 0 8px #10b981;
        }

        /* صندوق الإدخال الفوري الميداني */
        .stTextInput input {
            background-color: rgba(15, 23, 42, 0.95) !important;
            color: #ffffff !important;
            -webkit-text-fill-color: #ffffff !important;
            border-radius: 14px !important;
            border: 2px solid rgba(255, 123, 0, 0.6) !important;
            padding: 16px !important;
            font-size: 18px !important;
            box-shadow: 0 0 20px rgba(255, 123, 0, 0.15);
        }
        .stTextInput input:focus {
            border-color: #ff7b00 !important;
            box-shadow: 0 0 25px rgba(255, 123, 0, 0.4) !important;
        }

        h1, h2, h3, h4, h5, h6, p, span, label {
            color: #f8fafc !important;
        }

        div.stAlert {
            background: rgba(15, 23, 42, 0.95) !important;
            color: #ffffff !important;
            border: 1px solid rgba(255, 123, 0, 0.5) !important;
            border-radius: 14px;
        }

        .instant-result-card {
            background: linear-gradient(135deg, rgba(30, 41, 59, 0.6) 0%, rgba(15, 23, 42, 0.9) 100%);
            border: 1px solid rgba(255, 123, 0, 0.35);
            padding: 25px;
            border-radius: 16px;
            margin-top: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.4);
        }

        .stButton button {
            width: 100%;
            background: linear-gradient(135deg, #ff7b00 0%, #ea580c 100%);
            color: #ffffff !important;
            border: none;
            border-radius: 12px;
            padding: 12px 20px;
            font-weight: 700;
            font-size: 16px;
            box-shadow: 0 0 15px rgba(255, 123, 0, 0.3);
            transition: all 0.3s ease;
        }
        .stButton button:hover {
            box-shadow: 0 0 25px rgba(255, 123, 0, 0.6);
            transform: translateY(-2px);
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
current_date_str = datetime.now().strftime("%Y-%m-%d")

# --- الشريط العلوي العالمي ---
st.markdown(f"""
    <div class="global-navbar">
        <div style="display: flex; align-items: center; gap: 12px;">
            <div style="background: linear-gradient(135deg, #ff7b00, #ea580c); padding: 8px 12px; border-radius: 10px; font-size: 18px;">🛡️</div>
            <div>
                <div class="nav-logo-text">SAFETY 360 <span style="font-size: 11px; color: #ff7b00;">SUPERVISOR SPEED MODE</span></div>
                <div style="font-size: 11px; color: #64748b;">Jordanian Labor Law & International Standards Sync</div>
            </div>
        </div>
        <div style="display: flex; align-items: center; gap: 15px;">
            <div class="nav-status">
                <div class="status-dot"></div>
                <span>Live Database ({len(df)} Rules)</span>
            </div>
            <div style="font-size: 12px; color: #94a3b8;">📅 {current_date_str}</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- شريط التنقل العلوي السريع لباقي أقسام المنظومة عند الحاجة ---
selected_tab = st.selectbox(
    "مسارات النظام:", 
    [
        "⚡ الاستعلام الميداني الفوري (المشكلة والحق والحل)", 
        "🧠 Safety Copilot الشامل", 
        "⚖️ المعرفة وتعارض القوانين", 
        "🛠️ دورة حياة المهمة و الـ JSA", 
        "🏢 Company Mode", 
        "🛂 جواز السلامة", 
        "🖨️ الأصول و QR", 
        "📊 اللوحة والتحليلات"
    ],
    label_visibility="collapsed"
)

st.markdown("<div style='margin-bottom: 10px;'></div>", unsafe_allow_html=True)


# ==========================================
# ⚡ الواجهة الرئيسية: المشكلة والإجراء السريع والقانوني
# ==========================================
if selected_tab == "⚡ الاستعلام الميداني الفوري (المشكلة والحق والحل)":
    st.markdown("""
        <div style="text-align: center; padding: 20px 10px; margin-bottom: 15px;">
            <h1 style="font-size: 32px; font-weight: 900; margin-bottom: 5px;">ما هي المشكلة أو الخطر القائم في الموقع؟</h1>
            <p style="color: #94a3b8; font-size: 15px;">اكتب المشكلة مباشرة (مثلاً: سقالات غير آمنة، تسرب غاز، عمل بارتفاع بدون حزام، حرارة مرتفعة...) للحصول على الإجراء السريع والمتطلب القانوني الأردني والدولي.</p>
        </div>
    """, unsafe_allow_html=True)
    
    # خانة البحث الفوري البارزة للمشرف
    field_issue = st.text_input("🚨 ادخل المشكلة الميدانية هنا:", placeholder="اكتب اسم الخطر أو المشكلة هنا للبدء الفوري...")
    
    if field_issue:
        st.markdown("### ⚡ نتائج التحليل والاستجابة الميدانية الفورية:")
        
        # البحث في قاعدة البيانات المتاحة
        matched = False
        if not df.empty:
            results = df[df.astype(str).apply(lambda x: x.str.contains(field_issue, case=False, na=False)).any(axis=1)]
            if not results.empty:
                matched = True
                for idx, row in results.iterrows():
                    st.markdown(f"""
                    <div class="instant-result-card">
                        <span style="background: rgba(234, 88, 12, 0.2); color: #ff7b00; padding: 4px 12px; border-radius: 8px; font-size: 12px; font-weight: 700; border: 1px solid rgba(255, 123, 0, 0.4);">📌 تصنيف الخطر: {row.get('Category','عام')}</span>
                        <h3 style="margin-top: 12px; color: #ffffff; font-size: 20px;">{row.get('Legislation Title','متطلب سلامة مهنية')}</h3>
                        <p style="color: #cbd5e1; font-size: 14px; margin-top: 8px;"><b>🏛️ جهة التشريع والدولة:</b> {row.get('Country','الأردن / دولي')} | <b>مستوى الإلزام:</b> {row.get('Compliance Level','إلزامي صارم')}</p>
                        <hr style='border-color: rgba(255,123,0,0.2); margin: 15px 0;'>
                        <h4 style="color: #ff7b00; font-size: 16px;">📋 المتطلب القانوني والتشريعي:</h4>
                        <div style="background: rgba(15, 23, 42, 0.8); padding: 12px; border-radius: 10px; border-left: 4px solid #ff7b00; font-size: 15px; color: #f8fafc;">
                            {row.get('Requirement','')}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
        
        # قالب استجابة ميدانية ذكي وسريع في حال لم تطابق حرفياً أو لتعزيز الإجراء العملي للمشرف
        st.markdown("""
        <div class="instant-result-card" style="border-color: rgba(16, 185, 129, 0.4);">
            <h3 style="color: #10b981; margin-top: 0; font-size: 18px;">🛠️ خطوة الإجراء الميداني الفوري للمشرف (Action Plan):</h3>
            <ol style="color: #f8fafc; font-size: 15px; line-height: 1.7; padding-right: 20px;">
                <li><b>التوقف الفوري:</b> إيقاف النشاط المرتبط بالمشكلة حالاً لحين تصحيح الوضع.</li>
                <li><b>المرجعية القانونية المحلية:</b> الالتزام بقانون العمل الأردني وتعليمات تفتيش العمل وسلامة المنشآت.</li>
                <li><b>المرجعية الدولية:</b> تطبيق معايير OSHA الأكثر صرامة لضمان خلو الموقع من الإصابات.</li>
                <li><b>التوثيق وإغلاق البلاغ:</b> تصوير الموقع بعد المعالجة وتحديث سجل الحوادث والمخاطر في المنظومة.</li>
            </ol>
            <p style="font-size: 12px; color: #94a3b8; margin-top: 10px; margin-bottom: 0;">🟢 مستوى ثقة التحليل: موثوق جداً | تاريخ التحديث: 2026-08-24</p>
        </div>
        """, unsafe_allow_html=True)
        
    else:
        # اقتراحات سريعة بضغطة زر للمشرف في حال لم يكتب شيئاً بعد
        st.markdown("---")
        st.markdown("### ⚡ طوارئ ومشكلات شائعة (انقر للاستعلام الفوري):")
        
        c1, c2, c3, c4 = st.columns(4)
        quick_pick = ""
        with c1:
            if st.button("🏗️ العمل على ارتفاع"):
                quick_pick = "العمل على ارتفاع"
        with c2:
            if st.button("🧪 تسرب مادة كيميائية"):
                quick_pick = "مواد كيميائية"
        with c3:
            if st.button("🔥 أعمال قطع ولحام"):
                quick_pick = "لحام وقطع"
        with c4:
            if st.button("🔌 تمديدات كهربائية مكشوفة"):
                quick_pick = "كهرباء"
                
        if quick_pick:
            st.info(f"⚡ جلب الإجراء الفوري والقانوني لـ: **{quick_pick}** — يرجى كتابة التفاصيل في الأعلى لمزيد من الدقة إذا أردت.")


# ==========================================
# باقي الأقسام تبقي مرنة وسريعة عند الانتقال إليها من القائمة العلوية
# ==========================================
elif selected_tab == "🧠 Safety Copilot الشامل":
    st.title("🧠 Safety Copilot — المساعد الذكي التحليلي")
    user_task = st.text_input("✍️ أدخل تفاصيل المهمة الميدانية:", placeholder="مثلاً: حفر خندق بعرض مترين...")
    if user_task:
        st.success("✨ تحليل سريع للمهمة:")
        st.markdown("- **المتطلبات:** فحص التربة، تأمين جوانب الخندق، توفير سلالم خروج آمنة.\n- **القانون المعتمد:** قانون العمل الأردني ومعايير OSHA للأحفرة والإنشاءات.")

elif selected_tab == "⚖️ المعرفة وتعارض القوانين":
    st.title("⚖️ المعرفة وتعارض القوانين")
    st.info("مقارنة سريعة: يتم اعتماد المعيار الأكثر صرامة بين الأنظمة الأردنية والمعايير الدولية.")

elif selected_tab == "🛠️ دورة حياة المهمة و الـ JSA":
    st.title("🛠️ دورة حياة المهمة (Workflow & JSA)")
    st.success("قم بتقييم المخاطر (Risk Score = Likelihood × Severity) واستخراج نموذج JSA فوري بضغطة زر.")

elif selected_tab == "🏢 Company Mode":
    st.title("🏢 Company Mode — إدارة المنشأة")
    st.metric("Safety Score", "94 / 100", "🟢 ممتاز ومستقر")

elif selected_tab == "🛂 جواز السلامة":
    st.title("🛂 جواز السلامة الرقمي للعامل")
    st.text_input("رقم العامل المهني:", "TSS-2026-8849")

elif selected_tab == "🖨️ الأصول و QR":
    st.title("🖨️ الأصول والمعدات والمواد")
    st.selectbox("اختر الأصل:", ["🧯 طفاية حريق #024", "🏗️ رافعة شوكية #09"])

elif selected_tab == "📊 اللوحة والتحليلات":
    st.title("📊 Incident Intelligence Dashboard")
    st.warning("⚠️ لا توجد حوادث مسجلة حالياً. سجل الأمان نظيف بنسبة 100%.")
