# این فایل برای راه اندازی برنامه است که مسئولیت راندازی و اجرا است
# مسیر فایل src/linux_toolkit/application/app.py

# اضافه کردن کتاب خانه logging برای استفاده
import logging

# پاس دادن تابع setup_logging به این فایل برای استفاده
from linux_toolkit.core.logging import setup_logging

# دریافت خروجی کتاب خانه در یک متغییر بصورت رشته
logger = logging.getLogger(__name__)

class LinuxToolkitApplication:

# این تابع مشخص می کنه که برنامه اروری دارد یا نه اگر ندارد پیام را در ترمینال چاپ می کند
# اگر اروری پیداکرد از تریق تابع setup_logging که پاس داده شده از مسیر src/linux_toolkit/core/logging.py
# ان را نمایش دهد 
    def __init__(self):
        setup_logging()
        logger.info("در حال انالیز کردن برنامه")