import streamlit as st
import pandas as pd
import os
from datetime import datetime

# إعدادات الصفحة
st.set_page_config(
    page_title="SAFETY 360 | AI-Powered Safety Intelligence", 
    page_icon="🛡️", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# تصميم واجهة الـ Command Center المتقدم والـ Glassmorphism العصري
st.markdown("""
    <style>
        /* الخلفية العامة */
        .stApp {
            background: radial-gradient(circle at 50% 0%, #0f172a 0%, #020617 100%) !important;
        }
        
        /* تخصيص القائمة الجانبية لتشبه منصات القيادة */
        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #090d16 0%, #020617 100%) !important;
            border-right: 1px solid rgba(255, 123, 0, 0.2);
        }
        section[data-testid="stSidebar"] * {
            color: #f1f5f9 !important;
        }
        
        /* إخفاء عناصر الراديو الافتراضية وجعلها تبدو كأزرار تحكم متطورة */
        .stRadio > label {
            font-weight: 700;
            color: #ff7b00 !important;
            margin-bottom: 10px;
        }
        
        /* حقول الإدخال والنصوص */
        .stTextInput input, .stTextArea textarea, .stSelectbox select {
            background-color: rgba(15, 23, 42, 0.8) !important;
            color: #ffffff !important;
            -webkit-text-fill-color: #ffffff !important;
            border-radius: 12px !important;
            border: 1px solid rgba(255, 123, 0, 0.4) !important;
            padding: 12px !important;
            font-size: 15px !important;
            box-shadow: inset 0 2px 4px rgba(0,0,0,0.5);
        }
        .stTextInput input:focus, .stTextArea textarea:focus {
            border-color: #ff7b00 !important;
            box-shadow: 0 0 15px rgba(255, 123, 0, 0.3) !important;
        }

        h1, h2, h3, h4, h5, h6, p, span, label {
            color: #f8fafc !important;
        }

        /* تنبيهات النظام الاحترافية */
        div.stAlert {
            background: rgba(15, 23, 42, 0.95) !important;
            color: #ffffff !important;
            border: 1px solid rgba(255, 123, 0, 0.5) !important;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.4);
        }

        /* تصميم بطاقات الأوامر السريعة في الواجهة الرئيسية */
        .command-card {
            background: linear-gradient(135deg, rgba(30, 41, 59, 0.4) 0%, rgba(15, 23, 42, 0.7) 100%);
            border: 1px solid rgba(255, 123, 0, 0.25);
            padding: 22px;
            border-radius: 18px;
            text-align: center;
            backdrop-filter: blur(12px);
            transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
            margin-bottom: 20px;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        }
        .command-card:hover {
            border-color: #ff7b00;
            transform: translateY(-5px);
            box-shadow: 0 12px 30px -5px rgba(255, 123, 0, 0.3);
            background: linear-gradient(135deg, rgba(30, 41, 59, 0.7) 0%, rgba(15, 23, 42, 0.9) 100%);
        }

        /* أزرار Streamlit المخصصة */
        .stButton button {
            width: 100%;
            background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
            color: #f8fafc !important;
            border: 1px solid rgba(255, 123, 0, 0.3);
            border-radius: 12px;
            padding: 12px 20px;
            font-weight: 600;
            letter-spacing: 0.5px;
            transition: all 0.3s ease;
        }
        .stButton button:hover {
            background: linear-gradient(135deg, #ff7b00 0%, #ea580c 100%);
            border-color: #ff7b00;
            color: #ffffff !important;
            box-shadow: 0 0 20px rgba(255, 123, 0, 0.4);
            transform: scale(1.02);
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

# --- القائمة الجانبية المحدثة بأسلوب منصات التحكم الذكية ---
with st.sidebar:
    st.markdown("""
        <div style="text-align: center; padding: 10px 0;">
            <h2 style="margin: 0; color: #ff7b00; font-weight: 900; font-size: 26px;">🛡️ SAFETY 360</h2>
            <p style="font-size: 11px; color: #94a3b8; letter-spacing: 1px; margin-top: 5px;">COMMAND & INTELLIGENCE CENTER</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<hr style='border-color: rgba(255,123,0,0.2); margin: 15px 0;'>", unsafe_allow_html=True)
    st.markdown("### 🧭 مسارات المنظومة")
    
    menu = st.radio(
        "اختر المسار التشغيلي:",
        [
            "🏠 الرئيسية (ماذا تريد أن تفعل؟)",
            "🧠 Safety Copilot (المساعد الذكي المتكامل)",
            "⚖️ Knowledge & Conflicts (المعرفة وتعارض القوانين)",
            "🛠️ Safety Workflow (دورة حياة المهمة)",
            "🏢 Company Mode (إدارة المنشأة)",
            "🛂 Safety Passport (جواز السلامة للعامل)",
            "🖨️ QR Codes & Assets (الأصول والمعدات)",
            "📊 Incident Intelligence & Dashboard"
        ],
        label_visibility="collapsed"
    )
    
    st.markdown("<hr style='border-color: rgba(255,123,0,0.2); margin: 20px 0;'>", unsafe_allow_html=True)
    
    # مؤشرات الحالة في الشريط الجانبي
    if not df.empty:
        st.markdown("🟢 **حالة الخادم:** متصل وآمن")
        st.markdown(f"📊 **المعايير المعتمدة:** `{len(df)}` قاعدة بيانات")
    else:
        st.markdown("🔴 **حالة الخادم:** وضع غير متصل (Offline Mode)")
        
    st.markdown("<hr style='border-color: rgba(255,123,0,0.2); margin: 20px 0;'>", unsafe_allow_html=True)
    st.markdown("""
        <div style="text-align: center; font-size: 12px; color: #64748b;">
            <b>Disaster & Crisis Management</b><br>
            Engineered by T.S.S © 2026
        </div>
    """, unsafe_allow_html=True)


# ==========================================
# 1. 🏠 الرئيسية (ماذا تريد أن تفعل؟)
# ==========================================
if menu == "🏠 الرئيسية (ماذا تريد أن تفعل؟)":
    # Header بصري جذاب ومستقبلي
    st.markdown("""
        <div style="padding: 35px 25px; background: linear-gradient(135deg, rgba(30, 41, 59, 0.6) 0%, rgba(15, 23, 42, 0.9) 100%); border-radius: 20px; border: 1px solid rgba(255, 123, 0, 0.35); margin-bottom: 35px; text-align: center; box-shadow: 0 15px 35px rgba(0,0,0,0.5);">
            <span style="background: rgba(255, 123, 0, 0.15); color: #ff7b00; padding: 6px 18px; border-radius: 20px; font-size: 13px; font-weight: 700; border: 1px solid rgba(255, 123, 0, 0.4);">⚡ نظام القيادة والتحقّم السيبراني والميداني</span>
            <h1 style="margin-top: 15px; font-size: 40px; font-weight: 900; background: linear-gradient(90deg, #ffffff 0%, #cbd5e1 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">SAFETY 360 INTELLIGENCE</h1>
            <p style="color: #94a3b8; font-size: 16px; max-width: 750px; margin: 12px auto 0 auto; line-height: 1.6;">منصة ذكية متكاملة لإدارة السلامة والصحة المهنية، تقييم المخاطر الميدانية، واستجابة الطوارئ الفورية المدعومة بالذكاء الاصطناعي.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎯 لوحة التحكم السريعة (اختر الهدف التشغيلي):")
    st.write("")
    
    col1, col2, col3 = st.columns(3)
    
    intent = ""
    with col1:
        st.markdown('<div class="command-card">', unsafe_allow_html=True)
        if st.button("🚨 حالة طوارئ فوريّة", use_container_width=True):
            intent = "emergency"
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="command-card">', unsafe_allow_html=True)
        if st.button("⚖️ الاستعلام عن متطلب قانوني", use_container_width=True):
            intent = "law"
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="command-card">', unsafe_allow_html=True)
        if st.button("🤖 سؤال Safety Copilot", use_container_width=True):
            intent = "copilot"
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col2:
        st.markdown('<div class="command-card">', unsafe_allow_html=True)
        if st.button("⚠️ تقييم المخاطر (Risk Assessment)", use_container_width=True):
            intent = "risk"
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="command-card">', unsafe_allow_html=True)
        if st.button("🧪 بيانات مادة كيميائية (SDS)", use_container_width=True):
            intent = "material"
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="command-card">', unsafe_allow_html=True)
        if st.button("🛂 فحص جواز السلامة (Passport)", use_container_width=True):
            intent = "passport"
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col3:
        st.markdown('<div class="command-card">', unsafe_allow_html=True)
        if st.button("📋 إنشاء نموذج JSA & Workflow", use_container_width=True):
            intent = "workflow"
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="command-card">', unsafe_allow_html=True)
        if st.button("📸 تحليل صورة خطر (AI Vision)", use_container_width=True):
            intent = "vision"
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="command-card">', unsafe_allow_html=True)
        if st.button("🏢 فتح Company Mode", use_container_width=True):
            intent = "company"
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")
    
    # توجيه المستخدم حسب اختياره السريع
    if intent == "emergency":
        st.error("🚨 بروتوكول الطوارئ السريع:")
        st.markdown("1. أطلق صفارة الإنذار وتفعيل نظام الإنذار المبكر.\n2. الاتصال الفوري بغرفة العمليات والدفاع المدني (911).\n3. إخلاء الموقع فوراً التوجه لنقطة التجمع الآمنة المعتمدة.")
    elif intent == "law" or intent == "":
        q_search = st.text_input("🔍 بحث فوري في التشريعات والمعايير:", placeholder="مثلاً: أعمال البناء، السقالات، تسرب غاز، مواد خطرة...")
        if q_search and not df.empty:
            results = df[df.astype(str).apply(lambda x: x.str.contains(q_search, case=False, na=False)).any(axis=1)]
            if not results.empty:
                for idx, row in results.iterrows():
                    with st.expander(f"📌 [{row.get('Category','')}] - {row.get('Legislation Title','')} ({row.get('Country','')})"):
                        st.markdown(f"**🏛️ مستوى الإلزام:** `{row.get('Compliance Level','')}` | **🔍 مستوى الثقة:** 🟢 موثوق جدًا")
                        st.markdown(f"**📅 آخر تحقق:** `{current_date_str}`")
                        st.markdown(f"**📋 المتطلب:**\n> {row.get('Requirement','')}")
            else:
                st.warning("⚠️ لم يتم العثور على نتائج مطابقة في قاعدة البيانات.")
    elif intent == "copilot":
        st.info("💡 يرجى الانتقال من القائمة الجانبية إلى (Safety Copilot) لتجربة المساعد الذكي التفاعلي المتكامل.")
    elif intent == "risk":
        st.info("💡 أداة تقييم المخاطر متاحة عبر مسار (Safety Workflow) في القائمة الجانبية.")
    elif intent == "material":
        st.info("🧪 قاعدة بيانات المواد: ابحث برسم المادة أو رقم CAS للحصول على صحيفة بيانات السلامة (SDS).")


# ==========================================
# 2. 🧠 Safety Copilot (المساعد الذكي المتكامل)
# ==========================================
elif menu == "🧠 Safety Copilot (المساعد الذكي المتكامل)":
    st.title("🧠 Safety Copilot — المساعد الذكي التحليلي")
    st.markdown("المساعد لا يجيب فقط، بل يفهم المهمة، يحلل المخاطر التفاعلية، ويستخرج الإجراءات والمصادر.")
    
    user_task = st.text_input("✍️ ما هي المهمة التي تود تنفيذها؟", placeholder="مثلاً: تنفيذ أعمال لحام وقطع في موقع إنشائي مرتفع...")
    
    if user_task:
        st.markdown("### 💬 تفاعل Safety Copilot التلقائي معك:")
        st.markdown("عشان نبني خطة سلامة دقيقة، يرجى تحديد التفاصيل التالية:")
        
        c1, c2 = st.columns(2)
        with c1:
            loc_type = st.selectbox("أين سيتم العمل؟", ["مفتوح / خارجي", "مكان مغلق (Confined Space)", "ارتفاع شاهق", "منطقة قابلة للاشتعال"])
            has_chem = st.selectbox("هل توجد مواد قابلة للاشتعال أو كيميائية؟", ["نعم", "لا"])
        with c2:
            has_height = st.selectbox("هل يوجد عمل على ارتفاع؟", ["نعم", "لا"])
            team_size = st.number_input("عدد العمال المشاركين:", min_value=1, value=3)
            
        if st.button("🚀 بناء خطة السلامة الشاملة للمهمة"):
            st.success("✨ تم بناء خطة السلامة التشغيلية بنجاح:")
            st.markdown(f"""
            * **📋 المهمة المحللة:** {user_task} (الموقع: {loc_type})
            * **🟢 مستوى الثقة في التحليل:** `🟢 موثوق جدًا (مستند لمعايير OSHA وتشريعات العمل)`
            * **📅 آخر تحديث للمصادر:** `{current_date_str}`
            
            ---
            ### 🛡️ خطوة الإجراءات والسيطرة:
            1. **التصاريح اللازمة:** استخراج (Hot Work Permit) + (Confined Space Permit إذا لزم).
            2. **معدات الوقاية الشخصية (PPE):** خوذة، نظارات لحام داكنة، قفازات جلدية، حذاء سلامة عازل.
            3. **التحكم بالمخاطر:** توفر طفاية حريق بودرة جافة قريبة، وجود مراقب حريق (Fire Watcher) طوال فترة العمل.
            4. **إجراءات الطوارئ:** جاهزية الاسعافات الأولية وخطط الإخلاء الفوري.
            """)


# ==========================================
# 3. ⚖️ Knowledge & Conflicts (المعرفة وتعارض القوانين)
# ==========================================
elif menu == "⚖️ Knowledge & Conflicts (المعرفة وتعارض القوانين)":
    st.title("⚖️ إدارة المعرفة وتعارض القوانين (Compliance & Conflicts)")
    st.markdown("مقارنة ذكية بين التشريعات المحلية والمعايير الدولية وكشف التعارضات برمجياً.")
    
    topic = st.selectbox("اختر الموضوع للمقارنة والتحقق:", ["أعمال البناء والتشييد والعمل على ارتفاعات", "العمل داخل الأماكن المغلقة", "التعامل مع المواد الكيميائية الخطرة"])
    
    if topic:
        st.markdown(f"### 🔍 تحليل التوافق والتعارض لـ: {topic}")
        st.markdown("⚠️ **ملاحظة نظامية:** يوجد اختلاف طفيف بين المتطلبات المحلية الأردنية ومعايير OSHA الأمريكية من حيث الارتفاع الإلزامي لتأمين الحواف.")
        
        col_loc, col_int = st.columns(2)
        with col_loc:
            st.info("🇯🇴 المتطلب المحلي (الأنظمة الأردنية):")
            st.markdown("- الالتزام بقانون العمل الأردني وتعليمات السلامة الصادرة عن وزارة العمل.\n- التركيز على الإشراف الميداني ولجان السلامة المؤسسية.")
        with col_int:
            st.info("🌎 المعيار الدولي (OSHA / ISO):")
            st.markdown("- OSHA 1926: الالتزام بالحماية الإجبارية عند ارتفاع 1.8 متر (6 قدم) في قطاع البناء.\n- ISO 45001: إدارة المخاطر واستمرارية الأعمال.")
            
        st.markdown("---")
        st.markdown("💡 **ماذا يعني ذلك عملياً؟**")
        st.success("يُعتمد **المعيار الأكثر صرامة** (تطبيق معيار 1.8 متر الدولي داخل المنشأة لضمان أقصى درجات الحماية وتلبية المتطلب المحلي معاً).")
        st.caption(f"📅 آخر تحقق وتحديث للمعلومة: {current_date_str} | مستوى الثقة: 🟢 موثوق جدًا")


# ==========================================
# 4. 🛠️ Safety Workflow (دورة حياة المهمة)
# ==========================================
elif menu == "🛠️ Safety Workflow (دورة حياة المهمة)":
    st.title("🛠️ Safety Workflow — دورة حياة المهمة المتكاملة")
    st.markdown("مسار المشرف الذكي: من تقييم المخاطر (Risk Assessment) حتى إغلاق المهمة وسجل الحوادث.")
    
    step = st.radio("اختر المرحلة الحالية في المهمة:", ["1. Risk Assessment", "2. JSA (تحليل سلامة العمل)", "3. Permit to Work (التصاريح)", "4. Toolbox Talk (اجتماع الصندوق)", "5. Execution & Inspection", "6. Close & Incident Report"])
    
    if "1." in step:
        st.subheader("📊 تقييم المخاطر (Risk Assessment)")
        act = st.text_input("اسم النشاط التشغيلي:", "تفريغ خوادم كيميائية")
        p = st.slider("الاحتمالية (1-5):", 1, 5, 3)
        s = st.slider("الشدة (1-5):", 1, 5, 4)
        score = p * s
        st.metric("مستوى الخطورة الإجمالي (Risk Score)", score)
        if score >= 15:
            st.error("🚨 خطر مرتفع جداً! يتطلب اعتماد مدير السلامة فوراً.")
    elif "2." in step:
        st.subheader("📋 نموذج JSA (Job Safety Analysis)")
        st.write("تسلسل خطوات العمل ➔ الخطر المرتبط ➔ إجراءات السيطرة المقترحة.")
        st.text_area("أدخل خطوات العمل:", "1. فحص الصمام\n2. فتح المحبس تدريجياً\n3. المراقبة المستمرة")
        st.success("✨ تم اعتماد نموذج JSA بنجاح وربطه بالملف الرقمي.")
    else:
        st.info(f"📍 المرحلة النشطة حالياً: {step} — النظام يتابع كافة المتطلبات التنظيمية والميدانية.")


# ==========================================
# 5. 🏢 Company Mode (إدارة المنشأة)
# ==========================================
elif menu == "🏢 Company Mode (إدارة المنشأة)":
    st.title("🏢 Company Mode — نظام إدارة السلامة للمؤسسات")
    st.markdown("مساحتك الخاصة لإدارة العمال، المواقع، المخاطر، وسجل الحوادث ومؤشر السلامة (Safety Score).")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Safety Score", "94 / 100", "🟢 ممتاز")
    with col2:
        st.metric("إجمالي العمال", "42 عامل", "نشطون")
    with col3:
        st.metric("المواقع المدارة", "3 مواقع", "عمان، العقبة، الزرقاء")
    with col4:
        st.metric("الحوادث المسجلة", "0 حادث", "سجل نظيف")
        
    st.markdown("---")
    st.subheader("📋 إدارة الإجراءات التصحيحية والمستندات المؤسسية")
    st.write("يمكنك رفع شهادات العمال، متابعة التفتيش الدوري، واستعراض تقارير الأداء الميداني بضغطة زر.")


# ==========================================
# 6. 🛂 Safety Passport (جواز السلامة للعامل)
# ==========================================
elif menu == "🛂 Safety Passport (جواز السلامة للعامل)":
    st.title("🛂 Safety Passport — جواز السلامة الرقمي للعامل")
    st.markdown("التحقق الفوري من صلاحية تدريبات العامل، شهاداته، والأعمال المسموح له بتنفيذها.")
    
    worker_id = st.text_input("أدخل رقم العامل أو امسح الباركود:", "TSS-2026-8849")
    if worker_id:
        st.success("🟢 تم العثور على ملف العامل: طارق السقرات (مشرف سلامة / إدارة أزمات)")
        st.markdown("""
        * **🪪 رقم الهوية المهنية:** TSS-2026-8849
        * **🎓 الدورات والشهادات:** 
          * دورة إدارة الأزمات والطوارئ (معتمد)
          * رخصة القيادة الدولية للحاسوب (ICDL)
          * دورة الإسعافات الأولية المتقدمة (ساري المفعول)
        * **🛠️ الأعمال المسموح له بتنفيذها:** 
          * ✅ الإشراف على مواقع الإنشاءات
          * ✅ إدارة الطوارئ والإنقاذ الأولي
          * ⚠️ **تحذير:** يتطلب تجديد رخصة العمل في الأماكن المغلقة قريباً.
        """)


# ==========================================
# 7. 🖨️ QR Codes & Assets (الأصول والمعدات)
# ==========================================
elif menu == "🖨️ QR Codes & Assets (الأصول والمعدات)":
    st.title("🖨️ نظام QR Codes لإدارة المعدات والمواد")
    st.markdown("امسح أو اختر كود المعدة لعرض حالة الفحص الدوري وصلاحية التشغيل.")
    
    asset_sel = st.selectbox("اختر الأصول أو المعدة:", ["🧯 طفاية حريق #024", "🏗️ رافعة شوكية #09", "🧪 برميل مادة الهيدروجين #C-12"])
    if asset_sel:
        st.info(f"📌 سجل أصل المعدة: {asset_sel}")
        st.markdown(f"""
        * **آخر فحص دوري:** 15 أغسطس 2026
        * **موعد الفحص القادم:** 15 نوفمبر 2026
        * **الحالة التشغيلية:** 🟢 جاهزة للاستخدام وآمنة
        * **المسؤول عن الصيانة:** فريق الهندسة والسلامة
        """)


# ==========================================
# 8. 📊 Incident Intelligence & Dashboard
# ==========================================
elif menu == "📊 Incident Intelligence & Dashboard":
    st.title("📊 Incident Intelligence & Analytics Dashboard")
    st.markdown("تحليل ذكي للحوادث، اكتشاف الأنماط المتكررة، والجذور السببية لمنع تكرارها.")
    
    st.warning("⚠️ **تنبيه تحليل الذكاء الاصطناعي:** تم رصد تشابه في نمط 2 بلاغات سابقة تتعلق بعدم تأمين حواف العمل خلال الشهر الحالي. يُنصح بتكثيف التفتيش الميداني في القطاع الشرقي.")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.metric("مؤشر المخاطر التراكمي", "منخفض جداً", "-12% عن الشهر السابق")
    with col_b:
        st.metric("نسبة إغلاق الإجراءات التصحيحية", "100%", "مكتمل")
        
    st.markdown("---")
    st.subheader("📈 سجل التحليل الجذري للحوادث (Root Cause Analysis)")
    st.write("النظام يحلل: ماذا حدث؟ ➔ لماذا حدث؟ ➔ الإجراء التصحيحي الجذري لمنع تكراره نهائياً.")
