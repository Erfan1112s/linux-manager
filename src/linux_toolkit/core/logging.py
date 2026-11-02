# این فایل برای ثبت اتفاقاط سیستم هست 
# مسیر فایل src/linux_toolkit/core/logging.py

# این اینپروت یک کتاب خانه را به برنامه اضافه می کنه که لاگ های برنامه را مدیریت می کنه
import logging

# این تابع از کتاب خانه logging استفاده می کنه در واقع نحوه استفاده از کتاب خانه
def setup_logging():
    # در این خط کتاب خانه را صدا می زینم
    logging.basicConfig(
        # ورودی های را دریافت می کنیم
        level=logging.INFO,
        # چیز های که می خواهیم را دریافت می کنیم
        format="%(levelname)s: %(message)s"
    )