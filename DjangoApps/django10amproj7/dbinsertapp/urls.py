from django.conf.urls import url
drom.import views
app_name='dbinsertapp'
urlpatterns=[
    url(r'^$',views.input,name='input'),
    url(r'^insert$',views.insert,name='insert'),
    url(r'display$',views.display,name='display'),
]