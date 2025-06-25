from django.db import models
from django.contrib.auth import get_user_model
from courses.models import Course

User = get_user_model()

class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)
    progress_percent = models.FloatField(default=0.0)

    class Meta:
        unique_together = ('user', 'course')  # Bir kullanıcı bir kursa bir kez kayıt olabilir

    def __str__(self):
        return f"{self.user.username} → {self.course.title}"
