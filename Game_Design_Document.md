
# 🔥 DESERT STRIKE: ELITE SQUAD
## وثيقة تصميم اللعبة (Game Design Document)

---

## 🎮 نظرة عامة
- **النوع**: Battle Royale / Third-Person Shooter
- **المنصات**: PC, Mobile (Android/iOS)
- **عدد اللاعبين**: 50 لاعب في المباراة الواحدة
- **مدة المباراة**: 10-15 دقيقة
- **المحرك**: Unity 3D / Unreal Engine 5
- **النمط الفني**: Realistic Stylized (مشابه لـ Free Fire)

---

## 👤 الشخصيات (Characters) - 8 شخصيات

### 1. 🔵 THE ARCHITECT (المهندس) - الشخصية الأقوى
**الصورة**: og-image.png (الشخص بالبدلة الزرقاء)
**الدور**: Builder / Support
**الصعوبة**: ⭐⭐⭐⭐⭐

**المهارات:**
- **Passive - Quick Builder**: بناء الجدران أسرع 50% من الشخصيات الأخرى
- **Active - Fortress Wall**: ينشئ جداراً حديدياً ضخماً (3000 HP) يحمي الفريق لمدة 30 ثانية
- **Active - Turret Deploy**: ينشر برجاً آليًا يطلق النار على الأعداء (100 damage/sec)
- **Ultimate - Mega Fortress**: يبني قلعة كاملة من 8 جدران + 2 برج + بوابة، تدوم 60 ثانية
- **Passive - Resource Master**: يجمع الموارد بنسبة 200% من العادي

**الإحصائيات:**
- HP: 250
- Speed: 85
- Armor: 120

---

### 2. 🟤 THE SNIPER (القناص)
**الصورة**: الصورة الأولى (الشخص بالجاكيت البني)
**الدور**: Long Range / Recon
**الصعوبة**: ⭐⭐⭐⭐

**المهارات:**
- **Passive - Eagle Eye**: رؤية الأعداء من مسافة 200m على الخريطة
- **Active - Invisibility Cloak**: يختفي تماماً لمدة 8 ثواني (لا يمكن رؤيته بالعين المجردة)
- **Active - Precision Shot**: الطلقة التالية تسبب ضعف الضرر + تخترق الدرع
- **Ultimate - Airstrike**: يستدعي غارة جوية على منطقة محددة (500 damage/sec لمدة 5 ثواني)

**الإحصائيات:**
- HP: 180
- Speed: 100
- Armor: 80

---

### 3. ⚽ THE STRIKER (المهاجم)
**الصورة**: images(16).jpeg (ميسي)
**الدور**: Assault / Frontline
**الصعوبة**: ⭐⭐⭐

**المهارات:**
- **Passive - Dribble**: يتحرك بسرعة 150% لمدة 3 ثواني بعد كل قتل
- **Active - Power Kick**: ركل قنبلة دخانية بعيداً أو ركل العدو لمسافة 10m
- **Active - Team Spirit**: يعطي كل زملائه درع مؤقت (150 HP) لمدة 20 ثانية
- **Ultimate - Golden Goal**: يصبح محصناً تماماً لمدة 5 ثواني وضرباته تسبب 300% ضرر

**الإحصائيات:**
- HP: 220
- Speed: 110
- Armor: 100

---

### 4. 📚 THE SCHOLAR (الطالب)
**الصورة**: Screenshot_٢٠٢٥١١٢٣ (كريم - بعد 3 ساعات دراسة)
**الدور**: Tactician / Intel
**الصعوبة**: ⭐⭐⭐⭐

**المهارات:**
- **Passive - Fast Learner**: يتعلم مواقع الأسلحة والمعدات بشكل أسرع
- **Active - Study Break**: يستعيد 50% من HP خلال 5 ثواني (لا يمكن التحرك)
- **Active - Cheat Sheet**: يكشف مواقع جميع الأعداء لمدة 5 ثواني
- **Ultimate - Exam Mode**: يصبح ذكاء اصطناعياً يتنبأ بحركات الأعداء ويُظهر مساراتهم المستقبلية

**الإحصائيات:**
- HP: 150
- Speed: 95
- Armor: 60

---

### 5. 🏃 THE RUNNER (العداء)
**الصورة**: Screenshot_٢٠٢٥١٠٢٨ (الطفل الصغير)
**الدور**: Scout / Flanker
**الصعوبة**: ⭐⭐

