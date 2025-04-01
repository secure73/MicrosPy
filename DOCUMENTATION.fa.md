<style> body { direction: rtl; text-align: right; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; } pre, code { direction: ltr; text-align: left; font-family: 'Consolas', 'Monaco', monospace; } .mermaid { direction: ltr; } .mermaid svg { direction: ltr; } </style>

# مستندات فریمورک میکرو پایتون

## نمای کلی
این یک فریمورک میکرو است که برای یادگیری اصول اولیه پایتون و توسعه API های RESTful طراحی شده است. این فریمورک یک معماری MVC (مدل-نمایش-کنترلر) ساده را پیاده‌سازی می‌کند و قابلیت‌های پایه API های RESTful را فراهم می‌کند.

## پیش‌نیازها
- پایتون 3.13.2 یا بالاتر
- محیط مجازی (توصیه شده)

## نصب

1. کلون کردن مخزن:
```bash
git clone <repository-url>
cd micro_py_framework
```

2. ایجاد و فعال‌سازی محیط مجازی:
```bash
# ویندوز
python -m venv venv
.\venv\Scripts\activate

# لینوکس/مک
python -m venv venv
source venv/bin/activate
```

3. نصب وابستگی‌ها:
```bash
pip install -r requirements.txt
```

## ساختار پروژه
```
micro_py_framework/
├── app.py                 # نقطه ورود اصلی برنامه
├── controller/            # پوشه کنترلرها
│   └── UserController.py  # عملیات مربوط به کاربر
├── model/                # پوشه مدل‌ها
│   └── UserModel.py      # عملیات داده‌های کاربر
├── table/                # جداول پایگاه داده
│   ├── DBConnection.py   # مدیریت اتصال پایگاه داده
│   ├── DBMigrate.py      # مهاجرت و طرح پایگاه داده
│   └── UserTable.py      # طرح جدول کاربر
├── interface/            # پوشه رابط‌ها
│   └── IController.py    # رابط کنترلر
└── helper/              # ابزارهای کمکی
    ├── HttpHandler.py    # پردازنده درخواست‌های HTTP
    ├── Response.py       # فرمت‌بندی پاسخ
    ├── JWTManager.py     # احراز هویت JWT
    └── FormatCheck.py    # اعتبارسنجی ورودی
```

## اجرای برنامه
```bash
python app.py
```
سرور به طور پیش‌فرض روی پورت 8001 اجرا می‌شود.

## نقاط پایانی API

### نقاط پایانی کنترلر کاربر

1. **ایجاد کاربر**
   - متد: POST
   - URL: `/user`
   - بدنه درخواست:
     ```json
     {
         "email": "user@example.com",
         "password": "password123",
         "name": "John Doe"
     }
     ```
   - پاسخ: پیام موفقیت یا جزئیات خطا

2. **دریافت کاربر**
   - متد: GET
   - URL: `/user` (لیست تمام کاربران)
   - URL: `/user/{id}` (دریافت کاربر خاص)
   - پاسخ: داده‌های کاربر یا پیام خطا

3. **به‌روزرسانی کاربر**
   - متد: PUT
   - URL: `/user`
   - بدنه درخواست:
     ```json
     {
         "id": 1,
         "name": "نام به‌روز شده",
         "password": "رمز جدید"  // اختیاری
     }
     ```
   - پاسخ: داده‌های به‌روز شده کاربر یا پیام خطا

4. **حذف کاربر**
   - متد: DELETE
   - URL: `/user`
   - بدنه درخواست:
     ```json
     {
         "id": 1
     }
     ```
   - پاسخ: پیام موفقیت یا جزئیات خطا

## اعتبارسنجی داده‌ها

### قوانین اعتبارسنجی داده‌های کاربر
- ایمیل: باید مطابق با فرمت استاندارد ایمیل باشد
- رمز عبور: حداقل 6 کاراکتر
- نام: حداقل 2 کاراکتر

## پایگاه داده

### پایگاه داده SQLite
- برنامه به طور پیش‌فرض از SQLite به عنوان پایگاه داده استفاده می‌کند
- فایل پایگاه داده: `db.db`
- جداول در اولین اجرا به طور خودکار ایجاد می‌شوند

### مهاجرت پایگاه داده (DBMigrate.py)
فایل `DBMigrate.py` مسئول مقداردهی اولیه پایگاه داده و ایجاد جداول است. این فایل موارد زیر را مدیریت می‌کند:

