from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('insert/',views.addTarea,name='insert'),
    path('delete/<int:id_tarea>/',views.delete,name='delete'),
    path('update/<int:id_tarea>/',views.update,name='update')
]