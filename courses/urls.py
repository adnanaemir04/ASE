from django.urls import path
from . import views

app_name = 'courses'  # Burası önemli!


urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('<int:pk>/', views.course_detail, name='course_detail'),
    path('lecture/<int:pk>/', views.lecture_detail, name='lecture_detail'),
    path('add/', views.add_course, name='add_course'),
    path('<int:pk>/add-lecture/', views.add_lecture, name='add_lecture'),
    path('dashboard/',views.instructor_dashboard,name = "instructor_dashboard"),



]