1. **اتصال به پایگاه داده**
   - ایجاد اتصال به پایگاه داده SQLite (`db.db`)
   - مدیریت نشانگر پایگاه داده برای دستورات SQL

2. **ایجاد جداول**
   - ایجاد خودکار جداول مورد نیاز در صورت عدم وجود
   - مدیریت دو جدول در حال حاضر:
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

3. **کاربرد**
   - مهاجرت به طور خودکار در زمان شروع برنامه اجرا می‌شود
   - اطمینان از به‌روز بودن طرح پایگاه داده
   - جلوگیری از خطاهای ناشی از عدم وجود جداول

4. **توابع**
   - استفاده از `CREATE TABLE IF NOT EXISTS` برای جلوگیری از ایجاد تکراری جداول
   - مدیریت کلیدهای اصلی با افزایش خودکار
   - اعمال محدودیت‌های یکتا برای ایمیل و نام محصول
   - مدیریت فیلدهای اجباری با محدودیت NOT NULL

### مدیریت اتصال پایگاه داده (DBConnection.py)
فایل `DBConnection.py` اتصالات پایگاه داده را با استفاده از SQLAlchemy ORM مدیریت می‌کند. این فایل موارد زیر را فراهم می‌کند:

1. **ادغام SQLAlchemy**
   - استفاده از SQLAlchemy برای نگاشت شیء-رابطه (ORM)
   - ارائه پایه اعلانی برای تعریف مدل‌ها
   - مدیریت کارآمد جلسات پایگاه داده

2. **پیکربندی اتصال**
   ```python
   engine = create_engine("sqlite:///db.db", echo=False)
   ```
   - پیکربندی پیش‌فرض از پایگاه داده SQLite استفاده می‌کند
   - پشتیبانی از MySQL/MariaDB از طریق تغییر رشته اتصال
   - `echo=False` ثبت درخواست‌های SQL را برای عملکرد بهتر غیرفعال می‌کند

3. **مدیریت جلسه**
   ```python
   Session = sessionmaker(bind=engine)
   ```
   - ایجاد کارخانه جلسه برای عملیات پایگاه داده
   - مدیریت اتصالات و تراکنش‌های پایگاه داده
   - ارائه دسترسی thread-safe به پایگاه داده

4. **توابع کمکی**
   - `create_all()`: ایجاد تمام جداول پایگاه داده تعریف شده در مدل‌ها
   - `get_session()`: برگرداندن یک جلسه جدید پایگاه داده برای عملیات

5. **پشتیبانی از پایگاه داده**
   - **SQLite** (پیش‌فرض):
     ```python
     engine = create_engine("sqlite:///db.db")
     ```
   - **MySQL/MariaDB**:
     ```python
     engine = create_engine("mysql+pymysql://username:password@localhost:3306/database_name")
     ```

6. **مدیریت خطا**
   - جذب و گزارش خطاهای اتصال به پایگاه داده
   - ارائه پیام‌های خطای واضح برای عیب‌یابی

7. **استفاده در مدل‌ها**
   ```python
   from table.DBConnection import DBConnection
   
   class YourModel:
       def __init__(self):
           self.Session = DBConnection.Session
   ```

8. **بهترین شیوه‌ها**
   - استفاده از اتصال‌دهی برای عملکرد بهتر
   - پیاده‌سازی مدیریت مناسب جلسه
   - پشتیبانی از چندین پایگاه داده
   - پیروی از بهترین شیوه‌های SQLAlchemy

### پشتیبانی از MySQL
- فریمورک از پایگاه داده MySQL نیز پشتیبانی می‌کند
- برای استفاده از MySQL، رشته اتصال را در `table/DBConnection.py` تغییر دهید:
  ```python
  engine = create_engine("mysql+pymysql://username:password@localhost:3306/database_name")
  ```

## مدیریت خطا
فریمورک شامل مدیریت خطای پایه برای موارد زیر است:
- داده‌های ورودی نامعتبر
- عملیات پایگاه داده
- اعتبارسنجی درخواست‌های HTTP
- منابع یافت نشده

## نکات امنیتی
1. این یک فریمورک آموزشی است و برای محیط‌های تولید توصیه نمی‌شود
2. هش کردن رمز عبور با bcrypt پیاده‌سازی شده است
3. اعتبارسنجی ورودی پایه از طریق FormatCheck.py ارائه می‌شود
4. پشتیبانی از احراز هویت JWT از طریق JWTManager.py در دسترس است
5. سیستم احراز هویت/مجوزدهی یکپارچه وجود ندارد

