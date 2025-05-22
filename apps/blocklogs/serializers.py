from rest_framework import serializers
from apps.blocklogs.models import Backlogs
from apps.projects.serializers import ProjectSerializer
from apps.projects.models import Project


class BlocklogsSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(read_only=True)
    project_id = serializers.PrimaryKeyRelatedField(
        queryset=Project.objects.all(),
        source='project',
        write_only=True
    )

    class Meta:
        model = Backlogs
        fields = ['id', 'title', 'description', 'project', 'project_id']

    def create(self, validated_data):

        blocklogs = Backlogs.objects.create(**validated_data)
        return blocklogs
