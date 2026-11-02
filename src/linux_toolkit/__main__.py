# هر برنامه ای باید یک نقطه شروع باید داشته باشه این فایلی نقطه شروع برنامه است 
# مسیر فایل src/linux_toolkit/__main__.py

# کلاس که برای دیافت ارور تعریف کردیم در مسیر src/linux_toolkit/application/app.py
# را به این فایل برای شروع برنامه تا قبل از هرچیز هموار ارور ها را دریافت کند
from linux_toolkit.application.app import LinuxToolkitApplication

# دریافت خروجی کلاس
def main():
    aplication = LinuxToolkitApplication()


# اگر خروجی برابر با فایل استارت بود خروجی را دریافت کن اگر نبود برو
if __name__ == "__main__":
    main()