## اعتبارسنجی ورودی
فریمورک شامل یک ابزار FormatCheck برای اعتبارسنجی داده‌های ورودی است:

1. **اعتبارسنجی ایمیل**
   ```python
   FormatCheck.email("user@example.com")
   ```
   - استفاده از الگوی Regex: `^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-z]+$`
   - اعتبارسنجی:
     - بخش نام کاربری: حروف، اعداد، نقطه، زیرخط، علامت مثبت، خط تیره
     - بخش دامنه: حروف، اعداد، خط تیره
     - TLD: فقط حروف
   - مقدار برگشتی: True اگر معتبر باشد، False در غیر این صورت

2. **اعتبارسنجی طول**
   ```python
   FormatCheck.minimumLength("password", 6)
   ```
   - بررسی می‌کند که رشته نیازمندی حداقل طول را برآورده می‌کند
   - پارامترها:
     - input_string: رشته مورد اعتبارسنجی
     - min_length: حداقل طول مورد نیاز
   - مقدار برگشتی: True اگر طول >= min_length باشد، False در غیر این صورت

3. **نمونه‌های استفاده**
   ```python
   # اعتبارسنجی ایمیل
   if not FormatCheck.email(user_email):
       return Response.bad_request("فرمت ایمیل نامعتبر است")

   # بررسی طول رمز عبور
   if not FormatCheck.minimumLength(password, 6):
       return Response.bad_request("رمز عبور باید حداقل 6 کاراکتر باشد")

   # بررسی طول نام
   if not FormatCheck.minimumLength(name, 2):
       return Response.bad_request("نام باید حداقل 2 کاراکتر باشد")
   ```

4. **قوانین اعتبارسنجی**
   - ایمیل: باید مطابق با فرمت استاندارد ایمیل با کاراکترهای معتبر باشد
   - رمز عبور: حداقل 6 کاراکتر
   - نام: حداقل 2 کاراکتر

## نمونه استفاده

### ایجاد کاربر جدید
```bash
curl -X POST http://localhost:8001/user \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "password123", "name": "John Doe"}'
```

### دریافت تمام کاربران
```bash
curl http://localhost:8001/user
```

### دریافت کاربر خاص
```bash
curl http://localhost:8001/user/1
```

### به‌روزرسانی کاربر
```bash
curl -X PUT http://localhost:8001/user \
  -H "Content-Type: application/json" \
  -d '{"id": 1, "name": "نام به‌روز شده"}'
```

### حذف کاربر
```bash
curl -X DELETE http://localhost:8001/user \
  -H "Content-Type: application/json" \
  -d '{"id": 1}'
```

## دستورالعمل‌های توسعه

### ایجاد کنترلر جدید
1. ایجاد فایل جدید در پوشه `controller`
2. پیاده‌سازی رابط `IController`
3. اضافه کردن متدهای کنترلر (get, post, put, destroy)

### ایجاد مدل جدید
1. ایجاد فایل جدید در پوشه `model`
2. پیاده‌سازی رابط `IModel`
3. ایجاد جدول مربوطه در پوشه `table`
4. پیاده‌سازی عملیات پایگاه داده

## محدودیت‌ها
1. سیستم احراز هویت یکپارچه وجود ندارد
2. مدیریت خطای محدود
3. اعتبارسنجی ورودی پایه
4. محدودیت نرخ درخواست وجود ندارد
5. سیستم ثبت لاگ یکپارچه وجود ندارد
6. مکانیزم ذخیره‌سازی موقت یکپارچه وجود ندارد

## بهترین شیوه‌ها
1. همیشه از محیط مجازی استفاده کنید
2. کنترلرها را ساده نگه دارید، منطق را به مدل‌ها منتقل کنید
3. داده‌های ورودی را قبل از پردازش اعتبارسنجی کنید
4. خطاهای پایگاه داده را به درستی مدیریت کنید
5. از کدهای وضعیت HTTP مناسب در پاسخ‌ها استفاده کنید

## عیب‌یابی
1. اگر اتصال به پایگاه داده با خطا مواجه شد:
   - بررسی کنید که فایل پایگاه داده وجود دارد
   - اعتبارنامه‌های پایگاه داده را بررسی کنید (برای MySQL)
   - مجوزهای پایگاه داده را بررسی کنید

2. اگر سرور شروع نشد:
   - بررسی کنید که پورت 8001 در دسترس است
   - بررسی کنید که تمام وابستگی‌ها نصب شده‌اند
   - سازگاری نسخه پایتون را بررسی کنید

