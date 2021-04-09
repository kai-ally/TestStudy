'''
功能描述：主函数，框架的入口
编写人：zk
编写日期：2021/04/07

步骤分析：
    1-
    2-
    3-
'''

from common.configLog import logger
import unittest
import os
import time
from HTMLTestRunner import HTMLTestReportCN
from common.configEmail import ConfigEmail


def create_suite():
    # 定义测试用例所在的文件路径
    case_path = os.path.dirname(__file__) + r'/testCase/'
    try:
        # 生成测试套件
        suite = unittest.defaultTestLoader.discover(start_dir=case_path, pattern='little*.py')
        logger.info(f'测试套件生成成功，为{suite}')
        return suite
    except Exception as e:
        logger.warning(f'测试套件生成失败，失败原因为{e}')

# 清除多余的报告
def clear_report():
    # 定义报告的存储路径
    report_path = os.path.dirname(__file__) + r'/reports/'
    # 列出该路径下所有文件名称
    report_dir = os.listdir(report_path)
    # 出去不是报告的文件
    report_dir.remove('__init__.py')
    # 定义一个空列表，用来存放报告的生成时间信息
    report_ctime = []
    # 判断，当报告的份数大于3份时，开始执行清理
    if len(report_dir) >=3:
        for i in report_dir:
            # 获取每一个文件的生成时间，并存储至列表中
            report_ctime.append(os.path.getctime(report_path + i))
        # 以时间为key，文件名为value，组成字典
        temp_dict = {report_ctime[j]: report_dir[j] for j in range(len(report_dir))}
        # 排序文件的生成时间，从小到大
        report_ctime.sort()
        # 根据文件的生成时间，留下两个文件，其他文件遍历删除
        for i in range(len(report_ctime)-2):
            os.remove(report_path + temp_dict[report_ctime[i]])


if __name__ == '__main__':
    # 清理多余报告
    clear_report()
    # 创建测试套件
    suite = create_suite()
    # 定义时间字符串，用于组成报告名称
    time_str = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
    # 定义报告路径
    report_path = os.path.dirname(__file__) + r'/reports/'
    report_name = report_path + time_str + r'-UI自动化测试报告.html'
    # 打开该文件，将执行的结果写入该文件中，并定义文件的标题、测试人员及描述信息
    with open(report_name, 'wb') as fp:
        runner = HTMLTestReportCN(stream=fp, description='今日头条APP测试项目', tester='zk', title='UI自动化测试报告')
        runner.run(suite)
    # ce = ConfigEmail()
    # ce.send_email(report_name)
