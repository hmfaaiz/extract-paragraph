from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('extract',views.extract,name='extract'),
    path('show',views.show,name='show'),
    path('download',views.download,name='download'),
   
]