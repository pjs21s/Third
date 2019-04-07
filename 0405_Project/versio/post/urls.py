from django.urls import path
from . import views
from django.conf.urls import url


app_name = 'post'
urlpatterns = [
    
    path('free_speech', views.free_speech, name='free_speech'),
    path('translation', views.translation, name='translation')
]