# 🍽️ مطعم الأصيل - نظام الكاشير
## Restaurant POS System

**Designed by: A7MED ASHRAF**  
📞 **01080343968**  
🌐 [https://a7medashraftarekh-cpu.github.io/A7MED-ASHRAF/](https://a7medashraftarekh-cpu.github.io/A7MED-ASHRAF/)

---

## 📦 محتويات المجلد

```
Restaurant_POS_A7MED_ASHRAF/
├── Windows/
│   ├── restaurant_pos.py      ← نسخة ويندوز (Python)
│   └── build_exe.bat          ← سكريبت بناء ملف EXE
├── Android/
│   ├── main.py                ← نسخة أندرويد (Kivy)
│   └── buildozer.spec         ← إعدادات بناء APK
├── build_android.sh           ← سكريبت بناء APK (Linux)
└── README.md                  ← هذا الملف
```

---

## 🖥️ تشغيل نسخة الويندوز

### الطريقة 1: تشغيل مباشر (بدون بناء)
1. تأكد من تثبيت [Python 3.8+](https://python.org)
2. افتح Command Prompt في مجلد `Windows`
3. شغل:
```bash
python restaurant_pos.py
```

### الطريقة 2: بناء ملف EXE
1. افتح `build_exe.bat` كـ Administrator
2. انتظر حتى ينتهي البناء
3. الملف النهائي هيكون في: `dist/Restaurant_POS_A7MED_ASHRAF.exe`

> 💡 **ملاحظة:** أول مرة تشغل هيتم إنشاء قاعدة بيانات SQLite مع 20 منتج تجريبي.

---

## 📱 بناء نسخة الأندرويد (APK)

### المتطلبات
- نظام Linux (Ubuntu موصى به)
- Python 3.8+
- 4GB+ مساحة فارغة

### خطوات البناء
```bash
# 1. امنح صلاحية التنفيذ
chmod +x build_android.sh

# 2. شغل سكريبت البناء
./build_android.sh
```

أو يدوياً:
```bash
cd Android
pip3 install buildozer cython
buildozer android debug
```

ملف APK هيتم إنشاؤه في: `Android/bin/`

---

## ✅ المميزات

| الميزة | الوصف |
|--------|-------|
| 🍽️ قائمة منتجات | مقسمة لفئات (أطباق رئيسية، مقبلات، مشروبات، حلويات) |
| 🛒 سلة طلبات | إضافة/حذف منتجات بنقرة واحدة |
| 📋 إدارة الطاولات | رقم الطاولة قابل للتغيير |
| 💰 حساب تلقائي | المجموع + الضريبة (14%) + الإجمالي |
| 💾 حفظ الطلبات | في قاعدة بيانات SQLite محلية |
| 🖨️ طباعة فواتير | نموذج فاتورة ضريبية مبسطة |
| 📱 تصميم متجاوب | يتكيف مع مختلف أحجام الشاشات |

---

## 🎨 التصميم

**تم التصميم بواسطة:** [A7MED ASHRAF](https://a7medashraftarekh-cpu.github.io/A7MED-ASHRAF/)  
**للتواصل:** 📞 01080343968

---

## 📄 الترخيص

هذا المشروع مفتوح المصدر للاستخدام الشخصي والتجاري.  
يرجى الإشارة إلى المصمم عند إعادة الاستخدام.

---

<div align="center">
  <b>شكراً لاستخدام نظام الكاشير!</b>
</div>
