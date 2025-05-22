from django.db import models
# Create your models here.


class Backlogs (models.Model):
    title = models.CharField(max_length=200, null=False)
    description = models.TextField(null=True)
    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE, null=False, related_name='blocklogs')

    def __str__(self):
        return self.title