3. اگر درخواست‌ها با خطا مواجه شدند:
   - فرمت درخواست را بررسی کنید
   - قوانین اعتبارسنجی ورودی را بررسی کنید
   - اطمینان حاصل کنید که از متد HTTP صحیح استفاده می‌کنید

## چرخه حیات درخواست HTTP

### جریان کلی درخواست
```mermaid
graph TD
    A[درخواست کلاینت] --> B[HttpHandler]
    B --> C{اعتبارسنجی درخواست}
    C -->|معتبر| D[مسیریابی به کنترلر]
    C -->|نامعتبر| E[برگرداندن خطای 400]
    D --> F[اجرای متد کنترلر]
    F --> G[پردازش عملیات مدل]
    G --> H[عملیات پایگاه داده]
    H --> I[فرمت‌بندی پاسخ]
    I --> J[ارسال پاسخ به کلاینت]
```

### جریان ایجاد کاربر
```mermaid
sequenceDiagram
    participant Client
    participant HttpHandler
    participant UserController
    participant UserModel
    participant Database

    Client->>HttpHandler: POST /user
    Note over HttpHandler: اعتبارسنجی درخواست
    HttpHandler->>UserController: مسیریابی به کنترلر
    UserController->>UserModel: create()
    UserModel->>UserModel: اعتبارسنجی ایمیل
    UserModel->>UserModel: هش کردن رمز عبور
    UserModel->>Database: درخواست INSERT
    Database-->>UserModel: موفقیت
    UserModel-->>UserController: موفقیت
    UserController-->>HttpHandler: 200 OK
    HttpHandler-->>Client: پاسخ
```

### جریان مدیریت خطا
```mermaid
graph TD
    A[بروز خطا] --> B{نوع خطا}
    B -->|اعتبارسنجی| C[فرمت‌بندی خطای اعتبارسنجی]
    B -->|پایگاه داده| D[فرمت‌بندی خطای پایگاه داده]
    B -->|یافت نشد| E[فرمت‌بندی خطای 404]
    C --> F[تنظیم کد وضعیت خطا]
    D --> F
    E --> F
    F --> G[ارسال پاسخ خطا]
```

### تعامل اجزا
```mermaid
graph LR
    A[HttpHandler] -->|مسیریابی| B[کنترلر]
    B -->|استفاده می‌کند| C[مدل‌ها]
    C -->|تعامل می‌کند| D[پایگاه داده]
    B -->|پیاده‌سازی می‌کند| E[رابط IController]
    C -->|پیاده‌سازی می‌کند| F[رابط IModel]
    D -->|مدیریت می‌شود توسط| G[DBConnection]
    D -->|طرح توسط| H[DBMigrate]
```

## پردازش پاسخ

### کلاس Response (helper/Response.py)
کلاس `Response` روشی استاندارد برای فرمت‌بندی پاسخ‌های API فراهم می‌کند. این کلاس یک ساختار پاسخ سازگار را در تمام نقاط پایانی تضمین می‌کند.

#### ساختار پاسخ
```json
{
    "status_code": 200,      // کد وضعیت HTTP
    "status": "success",     // "success" یا "error"
    "message": {}            // داده‌های پاسخ یا پیام خطا
}
```

#### متدهای موجود

1. **متد پاسخ پایه**
   ```python
   @staticmethod
   def response(status_code, data)
   ```
   - ایجاد یک شیء پاسخ استاندارد
   - تعیین خودکار وضعیت بر اساس کد وضعیت
   - کدهای وضعیت >= 400 به عنوان "error" علامت‌گذاری می‌شوند
   - کدهای وضعیت < 400 به عنوان "success" علامت‌گذاری می‌شوند

2. **پاسخ موفقیت**
   ```python
   @staticmethod
   def success(data)
   ```
   - برگرداندن پاسخ 200 OK
   - برای عملیات‌های موفق استفاده می‌شود
   - مثال:
     ```python
     Response.success({"user": "created"})
     # برمی‌گرداند:
     # {
     #     "status_code": 200,
     #     "status": "success",
     #     "message": {"user": "created"}
     # }
     ```

3. **پاسخ درخواست نامعتبر**
   ```python
   @staticmethod
   def bad_request(message)
   ```
   - برگرداندن پاسخ 400 Bad Request
   - برای خطاهای اعتبارسنجی یا ورودی نامعتبر استفاده می‌شود
   - مثال:
     ```python
     Response.bad_request("فرمت ایمیل نامعتبر است")
     # برمی‌گرداند:
     # {
     #     "status_code": 400,
     #     "status": "error",
     #     "message": "فرمت ایمیل نامعتبر است"
     # }
     ```

