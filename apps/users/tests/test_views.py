import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from apps.users.models import User


@pytest.mark.django_db
def test_register():
    client = APIClient()
    url = reverse('register')
    data = {
        "email": "test@example.com",
        "username": "testuser",
        "password": "pass123",
        "role": "developper"
    }
    response = client.post(url, data, format='json')
    assert response.status_code == 201
    assert User.objects.filter(email='test@example.com').exists()


@pytest.mark.django_db
def test_user_detail_permission_is_self():
    user1 = User.objects.create_user(email="test1@example.com", password="pass123", username='testuser1')
    user2 = User.objects.create_user(email="test2@example.com", password="pass123", username='testuser2')
    client = APIClient()
    client.force_authenticate(user=user1)
    url = reverse('user-detail', kwargs={'pk': user2.pk})
    response = client.get(url)
    assert response.status_code == 403

    url_self = reverse('user-detail', kwargs={'pk': user1.pk})
    response_self = client.get(url_self)
    assert response_self.status_code == 200
