# MyDjangoProject

این پروژه یک وب‌اپلیکیشن نمونه با استفاده از فریمورک جنگو است که شامل مدیریت موبایل‌ها و برندها می‌باشد.
نویسنده :‌حسین کوشکیان
## پیش‌نیازها

قبل از شروع، اطمینان حاصل کنید که موارد زیر را نصب کرده‌اید:

- Python 3.8 یا بالاتر
- pip 
- virtualenv (پیشنهادی)

## نصب و راه‌اندازی

1. ریپازیتوری را کلون کنید:

    ```sh
    git clone https://github.com/hoseinkoshkian/project_for_dide_pardaz_saba.git
    cd project_for_dide_pardaz_saba
    ```

2. یک محیط مجازی ایجاد کنید:

    ```sh
    python -m venv venv
    ```

3. محیط مجازی را فعال کنید:

    - در ویندوز:

        ```sh
        venv\Scripts\activate
        ```

    - در مک یا لینوکس:

        ```sh
        source venv/bin/activate
        ```

4. بسته‌های مورد نیاز را نصب کنید:

    ```sh
    pip install -r requirements.txt
    ```

5. تنظیمات پایگاه داده را پیکربندی کنید:

    فایل `settings.py` را در پوشه `mydjangoproject` باز کنید و تنظیمات پایگاه داده را به درستی مقداردهی کنید.
    چون دیتابیس پروژه اس کیو لایت است نیاز به ست کردن نیست
6. مهاجرت‌های پایگاه داده را اجرا کنید:

    ```sh
    python manage.py migrate
    ```

7. یک ابرکاربر (superuser) ایجاد کنید:

    ```sh
    python manage.py createsuperuser
    ```

8. سرور توسعه را اجرا کنید:

    ```sh
    python manage.py runserver
    ```

اکنون می‌توانید به آدرس `http://127.0.0.1:8000` بروید و اپلیکیشن خود را مشاهده کنید.

