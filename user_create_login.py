import os
import unittest
from appium import webdriver
import time
from appium.options.android import UiAutomator2Options
from config import get_config


class MyTestAppProject(unittest.TestCase):
    url = "http://127.0.0.1:4723/wd/hub"

    # 定义驱动，后续用来调用相关测代码
    caps = get_config.get_yaml_data()
    options = UiAutomator2Options().load_capabilities(caps)
    driver = webdriver.Remote(url, options=options)

    def setUp(self):
        # 捕获版本更新页面
        try:
            self.driver.find_element("id", "android:id/button2").click()
        except BaseException:
            print("没有提示更新版本！")

        # 跳过
        self.driver.find_element("id", "com.tal.kaoyan:id/tv_skip").click()

    def tearDown(self):
        self.driver.quit()

    @classmethod
    def setUpClass(cls) -> None:
        # 隐式等待
        cls.driver.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test_kaoyanbang_create_user(self,):
        # 注册
        self.driver.find_element("id", "com.tal.kaoyan:id/login_register_text").click()

        # 输入用户名
        self.driver.find_element("id", "com.tal.kaoyan:id/activity_register_username_edittext").send_keys("skzhaohh")

        # 输入密码
        self.driver.find_element("id", "com.tal.kaoyan:id/activity_register_password_edittext").send_keys("zsk123456!")

        # 输入邮箱
        self.driver.find_element("id", "com.tal.kaoyan:id/activity_register_email_edittext").send_keys("18739570240@163.com")

        # 点击立即注册
        self.driver.find_element("id", "com.tal.kaoyan:id/activity_register_register_btn").click()

        # 断言
        try:
            self.driver.find_element("id", "com.tal.kaoyan:id/myapptitle_Title")
        except Exception as mag:
            print("注册成功！" % mag)
        else:
            print("注册失败！")    # add assertion here

        # 截图
        time.sleep(0.5)
        self.driver.save_screenshot("./screenshots/screen.png")

    def test_kaoyanbang_login(self):
        # 输入用户名
        self.driver.find_element("id", "com.tal.kaoyan:id/login_email_edittext").send_keys("skzhaohh")

        # 输入密码
        self.driver.find_element("id", "com.tal.kaoyan:id/login_password_edittext").send_keys("zsk123456!")

        # 点击登录
        self.driver.find_element("id", "com.tal.kaoyan:id/login_login_btn").click()

        # 断言
        # self.assertEqual(True, False)  # add assertion here

        # 截图
        time.sleep(0.5)
        self.driver.save_screenshot("./screenshots/screen.png")


if __name__ == '__main__':
    unittest.main()
