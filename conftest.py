import pytest
from apps.accounts.models import CustomUser
from apps.customers.models import Customer, Address
from apps.orders.models import Payment, Status


@pytest.fixture
def user(db):
    """Usuário para testes"""
    return CustomUser.objects.create_user(
        email='user@test.com',
        password='testpass123'
    )


@pytest.fixture
def customer_pf(db, user):
    """Cliente Pessoa Física"""
    return Customer.objects.create(
        customer_type='PF',
        document='12345678901',
        name='João Silva',
        phone_number='11999999999',
        created_by=user
    )


@pytest.fixture
def payment_method(db):
    """Método de pagamento"""
    return Payment.objects.create(
        name='Dinheiro',
        is_requires_due_date=False
    )


@pytest.fixture
def status(db):
    """Status de pedido"""
    return Status.objects.create(
        description='Pendente',
        category=1,
        sequence_order=1
    )
