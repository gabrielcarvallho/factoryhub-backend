import pytest
from apps.accounts.models import CustomUser


@pytest.mark.django_db
class TestCustomUser:
    """Testes básicos do modelo CustomUser"""

    def test_create_user(self):
        """Testa criação de usuário"""
        user = CustomUser.objects.create_user(
            email='test@example.com',
            password='testpass123'
        )
        assert user.email == 'test@example.com'
        assert user.check_password('testpass123')

    def test_email_must_be_provided(self):
        """Testa que email é obrigatório"""
        with pytest.raises(ValueError):
            CustomUser.objects.create_user(email='', password='testpass123')
