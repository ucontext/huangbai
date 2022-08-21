# Generated by Django 4.1 on 2022-08-21 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Archive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_date', models.CharField(max_length=11, verbose_name='工作日期')),
                ('service_item', models.CharField(max_length=30, verbose_name='服务事项')),
                ('service_addr', models.CharField(max_length=10, verbose_name='服务地点')),
                ('service_content', models.CharField(max_length=150, verbose_name='服务内容')),
                ('person_count', models.IntegerField(verbose_name='服务人员')),
                ('work_number', models.CharField(max_length=7, verbose_name='任务编号')),
            ],
            options={
                'verbose_name': '安服文档',
                'verbose_name_plural': '安服文档',
                'db_table': 'doc_aqfw',
            },
        ),
    ]