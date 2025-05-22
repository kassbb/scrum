from django.db import models


class Sprint(models.Model):
    title = models.CharField(max_length=200)
    date_debut = models.DateField(null=True)
    date_fin = models.DateField(null=True)
    goal = models.TextField(null=True)
    # Option 1: Use the imported model directly
    backlog = models.ForeignKey('blocklogs.Backlogs', on_delete=models.CASCADE, null=False, related_name='sprints')

    def __str__(self):
        return self.title
