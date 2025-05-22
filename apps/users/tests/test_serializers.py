import pytest
from apps.users.serializers import UserSerializer


@pytest.mark.django_db
def test_user_serializer_valid_data():
    data = {
        'email': 'validemail@example.com',
        'username': 'Validusername',
        'password': 'validpassword',
        'role': 'developper'
    }
    serializer = UserSerializer(data=data)
    assert serializer.is_valid()
    user = serializer.save()
    assert user.email == 'validemail@example.com'


@pytest.mark.django_db
def test_user_serializer_missing_email():
    data = {
        'username': 'nouser',
        'password': 'pass1234',

    }
    serializer = UserSerializer(data=data)
    assert not serializer.is_valid()
    assert 'email' in serializer.errors
