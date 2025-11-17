import pytest
from apps.customers.models import Customer, Address


@pytest.mark.django_db
class TestCustomer:
    """Testes básicos do modelo Customer"""

    def test_create_customer_pf(self, user):
        """Testa criação de cliente pessoa física"""
        customer = Customer.objects.create(
            customer_type='PF',
            document='12345678901',
            name='João Silva',
            phone_number='11999999999',
            created_by=user
        )
        assert customer.name == 'João Silva'
        assert customer.customer_type == 'PF'

    def test_document_is_unique(self, customer_pf):
        """Testa que documento é único"""
        with pytest.raises(Exception):
            Customer.objects.create(
                customer_type='PF',
                document=customer_pf.document,
                name='Outro Cliente',
                phone_number='11888888888'
            )


@pytest.mark.django_db
class TestAddress:
    """Testes básicos do modelo Address"""

    def test_create_address(self, customer_pf):
        """Testa criação de endereço"""
        address = Address.objects.create(
            customer=customer_pf,
            cep='12345678',
            street_name='Rua Teste',
            district='Centro',
            number='123',
            city='São Paulo',
            state='SP'
        )
        assert address.customer == customer_pf
        assert address.city == 'São Paulo'
