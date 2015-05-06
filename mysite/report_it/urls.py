from django.conf.urls import url
from report_it import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
] 