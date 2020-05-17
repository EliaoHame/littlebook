#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2020/5/13 1:38
# @Author  : hellopand
# @File    : url.py
# @Software: PyCharm

from django.urls import path

from message import views

app_name = 'message'
urlpatterns = [
    path('board/', views.board, name='board'),
    path('messages/', views.selectAll, name='messages'),
]