4. **پاسخ غیرمجاز**
   ```python
   @staticmethod
   def unauthorized(message)
   ```
   - برگرداندن پاسخ 401 Unauthorized
   - برای خطاهای احراز هویت استفاده می‌شود
   - مثال:
     ```python
     Response.unauthorized("اعتبارنامه نامعتبر است")
     # برمی‌گرداند:
     # {
     #     "status_code": 401,
     #     "status": "error",
     #     "message": "اعتبارنامه نامعتبر است"
     # }
     ```

5. **پاسخ خطای داخلی**
   ```python
   @staticmethod
   def internal_error(message)
   ```
   - برگرداندن پاسخ 500 Internal Server Error
   - برای خطاهای سمت سرور استفاده می‌شود
   - مثال:
     ```python
     Response.internal_error("اتصال به پایگاه داده با خطا مواجه شد")
     # برمی‌گرداند:
     # {
     #     "status_code": 500,
     #     "status": "error",
     #     "message": "اتصال به پایگاه داده با خطا مواجه شد"
     # }
     ```

#### نمونه‌های استفاده

1. **در کنترلرها**
   ```python
   def post(self, data):
       try:
           # پردازش داده‌ها
           return Response.success({"message": "با موفقیت ایجاد شد"})
       except ValidationError:
           return Response.bad_request("ورودی نامعتبر است")
       except Exception:
           return Response.internal_error("خطای سرور")
   ```

2. **مدیریت خطا**
   ```python
   if not user_data:
       return Response.bad_request("کاربر یافت نشد")
   ```

3. **پاسخ موفقیت**
   ```python
   return Response.success({
       "user": {
           "id": 1,
           "name": "John Doe",
           "email": "john@example.com"
       }
   })
   ```

#### بهترین شیوه‌ها
1. همیشه از کلاس Response برای پاسخ‌های API سازگار استفاده کنید
2. از کدهای وضعیت مناسب برای سناریوهای مختلف استفاده کنید
3. پیام‌های خطای واضح و توصیفی ارائه دهید
4. ساختار داده پاسخ سازگار را حفظ کنید
5. از success() برای عملیات‌های موفق استفاده کنید
6. از متدهای خطای خاص (bad_request, unauthorized, internal_error) برای انواع مختلف خطا استفاده کنید

## احراز هویت

### احراز هویت JWT (helper/JWTManager.py)
فریمورک شامل پشتیبانی از JWT (JSON Web Token) برای احراز هویت است:

1. **ایجاد توکن**
   ```python
   jwt_manager = JWTManager()
   token = jwt_manager.create({"user_id": 123, "role": "admin"})
   ```
   - ایجاد توکن JWT با زمان انقضا
   - زمان انقضای پیش‌فرض: 60 دقیقه
   - استفاده از الگوریتم HS256
   - اضافه کردن خودکار برچسب زمان انقضا

2. **تأیید توکن**
   ```python
   decoded = jwt_manager.verify(token)
   if decoded:
       # توکن معتبر است
       user_data = decoded
   else:
       # توکن نامعتبر یا منقضی شده است
   ```
   - بررسی اعتبار توکن
   - بررسی زمان انقضا
   - برگرداندن داده‌های رمزگشایی شده یا False

3. **پیکربندی**
   ```python
   self.__secret_key = "کلید مخفی شما"
   self.__algorithm = "HS256"
   self.__expiration_minutes = 60
   ```
   - کلید مخفی قابل پیکربندی
   - الگوریتم قابل پیکربندی
   - زمان انقضای قابل پیکربندی

4. **نمونه استفاده**
   ```python
   # ایجاد توکن
   jwt_manager = JWTManager()
   user_data = {"user_id": 123, "role": "admin"}
   token = jwt_manager.create(user_data)

   # تأیید توکن
   decoded = jwt_manager.verify(token)
   if decoded:
       print("داده‌های رمزگشایی شده:", decoded)
   ```

5. **نکات امنیتی**
   - کلید مخفی باید در متغیرهای محیطی ذخیره شود
   - توکن‌ها پس از 60 دقیقه به طور پیش‌فرض منقضی می‌شوند
   - استفاده از الگوریتم HS256 استاندارد صنعتی
   - مدیریت مناسب انقضای توکن
</rewritten_file> 