'''
功能描述：发送邮件模块
编写人：zk
编写日期：2021/04/07

步骤分析：`
    1-
    2-
    3-
'''

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import os
from email.header import Header
from common.readConfig import ReadConfig
from common.configLog import logger

class ConfigEmail(object):

    def __init__(self):
        # 得到获取config.ini内参数的对象
        self._rc = ReadConfig()
        # 获取Email中的收件人、发件人及用户密码的信息
        self._send_to = self._rc.get_values('Email', 'to')
        self._from = self._rc.get_values('Email', 'from')
        self._pw = self._rc.get_values('Email', 'passwd')

    def send_email(self, filename):
        # 获取附件的文件名称
        name = os.path.split(filename)[-1]
        # 打开该文件，并将该文件内容读取到变量中
        with open(filename, 'rb') as fp:
            content = fp.read()
        # 组合邮件的第一部分-邮件的内容
        part1 = MIMEText('UI测试报告', 'plain', 'utf-8')
        # 组合邮件的第二部分-邮件的附件内容
        part2 = MIMEText(content, 'plain', 'utf-8')
        # 声明该部分为附件，并给与附件以文件的名称
        part2['Content-Type'] = 'application/octet-stream'
        part2['Content-Disposition'] = 'attachment; filename={}'.format(name)
        # 组合邮件
        msg = MIMEMultipart()
        msg.attach(part1)
        msg.attach(part2)

        # 声明一个时间字符串，用于组成邮件主题
        time_str = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
        subject = 'UI测试报告——' + time_str
        # 邮件的主题
        msg['Subject'] = Header(subject, 'utf-8')
        # 邮件的发送者
        msg['From'] = self._from
        # 邮件的接收者
        msg['To'] = self._send_to

        try:
            # 声明邮件对象
            smtpobj = smtplib.SMTP()
            # 连接邮件的服务器
            smtpobj.connect('smtp.qq.com')
            # 登录邮箱
            smtpobj.login(self._from, self._pw)
            # 发送邮件
            smtpobj.sendmail(self._from, self._send_to, msg.as_string())
        except Exception as e:
            logger.warning(f'邮件发送失败---{e}')
        else:
            logger.info('邮件发送成功')
        finally:
            # 退出邮件
            smtpobj.quit()

if __name__ == '__main__':
    ce = ConfigEmail()