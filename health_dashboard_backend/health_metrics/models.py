from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class HealthMetric(models.Model):
    """
    Модел за здравни показатели.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Потребител, към който принадлежи показателят
    date = models.DateField()                                 # Дата на записа
    steps = models.IntegerField()                             # Брой стъпки
    heart_rate = models.FloatField()                          # Сърдечен ритъм
    sleep_hours = models.FloatField()                         # Часове сън

    def __str__(self):
        return f"{self.user.username} - {self.date}"
