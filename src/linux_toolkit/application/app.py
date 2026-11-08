# این فایل برای راه اندازی برنامه است که مسئولیت راندازی و اجرا است
# مسیر فایل src/linux_toolkit/application/app.py

# اضافه کردن کتاب خانه logging برای استفاده
import logging

# پاس دادن تابع setup_logging به این فایل برای استفاده
from linux_toolkit.core.logging import setup_logging
# این کتابخانه حالت های برنامه را مشخص می کند 
from enum import Enum

# دریافت خروجی کتاب خانه در یک متغییر بصورت رشته
logger = logging.getLogger(__name__)

class ApplicationState(Enum): # این کلاس حالت های برنامه را مشخص می کند
    CREATED = "created" # این شئ حالت ساخت شدن برنامه است
    INITIALIZING = "initializing" # مراحل آماده سازی در حال اجرا است 
    INITIALIZED = "initialized" # آماده سازی با موفقیت انجام شده
    RUNNING = "running" #برنامه در حال اجرا است 
    STOPPED = "stopped" #برنامه متوقف شد
    FAILED = "failed" #برنامه با خطا مواجه شد

class ApplicationError(Exception): # کلاس برای نمایش خطاهای برنامه  
    """کلاس برای نمایش خطاهای برنامه""" 
    def __init__(self, message: str, state: ApplicationState) -> None: # سازنده کلاس برای نمایش پیام خطا
        super().__init__(message) # فراخوانی سازنده کلاس پایه برای نمایش پیام خطا
        self.state = state # حالت برنامه در زمان خطا را مشخص می کند

class LinuxToolkitApplication:
# این تابع مشخص می کنه که برنامه اروری دارد یا نه اگر ندارد پیام را در ترمینال چاپ می کند
# اگر اروری پیداکرد از تریق تابع setup_logging که پاس داده شده از مسیر src/linux_toolkit/core/logging.py
# ان را نمایش دهد 
    def __init__(self) -> None:
        setup_logging()
        logger.info("initializing linux toolkit application")
        self.state = ApplicationState.CREATED # حالت اولیه برنامه ساخت شده است

    def initialize(self) -> None: # این تابع برای آماده سازی برنامه است
        self.state = ApplicationState.INITIALIZING # حالت برنامه آماده سازی شده است

        try:
            # مرحله اماده سازی برنامه بعد قرار داده می شود 
            raise RuntimeError("test error") # این خطا برای تست آماده سازی برنامه است و باید حذف شود

            self.state = ApplicationState.INITIALIZED # اماده سازی با موفقیت انجام شد 
            logger.info("Application initialized successfully")

        except Exception as error: # اگر در آماده سازی برنامه خطایی رخ داد این بخش اجرا می شود
            self.state = ApplicationState.FAILED # حالت برنامه با خطا مواجه شد
            logger.error(f"Application failed to initialize: {error}") # نمایش خطا در ترمینال

            raise ApplicationError(f"Application failed to initialize: {error}", self.state) from error # نمایش خطا در ترمینال و مشخص کردن حالت برنامه
