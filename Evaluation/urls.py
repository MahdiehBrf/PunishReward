from django.conf.urls import url

from . import views

app_name = 'evaluation'
urlpatterns = [
    url(r'^add_employee', views.add_employee, name='add_employee'),
    url(r'^', views.show_master_page, name='show_master_page'),
]