**المهارات:**
- **Passive - Speed Demon**: أسرع شخصية في اللعبة (Speed: 130)
- **Active - Sprint**: يزيد السرعة إلى 200% لمدة 5 ثواني
- **Active - Slide**: ينزلق تحت الجدران ويتجنب الرصاص
- **Ultimate - Time Freeze**: يتجمد الزمن حوله لمدة 3 ثواني (يمكن التحرك بحرية)

**الإحصائيات:**
- HP: 140
- Speed: 130
- Armor: 50

---

### 6. 💪 THE BODYBUILDER (الرياضي)
**الصورة**: Screenshot_٢٠٢٥١٠١٩ (الشخص يكتب)
**الدور**: Tank / Brawler
**الصعوبة**: ⭐⭐⭐

**المهارات:**
- **Passive - Iron Muscles**: يقلل الضرر الوارد بنسبة 30%
- **Active - Ground Slam**: يضرب الأرض فيسبب صدمة تُطير الأعداء (100 damage + stun 2s)
- **Active - Adrenaline Rush**: يزيد HP بنسبة 50% لمدة 10 ثواني
- **Ultimate - Beast Mode**: يصبح عملاقاً (ضعف الحجم) مع 500% HP و200% ضرر لمدة 15 ثانية

**الإحصائيات:**
- HP: 300
- Speed: 70
- Armor: 150

---

### 7. 🎓 THE PROFESSOR (الدكتور)
**الصورة**: Screenshot_٢٠٢٥٠٨١٥ (Dr Muhammad Ayman)
**الدور**: Support / Healer
**الصعوبة**: ⭐⭐⭐⭐

**المهارات:**
- **Passive - Knowledge Share**: يعطي XP إضافية للفريق
- **Active - Healing Drone**: ينشر طائرة بدون طيار تعالج الزملاء (50 HP/sec)
- **Active - Shield Generator**: يخلق قبة واقية (2000 HP) حول الفريق
- **Ultimate - Resurrection**: يعيد زميلاً واحداً للحياة مع كامل معداته

**الإحصائيات:**
- HP: 200
- Speed: 90
- Armor: 90

---

### 8. 🛡️ THE VETERAN (المحارب القديم)
**الصورة**: Screenshot_٢٠٢٥٠٦١٨ (الشخص في المطار)
**الدور**: All-Rounder
**الصعوبة**: ⭐⭐⭐

**المهارات:**
- **Passive - Battle Hardened**: يتعافى تلقائياً من الضرر (5 HP/sec)
- **Active - Flashbang**: قنبلة تُعمي الأعداء لمدة 4 ثواني
- **Active - Tactical Roll**: قفزة جانبية تتجنب الرصاص
- **Ultimate - War Cry**: يُخيف الأعداء القريبين (يُبطئهم 50% ويُقلل دقتهم) + يُحفز الفريق

**الإحصائيات:**
- HP: 230
- Speed: 95
- Armor: 110

---

## 🔫 نظام الأسلحة

### الأسلحة الخفيفة (SMG)
| السلاح | الضرر | معدل النيران | المجال |
|--------|-------|-------------|--------|
| MP5 | 25 | 800 RPM | 50m |
| UZI | 20 | 1000 RPM | 30m |
| Vector | 22 | 900 RPM | 40m |

### البنادق الهجومية (AR)
| السلاح | الضرر | معدل النيران | المجال |
|--------|-------|-------------|--------|
| M416 | 35 | 600 RPM | 100m |
| AK-47 | 42 | 550 RPM | 120m |
| SCAR-L | 38 | 580 RPM | 110m |

### القناصات (Sniper)
| السلاح | الضرر | معدل النيران | المجال |
|--------|-------|-------------|--------|
| AWM | 120 | 30 RPM | 500m |
| Kar98k | 95 | 40 RPM | 400m |
| M24 | 105 | 35 RPM | 450m |

### الشوتغن
| السلاح | الضرر | معدل النيران | المجال |
|--------|-------|-------------|--------|
| S12K | 150 | 120 RPM | 15m |
| M1887 | 200 | 60 RPM | 20m |

### المسدسات
| السلاح | الضرر | معدل النيران | المجال |
|--------|-------|-------------|--------|
| Desert Eagle | 55 | 200 RPM | 50m |
| Glock | 25 | 400 RPM | 30m |

---

## 🎒 المعدات

### الدرع (Armor)
- **Level 1**: +50 HP
- **Level 2**: +100 HP
- **Level 3**: +150 HP
- **Level 4 (Legendary)**: +200 HP + تقليل ضرر 10%

### الخوذة (Helmet)
- **Level 1**: تقليل ضرر الرأس 30%
- **Level 2**: تقليل ضرر الرأس 40%
- **Level 3**: تقليل ضرر الرأس 55%

