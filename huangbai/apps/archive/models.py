from django.db import models


# Create your models here.
class Archive(models.Model):
    work_date = models.CharField(max_length=11, verbose_name="工作日期")
    service_item = models.CharField(max_length=30, verbose_name="服务事项")
    service_addr = models.CharField(max_length=10, verbose_name="服务地点")
    service_content = models.CharField(max_length=150, verbose_name="服务内容")
    person_count = models.IntegerField(verbose_name="服务人员")
    work_number = models.CharField(max_length=7, verbose_name="任务编号")

    class Meta:
        db_table = "doc_aqfw"
        verbose_name = "安服文档"
        verbose_name_plural = verbose_name
