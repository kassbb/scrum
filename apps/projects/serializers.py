from rest_framework import serializers
from apps.projects.models import Project
from apps.users.models import User
from apps.users.serializers import UserSerializer


class ProjectSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    owner_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='owner',
        write_only=True
    )

    team = UserSerializer(many=True, read_only=True)
    team_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=User.objects.all(),
        source='team',
        write_only=True
    )

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'owner', 'owner_id', 'team', 'team_ids', 'date_debut', 'date_fin', 'objectif']

    def create(self, validated_data):
        team = validated_data.pop('team')
        project = Project.objects.create(**validated_data)
        project.team.set(team)
        return project
