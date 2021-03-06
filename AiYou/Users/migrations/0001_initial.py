# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-03-11 09:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='地址编号')),
                ('recv_name', models.CharField(max_length=255, verbose_name='收货人姓名')),
                ('recv_phone', models.CharField(max_length=50, verbose_name='收货人联系方式')),
                ('province', models.CharField(max_length=255, verbose_name='省区')),
                ('city', models.CharField(max_length=255, verbose_name='市区')),
                ('country', models.CharField(max_length=255, verbose_name='县区')),
                ('desc', models.CharField(max_length=255, verbose_name='详细描述')),
                ('status', models.BooleanField(default=True, verbose_name='是否默认地址')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='所属用户')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='用户编号')),
                ('mickname', models.CharField(max_length=255, unique=True, verbose_name='用户昵称')),
                ('age', models.CharField(max_length=200, verbose_name='用户年龄')),
                ('gender', models.CharField(max_length=50, verbose_name='用户性别')),
                ('header', models.ImageField(default='static/images/users_head/default.png', upload_to='static/images/users_head/', verbose_name='用户头像')),
                ('phone', models.CharField(max_length=50, verbose_name='联系方式')),
                ('status', models.IntegerField(default=1, verbose_name='用户状态')),
                ('user', models.OneToOneField(on_delete=models.Model, to=settings.AUTH_USER_MODEL, verbose_name='关联')),
            ],
        ),
    ]
