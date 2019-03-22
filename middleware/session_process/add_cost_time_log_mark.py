import random
import time
import logging
LOG = logging.getLogger('log')


class RecordUrlCostTimeMiddleware:
    """
    Django2 新写法
    """
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        try:
            # 时间开始
            log_mark = "RUCTM_Log_Mark_" + str(random.randint(10 ** 5, 10 ** 8)) + "_{}"
            _start_time = time.time()
            LOG.info(log_mark.format("RecordUrlCostTimeMiddleware request_start_time start:{}".format(_start_time)))
            request.session['_request_start_time'] = _start_time
            request.session['_request_log_mark'] = log_mark
            LOG.info(log_mark.format("RecordUrlCostTimeMiddleware request.path is:{}".format(request.path)))
            if request.method == 'GET':
                request_dict = request.GET
                LOG.info(log_mark.format("RecordUrlCostTimeMiddleware GET requested_dict:{}".format(request_dict)))
            elif request.method == 'POST':
                request_dict = request.POST
                LOG.info(log_mark.format("RecordUrlCostTimeMiddleware POST requested_dict:{}".format(request_dict)))
            else:
                pass
        except Exception as e:
            LOG.exception("RecordUrlCostTimeMiddleware_error process_request error is:{}".format(e))

        response = self.get_response(request)

        try:
            request_end_time = time.time()
            log_mark = request.session.get('_request_log_mark')
            request_url = request.path
            request_start_time = request.session.get('_request_start_time')
            # 中间件加个response.data 防止像昨晚那样查不到rebuild错误信息
            try:
                LOG.info(log_mark.format("RecordUrlCostTimeMiddleware response date is :{}".format(response.content)))
            except Exception as e:
                LOG.info(log_mark.format("RecordUrlCostTimeMiddleware get response date error :{}".format(e)))

            if log_mark and request_start_time:
                LOG.info(log_mark.format("RecordUrlCostTimeMiddleware_request_url:{},cost_time:{}".format(request_url, request_end_time - request_start_time)))
                if request_end_time - request_start_time > 4:
                    LOG.info(log_mark.format("warning_error_failrequest_url:{},cost_time bigger than 4".format(request_url)))
            else:
                LOG.info(log_mark.format("warning_error_fail_time_log_mark_error,request.session is:{}".format(request.session)))
        except Exception as e:
            LOG.exception("RecordUrlCostTimeMiddleware_error,error is:{}".format(e))
        return response


# class RecordUrlCostTimeMiddleware(object):
#     def process_request(self, request):
#         try:
#             # 时间开始
#             log_mark = "RUCTM_Log_Mark_" + str(random.randint(10 ** 5, 10 ** 8)) + "_{}"
#             _start_time = time.time()
#             LOG.info(log_mark.format("RecordUrlCostTimeMiddleware request_start_time start:{}".format(_start_time)))
#             request.session['_request_start_time'] = _start_time
#             request.session['_request_log_mark'] = log_mark
#             LOG.info(log_mark.format("RecordUrlCostTimeMiddleware request.path is:{}".format(request.get_full_path())))
#             if request.method == 'GET':
#                 request_dict = request.GET
#                 LOG.info(log_mark.format("RecordUrlCostTimeMiddleware GET requested_dict:{}".format(request_dict)))
#             elif request.method == 'POST':
#                 request_dict = request.POST
#                 LOG.info(log_mark.format("RecordUrlCostTimeMiddleware POST requested_dict:{}".format(request_dict)))
#             else:
#                 pass
#         except Exception as e:
#             LOG.exception("RecordUrlCostTimeMiddleware_error process_request error is:{}".format(e))
#
#     def process_response(self, request, response):
#         try:
#             request_end_time = time.time()
#             log_mark = request.session.get('_request_log_mark')
#             request_url = request.path
#             request_start_time = request.session.get('_request_start_time')
#
#             # 中间件加个response.data 防止像昨晚那样查不到rebuild错误信息
#             try:
#                 LOG.info(log_mark.format("RecordUrlCostTimeMiddleware response date is :{}".format(response.data)))
#             except Exception as e:
#                 LOG.info(log_mark.format("RecordUrlCostTimeMiddleware get response date error :{}".format(e)))
#
#             if log_mark and request_start_time:
#                 LOG.info(log_mark.format("RecordUrlCostTimeMiddleware_request_url:{},cost_time:{}".format(request_url, request_end_time - request_start_time)))
#                 if request_end_time - request_start_time > 4:
#                     LOG.info(log_mark.format("warning_error_failrequest_url:{},cost_time bigger than 4".format(request_url)))
#             else:
#                 LOG.info(log_mark.format("warning_error_fail_time_log_mark_error,request.session is:{}".format(request.session)))
#
#         except Exception as e:
#             LOG.exception("RecordUrlCostTimeMiddleware_error,error is:{}".format(e))
#         return response
