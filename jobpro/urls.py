"""jobpro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.auth import views

from apps.core.views import frontpage, signup, search_result_view
from apps.job.views import job_detail,dashboard,apply_for_job

urlpatterns = [
    path('',frontpage,name='frontpage'),
    path('admin/', admin.site.urls),
    path('signup/',signup,name='signup'),
    path('logout/',views.LogoutView.as_view(),name='logout'),
    path('login/',views.LoginView.as_view(template_name='core/login.html'),name='login'),
    path('dashboard/',dashboard, name='dashboard'),
    path('jobs/<int:job_id>/',job_detail, name = 'job_detail'),
    path('apply_for_job/<int:job_id>',apply_for_job, name = 'apply_for_job'),
    path('result',search_result_view, name='search_result'),
]
