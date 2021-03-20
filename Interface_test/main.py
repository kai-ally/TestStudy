'''
功能描述：框架主程序入口
编写人：zk
编写日期：2021/03/19

步骤分析：
    1-
    2-
    3-
'''

import time
import os
import unittest
from common.configLog import logger
from common.sendEmail import SendEmail
from HTMLTestRunner import HTMLTestReportCN


def case_suite():
    # 定义testcase的文件路径
    case_path = os.path.dirname(__file__) + r'/testCase/'
    # 生成测试套件
    suite = unittest.defaultTestLoader.discover(start_dir=case_path, pattern='test*.py')
    logger.info(f'测试套件已生成，其中内容有{suite}')
    return suite


def clear_report():
    """保留最新生成的3份报告，其余的删除"""
    # 获取测试报告所在文件路径
    report_path = os.path.dirname(__file__) + r'/report/'
    # 列出该报告文件夹下所有的文件，组成列表
    report_list = os.listdir(report_path)
    # 删除掉不是报告的文件名称
    report_list.remove('__init__.py')
    # 定义一个空列表，用于存放测试报告的生成时间
    ctime_report = []
    # 获取报告文件列表的长度，得到有效报告的数量
    num = len(report_list)
    if num >= 3:
        # 循环遍历所有生成的报告，获取其生成时间，并追加至列表中
        for i in report_list:
            file_ctime = os.path.getctime(report_path + i)
            ctime_report.append(file_ctime)
        # 定义一个临时字典，将报告的生成时间和报告名称对应起来
        temp_dict = {ctime_report[j]: report_list[j] for j in range(num)}
        # 排序，将报告的生成时间进行排序
        ctime_report.sort()
        # 删除掉较早生成的报告，保留最新生成的2份报告
        for i in range(num -2):
            os.remove(report_path + temp_dict[ctime_report[i]])



if __name__ == '__main__':
    # 调用清除报告的函数，保留最新的两份报告
    clear_report()
    # 带用测试套件生成的函数，返回测试套件
    suite = case_suite()
    # 定义时间字符串，用于报告的命名
    time_str = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())
    # 拼接报告的存放路径和报告的名称
    report_name = os.path.dirname(__file__) + r'/report/' + time_str + r'_report.html'
    # 打开文件
    with open(report_name, 'wb') as fp:
        # 定义测试报告的输出路径、标题、内容描述及测试人员信息
        runner = HTMLTestReportCN(stream=fp, title='自动化测试报告', description='玩安卓项目', tester='zk')
        # 运行测试套件，生成测试报告
        runner.run(suite)
    # 将生成的自动化测试报告发送至指定邮箱
    sm = SendEmail()
    sm.send_email(report_name)
