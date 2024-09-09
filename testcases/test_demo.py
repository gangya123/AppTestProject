from appium import webdriver
from time import sleep
from config import get_config
from appium.options.android import UiAutomator2Options

url = "http://127.0.0.1:4723/wd/hub"

caps = get_config.get_yaml_data()
# 定义驱动，后续用来调用相关测代码
options = UiAutomator2Options().load_capabilities(caps)
driver = webdriver.Remote(url, options=options)

# 编写测试代码
# 隐式等待5s，显示
driver.implicitly_wait(5)

try:
    # 跳过版本更新
    driver.find_element("id", "android:id/button2").click()
except BaseException:
    print("没有提示！")

# 点击跳过
driver.find_element("id", "com.tal.kaoyan:id/tv_skip").click()

# 输入用户名
driver.find_element("id", "com.tal.kaoyan:id/login_email_edittext").send_keys("skzhaohh")

# 输入密码
driver.find_element("id", "com.tal.kaoyan:id/login_password_edittext").send_keys("zsk123456!")

# 点击登录
driver.find_element("id", "com.tal.kaoyan:id/login_login_btn").click()

sleep(5)
# 测试完毕，退出
driver.quit()
