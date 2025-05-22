from rest_framework import serializers
from apps.blocklogs.models import Backlogs
from apps.blocklogs.serializers import BlocklogsSerializer
from apps.sprints.models import Sprint


class SprintSerializer(serializers.ModelSerializer):
    backlog = BlocklogsSerializer(read_only=True)
    backlog_id = serializers.PrimaryKeyRelatedField(
        queryset=Backlogs.objects.all(),
        source='backlog',
        write_only=True
    )

    class Meta:
        model = Sprint
        fields = ['id', 'title', 'date_debut', 'date_fin', 'goal', 'backlog', 'backlog_id']

    def create(self, validated_data):

        sprint = Sprint.objects.create(**validated_data)

        return sprint
