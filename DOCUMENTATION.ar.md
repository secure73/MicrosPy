<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
    <meta charset="UTF-8">
    <style>
        body {
            direction: rtl;
            text-align: right;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        pre, code {
            direction: ltr;
            text-align: left;
            font-family: 'Consolas', 'Monaco', monospace;
        }
        .mermaid {
            direction: ltr;
        }
        .mermaid svg {
            direction: ltr;
        }
    </style>
</head>
<body>

# توثيق إطار عمل مايكرو بايثون

<div dir="rtl">

## نظرة عامة
هذا إطار عمل مصغر مصمم لتعلم أساسيات بايثون وتطوير واجهات برمجة التطبيقات RESTful. يقوم بتنفيذ بنية MVC (النموذج-العرض-المتحكم) بسيطة ويوفر وظائف واجهة برمجة التطبيقات RESTful الأساسية.

## المتطلبات الأساسية
- بايثون 3.13.2 أو أعلى
- بيئة افتراضية (موصى بها)

## التثبيت

1. استنساخ المستودع:
```bash
git clone <repository-url>
cd micro_py_framework
```

2. إنشاء وتفعيل البيئة الافتراضية:
```bash
# ويندوز
python -m venv venv
.\venv\Scripts\activate

# لينكس/ماك
python -m venv venv
source venv/bin/activate
```

3. تثبيت التبعيات:
```bash
pip install -r requirements.txt
```

## هيكل المشروع
```
micro_py_framework/
├── app.py                 # نقطة الدخول الرئيسية للتطبيق
├── controller/            # مجلد المتحكمات
│   └── UserController.py  # عمليات المستخدم
├── model/                # مجلد النماذج
│   └── UserModel.py      # عمليات بيانات المستخدم
├── table/                # جداول قاعدة البيانات
│   ├── DBConnection.py   # إدارة اتصال قاعدة البيانات
│   ├── DBMigrate.py      # ترحيل ومخطط قاعدة البيانات
│   └── UserTable.py      # مخطط جدول المستخدم
├── interface/            # مجلد الواجهات
│   └── IController.py    # واجهة المتحكم
└── helper/              # أدوات مساعدة
    ├── HttpHandler.py    # معالج طلبات HTTP
    ├── Response.py       # تنسيق الاستجابة
    ├── JWTManager.py     # المصادقة باستخدام JWT
    └── FormatCheck.py    # التحقق من صحة المدخلات
```

## تشغيل التطبيق
```bash
python app.py
```
سيبدأ الخادم على المنفذ 8001 افتراضياً.

## نقاط النهاية API

### نقاط نهاية متحكم المستخدم

1. **إنشاء مستخدم**
   - الطريقة: POST
   - الرابط: `/user`
   - جسم الطلب:
     ```json
     {
         "email": "user@example.com",
         "password": "password123",
         "name": "John Doe"
     }
     ```
   - الاستجابة: رسالة نجاح أو تفاصيل الخطأ

2. **الحصول على مستخدم**
   - الطريقة: GET
   - الرابط: `/user` (قائمة جميع المستخدمين)
   - الرابط: `/user/{id}` (الحصول على مستخدم محدد)
   - الاستجابة: بيانات المستخدم أو رسالة خطأ

3. **تحديث مستخدم**
   - الطريقة: PUT
   - الرابط: `/user`
   - جسم الطلب:
     ```json
     {
         "id": 1,
         "name": "الاسم المحدث",
         "password": "كلمة المرور الجديدة"  // اختياري
     }
     ```
   - الاستجابة: بيانات المستخدم المحدثة أو رسالة خطأ

4. **حذف مستخدم**
   - الطريقة: DELETE
   - الرابط: `/user`
   - جسم الطلب:
     ```json
     {
         "id": 1
     }
     ```
   - الاستجابة: رسالة نجاح أو تفاصيل الخطأ

## التحقق من صحة البيانات

### قواعد التحقق من صحة بيانات المستخدم
- البريد الإلكتروني: يجب أن يتبع تنسيق البريد الإلكتروني القياسي
- كلمة المرور: الحد الأدنى 6 أحرف
- الاسم: الحد الأدنى حرفين

## قاعدة البيانات

### قاعدة بيانات SQLite
- يستخدم التطبيق SQLite كقاعدة بيانات افتراضية
- ملف قاعدة البيانات: `db.db`
- يتم إنشاء الجداول تلقائياً عند التشغيل الأول

### ترحيل قاعدة البيانات (DBMigrate.py)
ملف `DBMigrate.py` مسؤول عن تهيئة قاعدة البيانات وإنشاء الجداول. يتعامل مع:

1. **اتصال قاعدة البيانات**
   - إنشاء اتصال بقاعدة بيانات SQLite (`db.db`)
   - إدارة مؤشر قاعدة البيانات لتنفيذ أوامر SQL

2. **إنشاء الجداول**
   - إنشاء الجداول المطلوبة تلقائياً إذا لم تكن موجودة
   - يدير حالياً جدولين:
     - جدول `users`:
       ```sql
       CREATE TABLE users(
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           email TEXT NOT NULL UNIQUE,
           password TEXT NOT NULL,
           name TEXT NOT NULL
       )
       ```
     - جدول `products`:
       ```sql
       CREATE TABLE products(
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           name TEXT NOT NULL UNIQUE,
           category TEXT NOT NULL,
           price FLOAT NOT NULL
       )
       ```

3. **الاستخدام**
   - يتم تشغيل الترحيل تلقائياً عند بدء التطبيق
   - يضمن أن مخطط قاعدة البيانات محدث
   - يمنع الأخطاء الناتجة عن عدم وجود الجداول

4. **الميزات**
   - يستخدم `CREATE TABLE IF NOT EXISTS` لمنع إنشاء الجداول المكررة
   - يتعامل مع المفاتيح الأساسية مع الزيادة التلقائية
   - يفرض قيود فريدة على البريد الإلكتروني وأسماء المنتجات
   - يدير الحقول المطلوبة مع قيود NOT NULL

### إدارة اتصال قاعدة البيانات (DBConnection.py)
ملف `DBConnection.py` يدير اتصالات قاعدة البيانات باستخدام SQLAlchemy ORM. يوفر:

1. **تكامل SQLAlchemy**
   - يستخدم SQLAlchemy للربط بين الكائنات والعلاقات (ORM)
   - يوفر قاعدة إعلانية لتعريف النماذج
   - يدير جلسات قاعدة البيانات بكفاءة

2. **تكوين الاتصال**
   ```python
   engine = create_engine("sqlite:///db.db", echo=False)
   ```
   - يستخدم التكوين الافتراضي قاعدة بيانات SQLite
   - يدعم MySQL/MariaDB من خلال تعديل سلسلة الاتصال
   - `echo=False` يعطل تسجيل استعلامات SQL لأداء أفضل

3. **إدارة الجلسة**
   ```python
   Session = sessionmaker(bind=engine)
   ```
   - ينشئ مصنع جلسات لعمليات قاعدة البيانات
   - يدير اتصالات ومعاملات قاعدة البيانات
   - يوفر وصولاً آمناً للخيوط لقاعدة البيانات

4. **طرق مساعدة**
   - `create_all()`: ينشئ جميع جداول قاعدة البيانات المعرفة في النماذج
   - `get_session()`: يعيد جلسة قاعدة بيانات جديدة للعمليات

5. **دعم قاعدة البيانات**
   - **SQLite** (الافتراضي):
     ```python
     engine = create_engine("sqlite:///db.db")
     ```
   - **MySQL/MariaDB**:
     ```python
     engine = create_engine("mysql+pymysql://username:password@localhost:3306/database_name")
     ```

6. **معالجة الأخطاء**
   - يلتقط ويبلغ عن فشل اتصال قاعدة البيانات
   - يوفر رسائل خطأ واضحة للتشخيص

7. **الاستخدام في النماذج**
   ```python
   from table.DBConnection import DBConnection
   
   class YourModel:
       def __init__(self):
           self.Session = DBConnection.Session
   ```

8. **أفضل الممارسات**
   - يستخدم تجميع الاتصالات لأداء أفضل
   - ينفذ إدارة جلسات مناسبة
   - يدعم عدة قواعد بيانات خلفية
   - يتبع أفضل ممارسات SQLAlchemy

### دعم MySQL
- يدعم الإطار أيضاً قواعد بيانات MySQL
- لاستخدام MySQL، قم بتعديل سلسلة الاتصال في `table/DBConnection.py`:
  ```python
  engine = create_engine("mysql+pymysql://username:password@localhost:3306/database_name")
  ```

## معالجة الأخطاء
يتضمن الإطار معالجة أخطاء أساسية لـ:
- بيانات إدخال غير صالحة
- عمليات قاعدة البيانات
- التحقق من صحة طلبات HTTP
- الموارد غير الموجودة

## ملاحظات أمنية
1. هذا إطار تعليمي ولا يوصى به للاستخدام في الإنتاج
2. تم تنفيذ تشفير كلمات المرور باستخدام bcrypt
3. يتم توفير التحقق الأساسي من المدخلات من خلال FormatCheck.py
4. يتوفر دعم المصادقة JWT من خلال JWTManager.py
5. لا يوجد نظام مصادقة/تفويض مدمج

## التحقق من صحة المدخلات
يتضمن الإطار أداة FormatCheck للتحقق من صحة بيانات الإدخال:

1. **التحقق من صحة البريد الإلكتروني**
   ```python
   FormatCheck.email("user@example.com")
   ```
   - يستخدم نمط Regex: `^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-z]+$`
   - يتحقق من:
     - جزء اسم المستخدم: أحرف، أرقام، نقاط، شرطات سفلية، علامات زائد، شرطات
     - جزء النطاق: أحرف، أرقام، شرطات
     - TLD: أحرف فقط
   - القيمة المرجعة: صحيح إذا كان صالحاً، خطأ خلاف ذلك

2. **التحقق من الطول**
   ```python
   FormatCheck.minimumLength("password", 6)
   ```
   - يتحقق مما إذا كان النص يلبي متطلبات الحد الأدنى للطول
   - المعلمات:
     - input_string: النص المراد التحقق منه
     - min_length: الحد الأدنى المطلوب للطول
   - القيمة المرجعة: صحيح إذا كان الطول >= min_length، خطأ خلاف ذلك

3. **أمثلة الاستخدام**
   ```python
   # التحقق من صحة البريد الإلكتروني
   if not FormatCheck.email(user_email):
       return Response.bad_request("تنسيق البريد الإلكتروني غير صالح")

   # التحقق من طول كلمة المرور
   if not FormatCheck.minimumLength(password, 6):
       return Response.bad_request("يجب أن تكون كلمة المرور 6 أحرف على الأقل")

   # التحقق من طول الاسم
   if not FormatCheck.minimumLength(name, 2):
       return Response.bad_request("يجب أن يكون الاسم حرفين على الأقل")
   ```

4. **قواعد التحقق**
   - البريد الإلكتروني: يجب أن يتبع تنسيق البريد الإلكتروني القياسي مع أحرف صالحة
   - كلمة المرور: الحد الأدنى 6 أحرف
   - الاسم: الحد الأدنى حرفين

## أمثلة الاستخدام

### إنشاء مستخدم جديد
```bash
curl -X POST http://localhost:8001/user \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "password123", "name": "John Doe"}'
```

### الحصول على جميع المستخدمين
```bash
curl http://localhost:8001/user
```

### الحصول على مستخدم محدد
```bash
curl http://localhost:8001/user/1
```

### تحديث مستخدم
```bash
curl -X PUT http://localhost:8001/user \
  -H "Content-Type: application/json" \
  -d '{"id": 1, "name": "الاسم المحدث"}'
```

### حذف مستخدم
```bash
curl -X DELETE http://localhost:8001/user \
  -H "Content-Type: application/json" \
  -d '{"id": 1}'
```

## إرشادات التطوير

### إنشاء متحكمات جديدة
1. إنشاء ملف جديد في مجلد `controller`
2. تنفيذ واجهة `IController`
3. إضافة طرق المتحكم (get, post, put, destroy)

### إنشاء نماذج جديدة
1. إنشاء ملف جديد في مجلد `model`
2. تنفيذ واجهة `IModel`
3. إنشاء الجدول المقابل في مجلد `table`
4. تنفيذ عمليات قاعدة البيانات

## القيود
1. لا يوجد نظام مصادقة مدمج
2. معالجة أخطاء محدودة
3. تحقق أساسي من المدخلات
4. لا يوجد تحديد لمعدل الطلبات
5. لا يوجد نظام تسجيل مدمج
6. لا يوجد آلية تخزين مؤقت مدمجة

## أفضل الممارسات
1. استخدم دائماً البيئة الافتراضية
2. حافظ على المتحكمات بسيطة، انقل المنطق إلى النماذج
3. تحقق من صحة بيانات الإدخال قبل المعالجة
4. تعامل مع أخطاء قاعدة البيانات بشكل مناسب
5. استخدم رموز حالة HTTP المناسبة في الاستجابات

## حل المشكلات
1. إذا فشل الاتصال بقاعدة البيانات:
   - تحقق من وجود ملف قاعدة البيانات
   - تحقق من بيانات اعتماد قاعدة البيانات (إذا كنت تستخدم MySQL)
   - تحقق من أذونات قاعدة البيانات

2. إذا فشل الخادم في البدء:
   - تحقق من توفر المنفذ 8001
   - تحقق من تثبيت جميع التبعيات
   - تحقق من توافق إصدار بايثون

3. إذا فشلت الطلبات:
   - تحقق من تنسيق الطلب
   - تحقق من قواعد التحقق من صحة المدخلات
   - تأكد من استخدام طريقة HTTP المناسبة

## دورة حياة طلب HTTP

### تدفق الطلب العام
```mermaid
graph TD
    A[طلب العميل] --> B[HttpHandler]
    B --> C{التحقق من صحة الطلب}
    C -->|صالح| D[التوجيه إلى المتحكم]
    C -->|غير صالح| E[إرجاع خطأ 400]
    D --> F[تنفيذ طريقة المتحكم]
    F --> G[معالجة عمليات النموذج]
    G --> H[عمليات قاعدة البيانات]
    H --> I[تنسيق الاستجابة]
    I --> J[إرسال الاستجابة إلى العميل]
```

### تدفق إنشاء المستخدم
```mermaid
sequenceDiagram
    participant Client
    participant HttpHandler
    participant UserController
    participant UserModel
    participant Database

    Client->>HttpHandler: POST /user
    Note over HttpHandler: التحقق من صحة الطلب
    HttpHandler->>UserController: التوجيه إلى المتحكم
    UserController->>UserModel: create()
    UserModel->>UserModel: التحقق من صحة البريد الإلكتروني
    UserModel->>UserModel: تشفير كلمة المرور
    UserModel->>Database: استعلام INSERT
    Database-->>UserModel: نجاح
    UserModel-->>UserController: نجاح
    UserController-->>HttpHandler: 200 OK
    HttpHandler-->>Client: الاستجابة
```

### تدفق معالجة الأخطاء
```mermaid
graph TD
    A[حدوث خطأ] --> B{نوع الخطأ}
    B -->|التحقق| C[تنسيق خطأ التحقق]
    B -->|قاعدة البيانات| D[تنسيق خطأ قاعدة البيانات]
    B -->|غير موجود| E[تنسيق خطأ 404]
    C --> F[تعيين رمز حالة الخطأ]
    D --> F
    E --> F
    F --> G[إرسال استجابة الخطأ]
```

### تفاعل المكونات
```mermaid
graph LR
    A[HttpHandler] -->|يوجه| B[المتحكمات]
    B -->|يستخدم| C[النماذج]
    C -->|يتفاعل| D[قاعدة البيانات]
    B -->|ينفذ| E[واجهة IController]
    C -->|ينفذ| F[واجهة IModel]
    D -->|يدار بواسطة| G[DBConnection]
    D -->|المخطط بواسطة| H[DBMigrate]
```

## معالجة الاستجابة

### فئة الاستجابة (helper/Response.py)
توفر فئة `Response` طريقة موحدة لتنسيق استجابات API. تضمن هيكل استجابة متناسق عبر جميع نقاط النهاية.

#### هيكل الاستجابة
```json
{
    "status_code": 200,      // رمز حالة HTTP
    "status": "success",     // "success" أو "error"
    "message": {}            // بيانات الاستجابة أو رسالة الخطأ
}
```

#### الطرق المتاحة

1. **طريقة الاستجابة الأساسية**
   ```python
   @staticmethod
   def response(status_code, data)
   ```
   - ينشئ كائن استجابة موحد
   - يحدد الحالة تلقائياً بناءً على رمز الحالة
   - يتم تمييز رموز الحالة >= 400 كـ "error"
   - يتم تمييز رموز الحالة < 400 كـ "success"

2. **استجابة النجاح**
   ```python
   @staticmethod
   def success(data)
   ```
   - يعيد استجابة 200 OK
   - يستخدم للعمليات الناجحة
   - مثال:
     ```python
     Response.success({"user": "created"})
     # يعيد:
     # {
     #     "status_code": 200,
     #     "status": "success",
     #     "message": {"user": "created"}
     # }
     ```

3. **استجابة طلب غير صالح**
   ```python
   @staticmethod
   def bad_request(message)
   ```
   - يعيد استجابة 400 Bad Request
   - يستخدم لأخطاء التحقق أو المدخلات غير الصالحة
   - مثال:
     ```python
     Response.bad_request("تنسيق البريد الإلكتروني غير صالح")
     # يعيد:
     # {
     #     "status_code": 400,
     #     "status": "error",
     #     "message": "تنسيق البريد الإلكتروني غير صالح"
     # }
     ```

4. **استجابة غير مصرح**
   ```python
   @staticmethod
   def unauthorized(message)
   ```
   - يعيد استجابة 401 Unauthorized
   - يستخدم لفشل المصادقة
   - مثال:
     ```python
     Response.unauthorized("بيانات الاعتماد غير صالحة")
     # يعيد:
     # {
     #     "status_code": 401,
     #     "status": "error",
     #     "message": "بيانات الاعتماد غير صالحة"
     # }
     ```

5. **استجابة خطأ داخلي**
   ```python
   @staticmethod
   def internal_error(message)
   ```
   - يعيد استجابة 500 Internal Server Error
   - يستخدم لأخطاء جانب الخادم
   - مثال:
     ```python
     Response.internal_error("فشل الاتصال بقاعدة البيانات")
     # يعيد:
     # {
     #     "status_code": 500,
     #     "status": "error",
     #     "message": "فشل الاتصال بقاعدة البيانات"
     # }
     ```

#### أمثلة الاستخدام

1. **في المتحكمات**
   ```python
   def post(self, data):
       try:
           # معالجة البيانات
           return Response.success({"message": "تم الإنشاء بنجاح"})
       except ValidationError:
           return Response.bad_request("مدخلات غير صالحة")
       except Exception:
           return Response.internal_error("خطأ في الخادم")
   ```

2. **معالجة الأخطاء**
   ```python
   if not user_data:
       return Response.bad_request("لم يتم العثور على المستخدم")
   ```

3. **استجابة النجاح**
   ```python
   return Response.success({
       "user": {
           "id": 1,
           "name": "John Doe",
           "email": "john@example.com"
       }
   })
   ```

#### أفضل الممارسات
1. استخدم دائماً فئة Response لاستجابات API متناسقة
2. استخدم رموز حالة مناسبة لسيناريوهات مختلفة
3. قدم رسائل خطأ واضحة ووصفية
4. حافظ على هيكل بيانات الاستجابة متناسقاً
5. استخدم success() للعمليات الناجحة
6. استخدم طرق خطأ محددة (bad_request, unauthorized, internal_error) لأنواع مختلفة من الأخطاء

## المصادقة

### المصادقة باستخدام JWT (helper/JWTManager.py)
يتضمن الإطار دعم JWT (JSON Web Token) للمصادقة:

1. **إنشاء الرمز**
   ```python
   jwt_manager = JWTManager()
   token = jwt_manager.create({"user_id": 123, "role": "admin"})
   ```
   - ينشئ رموز JWT مع انتهاء الصلاحية
   - انتهاء الصلاحية الافتراضي: 60 دقيقة
   - يستخدم خوارزمية HS256
   - يضيف تلقائياً الطابع الزمني لانتهاء الصلاحية

2. **التحقق من الرمز**
   ```python
   decoded = jwt_manager.verify(token)
   if decoded:
       # الرمز صالح
       user_data = decoded
   else:
       # الرمز غير صالح أو منتهي الصلاحية
   ```
   - يتحقق من صحة الرمز
   - يتحقق من انتهاء الصلاحية
   - يعيد البيانات المفكوكة أو False

3. **التكوين**
   ```python
   self.__secret_key = "مفتاحك السري"
   self.__algorithm = "HS256"
   self.__expiration_minutes = 60
   ```
   - مفتاح سري قابل للتكوين
   - خوارزمية قابلة للتكوين
   - وقت انتهاء الصلاحية قابل للتكوين

4. **مثال الاستخدام**
   ```python
   # إنشاء رمز
   jwt_manager = JWTManager()
   user_data = {"user_id": 123, "role": "admin"}
   token = jwt_manager.create(user_data)

   # التحقق من الرمز
   decoded = jwt_manager.verify(token)
   if decoded:
       print("البيانات المفكوكة:", decoded)
   ```

5. **ملاحظات أمنية**
   - يجب تخزين المفتاح السري في متغيرات البيئة
   - تنتهي صلاحية الرموز بعد 60 دقيقة افتراضياً
   - يستخدم خوارزمية HS256 القياسية في الصناعة
   - يتعامل مع انتهاء صلاحية الرمز بشكل مناسب

</div> 