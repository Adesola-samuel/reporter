from django.urls import path
from .import views

app_name = 'truck'
urlpatterns = [
    path('', views.index,name='index'),
    path('admission/', views.selection, name='selection'),
    path('exit/', views.exit, name='exit'),
    path('create-selection-form/', views.create_selection_form, name='create-selection-form'),
    path('create-exit-form/', views.create_exit_form, name='create-exit-form')
]