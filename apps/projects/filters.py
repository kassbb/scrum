import django_filters  # importation de la class FilterSet

from apps.projects.models import Project


class filterProject(django_filters.FilterSet):
    class Meta:
        model = Project
        fields = {
            'name': ['exact', 'icontains'],
            'description': ['exact', 'icontains'],
            'owner': ['exact'],
            'team': ['exact'],
            'date_debut': ['exact', 'gte', 'lte'],
            'date_fin': ['exact', 'gte', 'lte'],
            'objectif': ['exact', 'icontains'],
        }
