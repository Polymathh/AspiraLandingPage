from django.db import models

class Lead(models.Model):
    LANGUAGE_LEVEL_CHOICES = [
        ('A1', 'A1'),
        ('A2', 'A2'),
        ('B1', 'B1'),
        ('B2', 'B2'),
        ('C2', 'C2'),
    ]

    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    level_of_language = models.CharField(
        max_length=2,
        choices=LANGUAGE_LEVEL_CHOICES,
        default='A1'
        )
    created_at = models.DateTimeField(auto_now_add=True)
    is_followed_up = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.second_name} - {self.email}"
