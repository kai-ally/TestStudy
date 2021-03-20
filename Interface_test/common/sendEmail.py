'''
功能描述：发送测试结果给指定人员
编写人：zk
编写日期：2021/03/19

步骤分析：
    1-
    2-
    3-
'''

import os
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from common.readConfig import ReadConfig
from common.configLog import logger


class SendEmail(object):

    def __init__(self):
        # 定义获取配置文件对象，获取配置文件中email中的各个option的值
        rc = ReadConfig()
        self.from_addr = rc.get_value('email', 'from_addr')
        self.send_to = rc.get_value('email', 'send_to')
        self.passwd = rc.get_value('email', 'passwd')

    def send_email(self, filename):
        # 获取文件的名称，用于附件名称
        name = os.path.split(filename)[-1]
        # 读取发送文件的内容
        with open(filename, 'rb') as fp:
            content = fp.read()
        # 定义邮件的正文内容
        part1 = MIMEText('自动化测试报告', 'plain', 'utf-8')
        # 定义邮件的附件部分内容
        part2 = MIMEText(content, 'plain', 'utf-8')
        # 指定该部分为附件
        part2['Content-Type'] = 'application/octet-stream'
        part2['Content-Disposition'] = 'attachment; filename={}'.format(name)
        # 定义邮件的对象
        msg = MIMEMultipart()
        # 添加正文部分至该邮件
        msg.attach(part1)
        # 添加附件部分至该邮件
        msg.attach(part2)
        # 定义一个时间字符串，用于标记邮件主题
        time_str = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
        # 定义邮件主题
        subject = '自动化测试报告' + time_str
        msg['Subject'] = Header(subject, 'utf-8')
        # 定义邮件的发送者
        msg['From'] = self.from_addr
        # 定义邮件的接收者
        msg['To'] = self.send_to

        try:
            # 定义发送邮件的对象
            smtpobj = smtplib.SMTP()
            # 连接邮箱服务器
            smtpobj.connect('smtp.qq.com')
            # 使用用户名和授权码登录邮箱
            smtpobj.login(self.from_addr, self.passwd)
            # 发送邮件
            smtpobj.sendmail(self.from_addr, self.send_to, msg.as_string())
        except Exception as e:
            # 若发送异常，使用日志进行告警，并提示失败原因
            logger.warning(f'邮件发送失败，失败原因：{e}')
        else:
            # 发送成功，则记录日志
            logger.info('邮件发送成功')
        finally:
            # 无论成败与否，最后关闭邮箱
            smtpobj.quit()


if __name__ == '__main__':
    filename = os.path.dirname(os.path.dirname(__file__)) + r'/Log/2021_03_19_aototest_log.txt'
    sm = SendEmail()
    sm.send_email(filename)
