import django_filters  # importation de la class FilterSet
from apps.users.models import User


class UserFilter(django_filters.FilterSet):
    role = django_filters.CharFilter(method='filter_role')

    class Meta:
        model = User
        fields = {
            'email': ['exact', 'icontains'],
            'username': ['exact', 'icontains'],
            'is_active': ['exact'],
            'is_staff': ['exact'],
        }

    def filter_role(self, queryset, name, value):
        roles = value.split(',')
        return queryset.filter(role__in=roles)
