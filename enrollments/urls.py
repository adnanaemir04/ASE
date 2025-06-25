from django.urls import path
from . import views

urlpatterns = [
    path('<int:course_id>/enroll/', views.enroll_in_course, name='enroll_course'),
]
