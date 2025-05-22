from django.db import models
from apps.users.models import User


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='owned_projects')
    team = models.ManyToManyField(User, related_name='projects', null=True)
    date_debut = models.DateField(null=True)
    date_fin = models.DateField(null=True)
    objectif = models.TextField(null=True)

    def __str__(self):
        return self.name
