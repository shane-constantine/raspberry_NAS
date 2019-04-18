"""raspberry_NAS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from . import views
from ras_data.views import data_detail,data,datas_json
from files_manage.views import files_page,upload_ajax,download_file,delete_file
from apscheduler.scheduler import Scheduler
from . import timer_tasks

sched = Scheduler()


@sched.interval_schedule(seconds=1)
def my_task():
    #timer_tasks.get_data()
    pass
sched.start()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name="home"),
    path('sysdata/', data_detail, name="data_page"),
    path('files/', files_page, name="files_page"),
    path('data/data_now',data),
    path('data/datas',datas_json),
    path('upload/',upload_ajax),
    path('download/<int:pk>',download_file,name="download"),
    path('delete/<int:pk>', delete_file, name="delete"),
]
