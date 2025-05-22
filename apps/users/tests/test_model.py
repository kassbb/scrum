import pytest
from apps.users.models import Profile, User


@pytest.mark.django_db
def test_user_model():
    user = User.objects.create_user(
        username='Testuser',
        email='testuser@example.com',
        password='1234',
        role='developper'
    )

    assert user.username == str('Testuser').capitalize()
    assert user.email == 'testuser@example.com'
    assert user.role == 'developper'
    assert user.check_password('1234')


@pytest.mark.django_db
def test_profile_ceate():
    user = User.objects.create_user(email="testuser@example.com", password="1234", username='Testuser')
    assert Profile.objects.filter(user=user).exists()
