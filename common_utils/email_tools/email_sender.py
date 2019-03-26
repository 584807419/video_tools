import smtplib
import logging
from email.mime.text import MIMEText
from email.header import Header
from django.conf import settings

LOG = logging.getLogger('log')

def send_mail_new(message_content, error_type=3, receivers=None, ):
    try:
        message = MIMEText(message_content, 'plain', 'utf-8')
        message['From'] = Header(u"线上工单预警", 'utf-8')
        message['To'] = Header(u"运维人员", 'utf-8')
        message['Subject'] = Header("来自预警系统的邮件", 'utf-8')
        s = smtplib.SMTP_SSL(settings.EMAIL_HOST, settings.EMAIL_PORT)
        s.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        s.sendmail(settings.EMAIL_HOST_USER, receivers, message.as_string())
        s.close()
        print("send email success")
        LOG.info("send email success")
    except Exception as e:
        LOG.exception("send email task error:{}".format(e))