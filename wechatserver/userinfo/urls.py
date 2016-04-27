from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^weixin/', views.index, name='weixin'),
]
