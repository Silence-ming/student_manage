"""Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .view import *
urlpatterns = [
    path('admin/',admin.site.urls),

    path('teacher.html/',teacher),
    path('teacher_addPage.html/',teacher_addPage),
    path('teacher_add/',teacher_add),
    path('teacher_editPage.html/<str:id>',teacher_editPage),
    path('teacher_edit/',teacher_edit),
    path('teacher_del/<str:id>',teacher_dels),

    path('class.html/',classes),
    path('class_addPage.html/', class_addPage),
    path('class_add/', class_add),
    path('class_editPage.html/<str:id>', class_editPage),
    path('class_edit/', class_edit),
    path('class_del/<str:id>', class_dels),

    path('student.html/',student),
    path('student_addPage.html/',student_addPage),
    path('student_add/',student_add),
    path('student_editPage.html/<str:id>',student_editPage),
    path('student_edit/',student_edit),
    path('student_del/<str:id>',student_dels),
    path('',loginPage),
    path('login/',login),
    # path('registerPage/',registerPage),
    # path('register/',register),
    path('exit/',exits),
    path('keyPage/',keyPage),
    path('key/',key)
]
