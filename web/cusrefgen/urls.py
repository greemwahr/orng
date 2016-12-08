from django.conf.urls import url
from . import views

app_name = 'cusrefgen'
urlpatterns = [
    url(r'^refno/', views.display, name='display'),
    url(r'^$', views.form, name='form'),
]
