from appium import webdriver
from appium.options.android import UiAutomator2Options

url = "http://127.0.0.1:4723/wd/hub"
caps = {
    "platformName": "android",
    "deviceName": "127.0.0.1:21503",
    "appPackage": "com.tal.kaoyan",
    "appActivity": "com.tal.kaoyan.ui.activity.ucenter.LoginActivity"
}

# 定义驱动，后续用来调用相关测代码
options = UiAutomator2Options().load_capabilities(caps)
device = webdriver.Remote(url, options=options)

# 编写测试代码

# 测试完毕，推出
device.quit()
