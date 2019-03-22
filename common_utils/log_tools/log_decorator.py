# coding:utf-8
import logging
LOG = logging.getLogger('log')

from functools import wraps

def func_var_record(func):
    """
    功能:打印函数内所有的变量,debug方便,不用再每次加日志写很多次LOG.info
    用法:
        1.定义函数时候:
            视图类方法加装饰器@method_decorator(func_var_record)
            普通方法加装饰器@func_var_record
        2.函数体开始:
            log_mark = request.session.get('_request_log_mark')
            LOG.info(log_mark.format("function name start"))
        3.函数体结束:
            return处最后加上locals()
    :param func:
    :return:
    """
    def in_wrap(*args, **kwargs):
        res = func(*args, **kwargs)
        log_mark = "func_var_record_no_log_mark:{}"
        try:
            try:
                wsgi_request_obj = kwargs.get("request") or args[0]
                log_mark = wsgi_request_obj.session.get('_request_log_mark') or "{}"
            except Exception as e:
                LOG.exception(log_mark.format("func_var_record error1:{}".format(e)))
            LOG.info(log_mark.format("func_var_record start"))
            if isinstance(res, tuple):
                if len(res) == 2:
                    for k, v in res[-1].items():
                        try:
                            LOG.info(log_mark.format("key {} val: {}".format(k, v)))
                        except Exception as e:
                            LOG.exception(log_mark.format("func_var_record error2:{}".format(e)))
                    return res[0]
                if len(res) > 2:
                    for k, v in res[-1].items():
                        try:
                            LOG.info(log_mark.format("key {} val: {}".format(k, v)))
                        except Exception as e:
                            LOG.exception(log_mark.format("func_var_record error3:{}".format(e)))
                    return res[0:-1]
            else:
                return res
        except Exception as e:
            LOG.exception(log_mark.format("func_var_record_get: func_name: {} error: {}".format(func.__name__, e)))
            return res
    return in_wrap