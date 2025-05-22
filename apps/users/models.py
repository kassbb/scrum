from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):

    ROLE_CHOICES = (
        ('scrum_master', 'scrum master'),
        ('product_owner', 'product owner'),
        ('developper', 'Developer'),
    )
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='developper')
    email = models.CharField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f"{self.username} ({self.role}) "


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return f"profile de {self.user.username}"
