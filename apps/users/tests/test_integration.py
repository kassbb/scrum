import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from apps.users.models import User


@pytest.mark.django_db
def test_user_workflow():
    client = APIClient()

    register_url = reverse('register')
    register_data = {
        "email": "test@example.com",
        "username": "testuser",
        "password": "pass123",


    }
    response = client.post(register_url, register_data, format='json')
    assert response.status_code == 201
    assert User.objects.filter(email='test@example.com').exists()

    login_url = reverse('token_obtain_pair')
    login_data = {
        "email": "test@example.com",
        "password": "pass123"
    }
    response = client.post(login_url, login_data, format='json')
    assert response.status_code == 200
    tokens = response.json()
    assert 'access' in tokens and 'refresh' in tokens

    verify_url = reverse('token_verify')
    response = client.post(verify_url, {'token': tokens['access']}, format='json')
    assert response.status_code == 200

    user = User.objects.get(email='test@example.com')
    detail_url = reverse('user-detail', kwargs={'pk': user.pk})
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {tokens["access"]}')
    response = client.get(detail_url)

    assert response.status_code == 200
    assert response.data["email"] == "test@example.com"
    list_url = reverse('user-list')
    response = client.get(list_url)
    assert response.status_code in [200, 403]
