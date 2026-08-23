<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Safety - نظام إدارة السلامة والطوارئ الذكي</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;600;700;900&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Cairo', sans-serif;
        }
        .glass-card {
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
    </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen selection:bg-cyan-500 selection:text-white">

    <!-- Navbar -->
    <header class="fixed top-0 left-0 right-0 z-50 glass-card border-b border-slate-800/50">
        <div class="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between">
            <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-cyan-500 to-blue-600 flex items-center justify-center shadow-lg shadow-cyan-500/30">
                    <i class="fa-solid fa-shield-halved text-white text-lg"></i>
                </div>
                <span class="text-2xl font-black tracking-wider bg-gradient-to-r from-cyan-400 to-blue-500 bg-clip-text text-transparent">Safety</span>
            </div>
            
            <nav class="hidden md:flex items-center gap-8 text-sm font-medium text-slate-300">
                <a href="#features" class="hover:text-cyan-400 transition">الميزات</a>
                <a href="#ai-assistant" class="hover:text-cyan-400 transition">المساعد الذكي</a>
                <a href="#tools" class="hover:text-cyan-400 transition">الأدوات الميدانية</a>
                <a href="#contact" class="hover:text-cyan-400 transition">اتصل بنا</a>
            </nav>

            <div class="flex items-center gap-4">
                <a href="#" class="hidden sm:inline-block text-sm font-semibold text-slate-300 hover:text-white px-4 py-2 transition">تسجيل الدخول</a>
                <a href="#" class="bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-400 hover:to-blue-500 text-white text-sm font-bold px-6 py-2.5 rounded-xl shadow-lg shadow-cyan-500/20 transition transform hover:-translate-y-0.5">ابدأ الاستخدام</a>
            </div>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="relative pt-32 pb-20 md:pt-44 md:pb-32 overflow-hidden">
        <!-- Background Glow -->
        <div class="absolute top-1/4 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[500px] h-[500px] bg-cyan-500/10 blur-[120px] rounded-full pointer-events-none"></div>
        <div class="absolute top-1/3 right-1/4 w-[400px] h-[400px] bg-blue-600/10 blur-[100px] rounded-full pointer-events-none"></div>

        <div class="max-w-7xl mx-auto px-6 text-center relative z-10">
            <div class="inline-flex items-center gap-2 px-4 py-2 rounded-full glass-card border border-cyan-500/20 text-cyan-400 text-xs font-semibold mb-6">
                <i class="fa-solid fa-bolt text-xs"></i>
                <span>الجيل القادم من أنظمة إدارة السلامة والطوارئ</span>
            </div>
            
            <h1 class="text-4xl md:text-6xl lg:text-7xl font-black tracking-tight leading-tight max-w-4xl mx-auto mb-8">
                مستقبلك الميداني الآمن يبدأ من هنا: <span class="bg-gradient-to-r from-cyan-400 via-blue-500 to-indigo-500 bg-clip-text text-transparent">نظام ذكي للسلامة</span>
            </h1>
            
            <p class="text-lg md:text-xl text-slate-400 max-w-2xl mx-auto mb-10 font-light leading-relaxed">
                منصة متكاملة تجمع التشريعات، أدوات تقييم المخاطر، والمساعد الذكي لدعم صناع القرار ومسؤولي السلامة في الميدان بكفاءة عالية.
            </p>

            <div class="flex flex-col sm:flex-row items-center justify-center gap-4">
                <a href="#" class="w-full sm:w-auto bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-400 hover:to-blue-500 text-white font-bold px-8 py-4 rounded-xl shadow-xl shadow-cyan-500/25 transition transform hover:-translate-y-1 flex items-center justify-center gap-3">
                    <span>استكشف الأدوات الميدانية</span>
                    <i class="fa-solid fa-arrow-left text-sm"></i>
                </a>
                <a href="#" class="w-full sm:w-auto glass-card hover:bg-white/10 text-white font-bold px-8 py-4 rounded-xl transition flex items-center justify-center gap-3 border border-slate-700">
                    <i class="fa-solid fa-wand-magic-sparkles text-cyan-400"></i>
                    <span>تجربة المساعد الذكي</span>
                </a>
            </div>

            <!-- Stats Bar -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 max-w-4xl mx-auto mt-20">
                <div class="glass-card p-6 rounded-2xl border border-slate-800">
                    <h3 class="text-3xl font-black text-cyan-400 mb-1">+99%</h3>
                    <p class="text-sm text-slate-400">دقة عالية في تقييم المخاطر الميدانية</p>
                </div>
                <div class="glass-card p-6 rounded-2xl border border-slate-800">
                    <h3 class="text-3xl font-black text-blue-400 mb-1">استجابة فورية</h3>
                    <p class="text-sm text-slate-400">للأزمات وحالات الطوارئ المهنية</p>
                </div>
                <div class="glass-card p-6 rounded-2xl border border-slate-800">
                    <h3 class="text-3xl font-black text-indigo-400 mb-1">مرجع معتمد</h3>
                    <p class="text-sm text-slate-400">لأحدث التشريعات والمعايير الدولية</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Features Section -->
    <section id="features" class="py-24 bg-slate-900/50 border-t border-slate-900">
        <div class="max-w-7xl mx-auto px-6">
            <div class="text-center max-w-2xl mx-auto mb-16">
                <h2 class="text-3xl md:text-4xl font-bold mb-4">مميزات مصممة خصيصاً للميدان</h2>
                <p class="text-slate-400">كل ما تحتاجه لإدارة السلامة العامة والكوارث في منصة واحدة متطورة.</p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
                <!-- Feature 1 -->
                <div class="glass-card p-8 rounded-3xl hover:border-cyan-500/50 transition duration-300 group">
                    <div class="w-14 h-14 rounded-2xl bg-cyan-500/10 text-cyan-400 flex items-center justify-center text-2xl mb-6 group-hover:scale-110 transition duration-300">
                        <i class="fa-solid fa-robot"></i>
                    </div>
                    <h3 class="text-xl font-bold mb-3">المساعد الذكي</h3>
                    <p class="text-slate-400 text-sm leading-relaxed">إجابات فورية واستشارات دقيقة للتعامل الفوري مع أي طارئ ميداني بناءً على البروتوكولات المعتمدة.</p>
                </div>

                <!-- Feature 2 -->
                <div class="glass-card p-8 rounded-3xl hover:border-blue-500/50 transition duration-300 group">
                    <div class="w-14 h-14 rounded-2xl bg-blue-500/10 text-blue-400 flex items-center justify-center text-2xl mb-6 group-hover:scale-110 transition duration-300">
                        <i class="fa-solid fa-list-check"></i>
                    </div>
                    <h3 class="text-xl font-bold mb-3">قوائم التدقيق</h3>
                    <p class="text-slate-400 text-sm leading-relaxed">قوائم فحص رقمية جاهزة لعمليات التفتيش والمتابعة اليومية لضمان الامتثال لشروط السلامة العامة.</p>
                </div>

                <!-- Feature 3 -->
                <div class="glass-card p-8 rounded-3xl hover:border-indigo-500/50 transition duration-300 group">
                    <div class="w-14 h-14 rounded-2xl bg-indigo-500/10 text-indigo-400 flex items-center justify-center text-2xl mb-6 group-hover:scale-110 transition duration-300">
                        <i class="fa-solid fa-calculator"></i>
                    </div>
                    <h3 class="text-xl font-bold mb-3">حاسبة المخاطر</h3>
                    <p class="text-slate-400 text-sm leading-relaxed">أدوات حسابية متطورة لتقييم مستويات التهديد والخطورة وتحديد أولويات المعالجة والتدخل.</p>
                </div>

                <!-- Feature 4 -->
                <div class="glass-card p-8 rounded-3xl hover:border-teal-500/50 transition duration-300 group">
                    <div class="w-14 h-14 rounded-2xl bg-teal-500/10 text-teal-400 flex items-center justify-center text-2xl mb-6 group-hover:scale-110 transition duration-300">
                        <i class="fa-solid fa-book-bookmark"></i>
                    </div>
                    <h3 class="text-xl font-bold mb-3">المكتبة الشاملة</h3>
                    <p class="text-slate-400 text-sm leading-relaxed">أرشيف ضخم يضم القوانين، اللوائح التنفيذية، وإرشادات السلامة والصحة المهنية وإدارة الكوارث.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="py-12 border-t border-slate-900 bg-slate-950 text-center text-slate-500 text-sm">
        <div class="max-w-7xl mx-auto px-6 flex flex-col md:flex-row items-center justify-between gap-6">
            <div class="flex items-center gap-3">
                <div class="w-8 h-8 rounded-lg bg-cyan-500 flex items-center justify-center text-white font-bold text-sm">S</div>
                <span class="text-white font-bold text-lg">Safety Platform</span>
            </div>
            <p>جميع حقوق الطبع والنشر محفوظة © 2026</p>
            <div class="flex gap-6 text-slate-400">
                <a href="#" class="hover:text-cyan-400 transition"><i class="fa-brands fa-twitter"></i></a>
                <a href="#" class="hover:text-cyan-400 transition"><i class="fa-brands fa-linkedin"></i></a>
                <a href="#" class="hover:text-cyan-400 transition"><i class="fa-brands fa-github"></i></a>
            </div>
        </div>
    </footer>

</body>
</html>
