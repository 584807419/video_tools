from .models import VideoEditSoftware
import xadmin


class VideoEditSoftwareAdmin(object):
    list_display = ["name"]
    search_fields = ["name", "introduce"]
    list_filter = ["name"]
    # model_icon = "fa fa-cog fa-spin fa-la fa-fw"
    model_icon = "fa fa-camera-retro fa-lg"
    refresh_times = [3, 5]  # 定时刷新页面显示数据
    style_fields = {"introduce": "ueditor", "install_introduce": "ueditor",
                    "use_introduce": "ueditor"}  # 指定detail字段的样式是ueditor,然后插件中对ueditor这个样式进行识别
    import_excel = True
xadmin.site.register(VideoEditSoftware, VideoEditSoftwareAdmin)