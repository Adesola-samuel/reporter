from django.urls import path
from .import views

app_name = 'truck'
urlpatterns = [
    path('', views.index,name='index'),
    path('selection/', views.selection, name='selection'),
    path('create-selection-form/', views.create_selection_form, name='create-selection-form'),
    path('exit/', views.exit, name='exit'),
    path('create-exit-form/', views.create_exit_form, name='create-exit-form'),
    path('admmission/', views.admmission, name='admmission'),
    path('create-admmission-form/', views.create_admmission_form, name='create-admmission-form'),
]