### الظهر (Backpack)
- **Level 1**: 150 سعة
- **Level 2**: 200 سعة
- **Level 3**: 250 سعة

### المستلزمات الطبية
- **Bandage**: +15 HP (يصل حتى 75%)
- **First Aid Kit**: +75 HP (يصل حتى 100%)
- **Med Kit**: +100 HP كامل
- **Energy Drink**: +40 Energy (يزيد السرعة تدريجياً)
- **Painkiller**: +60 Energy
- **Adrenaline Syringe**: +100 Energy + Speed Boost

### القنابل
- **Frag Grenade**: 200 damage, نطاق 5m
- **Smoke Grenade**: دخان يخفي الرؤية لمدة 30 ثانية
- **Flashbang**: عمى لمدة 5 ثواني
- **Molotov**: حريق يستمر 10 ثواني (50 damage/sec)

---

## 🗺️ الخريطة - "Desert Storm"

### المناطق الرئيسية (8 مناطق)
1. **The Citadel** (وسط) - أعلى مخاطر، أفضل غنائم
2. **Abandoned Airport** (شمال) - مباني طويلة، قتال متوسط المدى
3. **Oil Refinery** (شرق) - أنابيب ومخازن، قتال قريب
4. **Ghost Town** (غرب) - مباني منخفضة، sniper paradise
5. **Military Base** (جنوب) - أفضل أسلحة، أعلى مخاطر
6. **Oasis** (شمال غرب) - غطاء طبيعي، stealth
7. **Radio Tower** (شمال شرق) - أعلى نقطة، sniper nest
8. **Underground Bunker** (تحت الأرض) - loot سري، قتال ضيق

### نظام المنطقة الآمنة
- الدائرة الأولى: 3 دقائق بعد البداية
- تقلص تدريجي كل 90 ثانية
- الضرر خارج الدائرة: 1 HP/sec → 5 HP/sec → 10 HP/sec

---

## 🎵 نظام الصوت

### الموسيقى
- **Lobby**: Epic orchestral + electronic
- **Parachute**: Tense, ambient
- **Early Game**: Stealth, minimal
- **Mid Game**: Building tension
- **Late Game**: Intense, heartbeat rhythm
- **Victory**: Triumphant, celebratory

### Sound Effects
- Footsteps (different surfaces)
- Gun sounds (realistic with distance attenuation)
- Vehicle engines
- Environment (wind, sand, explosions)

---

## 📱 واجهة المستخدم (UI)

### HUD Elements
- Minimap (top-right)
- HP Bar (bottom-center)
- Armor Bar (above HP)
- Ammo Count (bottom-right)
- Weapon Slots (bottom)
- Teammate Status (left)
- Kill Feed (top-right)
- Zone Timer (top-center)

### Controls (Mobile)
- Left Joystick: Movement
- Right Joystick: Aim
- Buttons: Shoot, Jump, Crouch, Prone, Reload, Use Skill
- Quick Chat Wheel

---

## 💰 نظام التقدم

### الرتب (Ranks)
1. Bronze (I-V)
2. Silver (I-V)
3. Gold (I-V)
4. Platinum (I-V)
5. Diamond (I-V)
6. Heroic
7. Grandmaster (Top 300)

### المكافآت
- **Daily**: Coins, XP, Crates
- **Weekly**: Skins, Characters
- **Seasonal**: Exclusive Legendary Items

### المتجر
- Characters (Gold/Diamonds)
- Weapon Skins
- Vehicle Skins
- Emotes
- Parachutes
- Backpacks

---

## 🚀 خارطة الطريق (Roadmap)

### المرحلة 1 (شهر 1-3)
- Core gameplay loop
- 3 Characters
- 1 Map
- Basic weapons

### المرحلة 2 (شهر 4-6)
- All 8 Characters
- Ranked Mode
- Clan System
- Season 1

### المرحلة 3 (شهر 7-12)
- New Maps
- Vehicles
- Battle Pass
- Esports Mode

---

## 🎯 أهداف التصميم
1. **Accessibility**: سهلة التعلم، صعبة الإتقان
2. **Fairness**: لا pay-to-win (جميع الشخصيات متاحة بالذهب)
3. **Performance**: 60 FPS على أجهزة متوسطة
4. **Social**: فرق 4 لاعبين + voice chat
5. **Competitive**: نظام رتب عادل + anti-cheat

---

**تم التصميم بواسطة: Game Design AI**
**التاريخ: 2026**
