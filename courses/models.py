from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Oluşturan ")
    category = models.CharField(max_length=100)
    level = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Lecture(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lectures")
    title = models.CharField(max_length=200)
    video = models.FileField(upload_to='lectures/')
    order_index = models.IntegerField()

    def __str__(self):
        return f"{self.course.title} - {self.title}"
