import unittest
from BSTestRunner import BSTestRunner

cases = unittest.defaultTestLoader.discover("../testcases", "test*.py")
file_name = open("report.html", "wb")
runner = BSTestRunner(stream=file_name, title="测试报告", description="测试报告描述")
runner.run(cases)
