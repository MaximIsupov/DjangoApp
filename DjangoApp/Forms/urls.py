from django.urls import path
from django.conf.urls import url, include

from . import views

from django.urls import path

from . import views

app_name = 'Forms'
urlpatterns = [
    path('', views.HelloWindow, name='index'),
    path('students/', views.IndexView.as_view(), name='students'),
    path('students/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('students/<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('students/<int:student_id>/edit_student/', views.edit_student, name='edit_student'),
    path('students/add_student_form/add_student/', views.add_student, name='add_student'),
    path('students/add_student_form/', views.add_student_form, name='add_student_form'),
    path('groups/', views.IndexViewGroups.as_view(), name='groups'),
    path('groups/<int:pk>/', views.DetailViewGroups.as_view(), name='group_detail'),
    path('groups/<int:pk>/group_results/', views.ResultsViewGroups.as_view(), name='group_results'),
    path('groups/<int:group_id>/edit_group/', views.edit_group, name='edit_group'),
    path('groups/add_group_form/add_group/', views.add_group, name='add_group'),
    path('groups/add_group_form/', views.add_group_form, name='add_group_form'),
    path('fakulcies/', views.IndexViewFakulcy.as_view(), name='fakulcies'),
    path('fakulcies/<int:pk>/', views.DetailViewFakulcy.as_view(), name='fakulcy_detail'),
    path('fakulcies/<int:pk>/fakulcy_results/', views.ResultsViewFakulcy.as_view(), name='fakulcy_results'),
    path('fakulcies/<int:group_id>/edit_fakulcy/', views.edit_fakulcy, name='edit_fakulcy'),
    path('fakulcies/add_fakulcy_form/add_fakulcy/', views.add_fakulcy, name='add_fakulcy'),
    path('fakulcies/add_fakulcy_form/', views.add_fakulcy_form, name='add_fakulcy_form'),
    path('students/<int:id>/student_delete', views.delete_student, name='delete_student'),
    path('groups/<int:id>/group_delete', views.delete_group, name='delete_group'),
    path('fakulcies/<int:id>/fakulcy_delete', views.delete_fakulcy, name='delete_fakulcy'),
]