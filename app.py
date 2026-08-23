import streamlit as st
import pandas as pd
import os
from datetime import datetime

# إعدادات الصفحة
st.set_page_config(
    page_title="SAFETY 360 | Global Intelligence & Crisis Command", 
    page_icon="🛡️", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# تصميم واجهة شركة عالمية (Global Enterprise UI & Top Nav)
st.markdown("""
    <style>
        /* إخفاء عناصر Streamlit الافتراضية غير المرغوب فيها للوصول لتصميم نظيف */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* الخلفية العامة */
        .stApp {
            background: radial-gradient(circle at 50% 0%, #090d16 0%, #020617 100%) !important;
        }
        
        /* الشريط العلوي العالمي (Global Top Navbar) */
        .global-navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: rgba(11, 18, 33, 0.85);
            backdrop-filter: blur(16px);
            border-bottom: 1px solid rgba(255, 123, 0, 0.25);
            padding: 14px 30px;
            border-radius: 14px;
            margin-bottom: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }
        .nav-logo {
            display: flex;
            align-items: center;
            gap: 12px;
        }
        .nav-logo-icon {
            width: 38px;
            height: 38px;
            background: linear-gradient(135deg, #ff7b00 0%, #ea580c 100%);
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
            box-shadow: 0 0 15px rgba(255, 123, 0, 0.4);
        }
        .nav-logo-text {
            font-size: 20px;
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
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 13px;
            color: #10b981;
            font-weight: 600;
        }
        .status-dot {
            width: 8px;
            height: 8px;
            background-color: #10b981;
            border-radius: 50%;
            box-shadow: 0 0 8px #10b981;
            animation: pulse 2s infinite;
        }
        @keyframes pulse {
            0% { transform: scale(0.95); opacity: 0.8; }
            50% { transform: scale(1.2); opacity: 1; }
            100% { transform: scale(0.95); opacity: 0.8; }
        }

        /* حقول الإدخال العالمية */
        .stTextInput input, .stTextArea textarea, .stSelectbox select {
            background-color: rgba(15, 23, 42, 0.9) !important;
            color: #ffffff !important;
            -webkit-text-fill-color: #ffffff !important;
            border-radius: 12px !important;
            border: 1px solid rgba(255, 123, 0, 0.35) !important;
            padding: 12px !important;
            font-size: 15px !important;
        }
        .stTextInput input:focus {
            border-color: #ff7b00 !important;
            box-shadow: 0 0 15px rgba(255, 123, 0, 0.25) !important;
        }

        h1, h2, h3, h4, h5, h6, p, span, label {
            color: #f8fafc !important;
        }

        /* تنبيهات النظام */
        div.stAlert {
            background: rgba(15, 23, 42, 0.95) !important;
            color: #ffffff !important;
            border: 1px solid rgba(255, 123, 0, 0.4) !important;
            border-radius: 12px;
        }

        /* بطاقات الأفكار والعمليات العصرية (Global Command Cards) */
        .enterprise-card {
            background: linear-gradient(135deg, rgba(30, 41, 59, 0.45) 0%, rgba(15, 23, 42, 0.8) 100%);
            border: 1px solid rgba(255, 123, 0, 0.25);
            padding: 24px;
            border-radius: 16px;
            backdrop-filter: blur(12px);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            margin-bottom: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }
        .enterprise-card:hover {
            border-color: #ff7b00;
            transform: translateY(-4px);
            box-shadow: 0 15px 35px rgba(255, 123, 0, 0.2);
        }

        /* أزرار Streamlit بأسلوب الشركات التقنية الكبرى */
        .stButton button {
            width: 100%;
            background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
            color: #f8fafc !important;
            border: 1px solid rgba(255, 123, 0, 0.35);
            border-radius: 12px;
            padding: 12px 20px;
            font-weight: 600;
            transition: all 0.3s ease;
        }
        .stButton button:hover {
            background: linear-gradient(135deg, #ff7b00 0%, #ea580c 100%);
            border-color: #ff7b00;
            color: #ffffff !important;
            box-shadow: 0 0 20px rgba(255, 123, 0, 0.4);
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

# --- الشريط العلوي العالمي (Global Enterprise Top Bar) ---
st.markdown(f"""
    <div class="global-navbar">
        <div class="nav-logo">
            <div class="nav-logo-icon">🛡️</div>
            <div>
                <div class="nav-logo-text">SAFETY 360 <span style="font-size: 11px; color: #ff7b00; font-weight: 500;">ENTERPRISE</span></div>
                <div style="font-size: 11px; color: #64748b;">Global Crisis & Safety Intelligence Platform</div>
            </div>
        </div>
        <div style="display: flex; align-items: center; gap: 20px;">
            <div class="nav-status">
                <div class="status-dot"></div>
                <span>AI Core: Active ({len(df)} Standards)</span>
            </div>
            <div style="font-size: 12px; color: #94a3b8; border-right: 1px solid rgba(255,255,255,0.1); padding-right: 15px;">
                📅 {current_date_str}
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- شريط الانتقالات العلوية (Horizontal Navigation Tabs) بدل القائمة الجانبية التقليدية ---
menu_options = [
    "🏠 الرئيسية والعمليات", 
    "🧠 Safety Copilot", 
    "⚖️ المعرفة والتعارضات", 
    "🛠️ دورة حياة المهمة", 
    "🏢 Company Mode", 
    "🛂 جواز السلامة", 
    "🖨️ الأصول والـ QR", 
    "📊 التحليلات واللوحة"
]

selected_tab = st.selectbox("🧭 اختر مسار القيادة والتحكم العالمي:", menu_options, label_visibility="collapsed")
st.markdown("<div style='margin-bottom: 25px;'></div>", unsafe_allow_html=True)


# ==========================================
# 1. 🏠 الرئيسية والعمليات
# ==========================================
if selected_tab == "🏠 الرئيسية والعمليات":
    st.markdown("""
        <div style="padding: 40px 30px; background: linear-gradient(135deg, rgba(30, 41, 59, 0.5) 0%, rgba(15, 23, 42, 0.9) 100%); border-radius: 20px; border: 1px solid rgba(255, 123, 0, 0.3); margin-bottom: 35px; text-align: center; box-shadow: 0 20px 40px rgba(0,0,0,0.6);">
            <span style="background: rgba(255, 123, 0, 0.15); color: #ff7b00; padding: 6px 18px; border-radius: 20px; font-size: 13px; font-weight: 700; border: 1px solid rgba(255, 123, 0, 0.4);">⚡ Next-Gen Enterprise Safety Ecosystem</span>
            <h1 style="margin-top: 15px; font-size: 42px; font-weight: 900; background: linear-gradient(90deg, #ffffff 0%, #cbd5e1 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">COMMAND & INTELLIGENCE HUB</h1>
            <p style="color: #94a3b8; font-size: 16px; max-width: 750px; margin: 12px auto 0 auto; line-height: 1.6;">منصة مركزية متطورة لإدارة المخاطر التشغيلية، الرقابة الفورية على الأزمات، والامتثال للمعايير العالمية بدعم كامل من الذكاء الاصطناعي.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎯 الإجراءات السريعة (Quick Operations):")
    st.write("")
    
    col1, col2, col3 = st.columns(3)
    
    intent = ""
    with col1:
        st.markdown('<div class="enterprise-card">', unsafe_allow_html=True)
        if st.button("🚨 حالة طوارئ فوريّة", use_container_width=True):
            intent = "emergency"
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="enterprise-card">', unsafe_allow_html=True)
        if st.button("⚖️ الاستعلام القانوني", use_container_width=True):
            intent = "law"
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="enterprise-card">', unsafe_allow_html=True)
        if st.button("🤖 سؤال Safety Copilot", use_container_width=True):
            intent = "copilot"
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col2:
        st.markdown('<div class="enterprise-card">', unsafe_allow_html=True)
        if st.button("⚠️ تقييم الخطر (Risk Assessment)", use_container_width=True):
            intent = "risk"
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="enterprise-card">', unsafe_allow_html=True)
        if st.button("🧪 صحيفة مادة كيميائية (SDS)", use_container_width=True):
            intent = "material"
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="enterprise-card">', unsafe_allow_html=True)
        if st.button("🛂 فحص جواز السلامة", use_container_width=True):
            intent = "passport"
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col3:
        st.markdown('<div class="enterprise-card">', unsafe_allow_html=True)
        if st.button("📋 نموذج JSA & Workflow", use_container_width=True):
            intent = "workflow"
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="enterprise-card">', unsafe_allow_html=True)
        if st.button("📸 تحليل خطر بصري (AI Vision)", use_container_width=True):
            intent = "vision"
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="enterprise-card">', unsafe_allow_html=True)
        if st.button("🏢 فتح Company Mode", use_container_width=True):
            intent = "company"
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")
    
    if intent == "emergency":
        st.error("🚨 بروتوكول الاستجابة السريعة للطوارئ:")
        st.markdown("1. تفعيل صفارات الإنذار ونظام البلاغات الآلي.\n2. الاتصال بغرفة العمليات والجهات المختصة (911).\n3. إخلاء المنطقة وتوجيه العاملين إلى نقاط التجمع الآمنة.")
    elif intent == "law" or intent == "":
        q_search = st.text_input("🔍 بحث فوري في قاعدة البيانات والمعايير العالمية:", placeholder="مثلاً: أعمال البناء، السقالات، المواد الخطرة، مساحات مغلقة...")
        if q_search and not df.empty:
            results = df[df.astype(str).apply(lambda x: x.str.contains(q_search, case=False, na=False)).any(axis=1)]
            if not results.empty:
                for idx, row in results.iterrows():
                    with st.expander(f"📌 [{row.get('Category','')}] - {row.get('Legislation Title','')} ({row.get('Country','')})"):
                        st.markdown(f"**🏛️ مستوى الإلزام:** `{row.get('Compliance Level','')}` | **🔍 الثقة:** 🟢 موثوق جدًا")
                        st.markdown(f"**📅 التاريخ:** `{current_date_str}`")
                        st.markdown(f"**📋 المتطلب:**\n> {row.get('Requirement','')}")
            else:
                st.warning("⚠️ لم يتم العثور على نتائج مطابقة.")
    elif intent == "copilot":
        st.info("💡 انتقل إلى مسار (Safety Copilot) من القائمة العلوية لتجربة المساعد التحليلي التفاعلي.")
    elif intent == "risk":
        st.info("💡 أدوات تقييم المخاطر متاحة عبر مسار (دورة حياة المهمة).")


# ==========================================
# 2. 🧠 Safety Copilot
# ==========================================
elif selected_tab == "🧠 Safety Copilot":
    st.title("🧠 Safety Copilot — المساعد الذكي التحليلي")
    st.markdown("تحليل مهام العمل، تقييم المخاطر الميدانية الفورية، واستخراج بروتوكولات الاستجابة بدقة متناهية.")
    
    user_task = st.text_input("✍️ أدخل تفاصيل المهمة أو النشاط الميداني:", placeholder="مثلاً: تنفيذ أعمال لحام وقطع في خزان وقود...")
    
    if user_task:
        st.markdown("### 💬 تحليل Safety Copilot التشغيلي:")
        c1, c2 = st.columns(2)
        with c1:
            loc_type = st.selectbox("طبيعة موقع العمل:", ["موقع مفتوح / خارجي", "مكان مغلق (Confined Space)", "ارتفاع شاهق", "منطقة خطرة قابلة للاشتعال"])
            has_chem = st.selectbox("هل توجد مواد كيميائية أو قابلة للاشتعال؟", ["نعم", "لا"])
        with c2:
            has_height = st.selectbox("هل يتطلب العمل ارتفاعات؟", ["نعم", "لا"])
            team_size = st.number_input("عدد الأفراد المشاركين:", min_value=1, value=4)
            
        if st.button("🚀 توليد خطة السلامة التشغيلية المعتمدة"):
            st.success("✨ تم إنشاء خطة الأمان بنجاح:")
            st.markdown(f"""
            * **📋 النشاط المحلل:** {user_task} ({loc_type})
            * **🟢 مستوى الثقة:** `مستند لمعايير OSHA و ISO 45001`
            * **📅 تاريخ الإصدار:** `{current_date_str}`
            
            ---
            ### 🛡️ الاشتراطات وإجراءات السيطرة:
            1. **التصاريح التنظيمية:** إصدار رخصة عمل ساخن (Hot Work Permit) ومراجعة كاشف الغازات.
            2. **معدات الوقاية (PPE):** خوذة سلامة، نظارات حماية داكنة، ملابس مقاومة للحرارة، وأحذية عازلة.
            3. **الرقابة الميدانية:** توافر مراقب حريق (Fire Watcher) وتجهيز طفايات الحريق المناسبة بالموقع.
            4. **إجراءات الطوارئ:** مسارات إخلاء واضحة وتوافر حقيبة إسعافات أولية متقدمة.
            """)


# ==========================================
# 3. ⚖️ المعرفة والتعارضات
# ==========================================
elif selected_tab == "⚖️ المعرفة والتعارضات":
    st.title("⚖️ إدارة المعرفة وتعارض القوانين (Compliance & Conflicts)")
    st.markdown("مقارنة ذكية بين التشريعات المحلية والمعايير الدولية وكشف التعارضات برمجياً.")
    
    topic = st.selectbox("اختر الموضوع للتحقق:", ["أعمال البناء والتشييد والعمل على ارتفاعات", "العمل داخل الأماكن المغلقة", "التعامل مع المواد الكيميائية الخطرة"])
    
    if topic:
        st.markdown(f"### 🔍 تحليل التوافق والتنظيم لـ: {topic}")
        col_loc, col_int = st.columns(2)
        with col_loc:
            st.info("🇯🇴 المتطلب المحلي (الأنظمة الأردنية):")
            st.markdown("- الالتزام بقانون العمل وتعليمات وزارة العمل الأردنية.\n- التركيز على الإشراف الميداني ولجان السلامة.")
        with col_int:
            st.info("🌎 المعيار الدولي (OSHA / ISO):")
            st.markdown("- OSHA 1926: الحماية الإجبارية عند ارتفاع 1.8 متر (6 قدم).\n- ISO 45001: نظام إدارة السلامة والصحة المهنية.")
            
        st.markdown("---")
        st.success("💡 **التوصية المعتمدة عالمياً:** يُطبق **المعيار الأكثر صرامة** (الالتزام بحدود 1.8 متر والمعايير الدولية لضمان أقصى حماية وتلبية المتطلبات المحلية معاً).")


# ==========================================
# 4. 🛠️ دورة حياة المهمة
# ==========================================
elif selected_tab == "🛠️ دورة حياة المهمة":
    st.title("🛠️ Safety Workflow — دورة حياة المهمة المتكاملة")
    st.markdown("إدارة مراحل العمل الميداني: من تحليل المخاطر (Risk Assessment) حتى إغلاق المهمة.")
    
    step = st.radio("اختر المرحلة التنفيذية الحالية:", ["1. Risk Assessment", "2. JSA (Job Safety Analysis)", "3. Permit to Work", "4. Execution", "5. Closeout"])
    if "1." in step:
        p = st.slider("الاحتمالية (1-5):", 1, 5, 2)
        s = st.slider("الشدة (1-5):", 1, 5, 4)
        score = p * s
        st.metric("مستوى الخطورة الإجمالي (Risk Score)", score)
        if score >= 15:
            st.error("🚨 خطر مرتفع! يتطلب اعتماد فوري من مدير السلامة.")
    else:
        st.info(f"📍 المرحلة النشطة: {step} — النظام يتابع كافة المتطلبات التنظيمية والميدانية بدقة.")


# ==========================================
# 5. 🏢 Company Mode
# ==========================================
elif selected_tab == "🏢 Company Mode":
    st.title("🏢 Company Mode — لوحة تحكم المنشأة المؤسسية")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Safety Score", "94 / 100", "🟢 ممتاز")
    c2.metric("إجمالي العمال", "42 عامل", "نشطون")
    c3.metric("المواقع المدارة", "3 مواقع", "عمان، العقبة، الزرقاء")
    c4.metric("الحوادث", "0 حادث", "سجل نظيف")


# ==========================================
# 6. 🛂 جواز السلامة
# ==========================================
elif selected_tab == "🛂 جواز السلامة":
    st.title("🛂 Safety Passport — جواز السلامة الرقمي للعامل")
    wid = st.text_input("أدخل رقم العامل المهني:", "TSS-2026-8849")
    if wid:
        st.success("🟢 تم العثور على الملف: طارق السقرات (مشرف سلامة / إدارة أزمات)")
        st.markdown("""
        * **🪪 الهوية المهنية:** TSS-2026-8849
        * **🎓 الاعتمادات والدورات:** إدارة الأزمات، ICDL، الإسعافات الأولية المتقدمة (ساري).
        * **🛠️ الصلاحيات:** الإشراف على مواقع الإنشاءات والطوارئ الأولية.
        """)


# ==========================================
# 7. 🖨️ الأصول والـ QR
# ==========================================
elif selected_tab == "🖨️ الأصول والـ QR":
    st.title("🖨️ نظام الأصول والمعدات (QR & Assets)")
    ast = st.selectbox("اختر الأصل الميداني:", ["🧯 طفاية حريق #024", "🏗️ رافعة شوكية #09", "🧪 برميل مادة كيميائية #C-12"])
    st.info(f"📌 تفاصيل أصل المعدة: {ast} — الحالة: 🟢 جاهزة وآمنة للاستخدام.")


# ==========================================
# 8. 📊 التحليلات واللوحة
# ==========================================
elif selected_tab == "📊 التحليلات واللوحة":
    st.title("📊 Incident Intelligence & Analytics Dashboard")
    st.warning("⚠️ **تنبيه الذكاء الاصطناعي:** تم رصد أنماط تشابه في بلاغات سابقة. يُنصح بتكثيف التفتيش الميداني.")
    col_a, col_b = st.columns(2)
    col_a.metric("مؤشر المخاطر التراكمي", "منخفض جداً", "-12%")
    col_b.metric("نسبة إغلاق الإجراءات", "100%", "مكتمل")
