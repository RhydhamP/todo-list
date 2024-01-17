from django.contrib import admin
from django.urls import path, include
from TO_DO_List import views

urlpatterns = [
    path('', views.createNewTask, name="index"),
    path('createNewTask', views.createNewTask, name="index"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('register', views.register, name="register"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('start/<int:id>', views.start, name="start"),
    path('complete/<int:id>', views.complete, name="complete"),

]
