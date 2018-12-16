from django.db import models

from DjangoUeditor.models import UEditorField

# Create your models here.

class VideoEditSoftware(models.Model):
    name = models.CharField(default="", blank=True, null=True, max_length=50,verbose_name="软件名字")
    size = models.IntegerField(default=0, blank=True, null=True, max_length=50, verbose_name="软件大小")
    bit = models.IntegerField(default=64, blank=True, null=True, max_length=50, verbose_name="软件位数")
    support_os = models.CharField(default="", blank=True, null=True, max_length=50, verbose_name="支持操作系统")

    click_nums = models.IntegerField(default=0, verbose_name="点击量")
    download_nums = models.IntegerField(default=0, verbose_name="下载量")

    introduce =UEditorField(verbose_name="软件简介", width=600, height=300, imagePath="videoedit/ueditor",
                          filePath="videoedit/ueditor",
                          upload_settings={"imageMaxSize": 1204000},
                          default="")
    download_url = models.CharField(default="", blank=True, null=True, max_length=255,verbose_name="下载链接")
    net_disk_url = models.CharField(default="", blank=True, null=True, max_length=50, verbose_name="网盘链接")
    net_disk_code = models.CharField(default="", blank=True, null=True, max_length=50, verbose_name="网盘密码")
    install_introduce = UEditorField(verbose_name="安装介绍", width=600, height=300, imagePath="videoedit/ueditor",
                          filePath="videoedit/ueditor",
                          upload_settings={"imageMaxSize": 1204000},
                          default="")
    use_introduce = UEditorField(verbose_name="使用介绍", width=600, height=300, imagePath="videoedit/ueditor",
                          filePath="videoedit/ueditor",
                          upload_settings={"imageMaxSize": 1204000},
                          default="")

    class Meta:
        verbose_name="视频编辑软件"
        verbose_name_plural=verbose_name


    def __str__(self):
        return f"{self.name}"
