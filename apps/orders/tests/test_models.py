import pytest
from datetime import date
from apps.orders.models import Payment, Status, Order


@pytest.mark.django_db
class TestPayment:
    """Testes básicos do modelo Payment"""

    def test_create_payment(self):
        """Testa criação de método de pagamento"""
        payment = Payment.objects.create(
            name='Dinheiro',
            is_requires_due_date=False
        )
        assert payment.name == 'Dinheiro'
        assert not payment.is_requires_due_date


@pytest.mark.django_db
class TestStatus:
    """Testes básicos do modelo Status"""

    def test_create_status(self):
        """Testa criação de status"""
        status = Status.objects.create(
            description='Pendente',
            category=1,
            sequence_order=1
        )
        assert status.description == 'Pendente'


@pytest.mark.django_db
class TestOrder:
    """Testes básicos do modelo Order"""

    def test_create_order(self, customer_pf, payment_method, status, user):
        """Testa criação de pedido"""
        order = Order.objects.create(
            customer=customer_pf,
            payment_method=payment_method,
            delivery_method='DELIVERY',
            delivery_date=date.today(),
            order_status=status,
            created_by=user
        )
        assert order.customer == customer_pf
        assert order.order_number == 1

    def test_order_number_auto_increment(self, customer_pf, payment_method, status, user):
        """Testa auto incremento do número do pedido"""
        order1 = Order.objects.create(
            customer=customer_pf,
            payment_method=payment_method,
            delivery_method='DELIVERY',
            delivery_date=date.today(),
            order_status=status,
            created_by=user
        )
        order2 = Order.objects.create(
            customer=customer_pf,
            payment_method=payment_method,
            delivery_method='DELIVERY',
            delivery_date=date.today(),
            order_status=status,
            created_by=user
        )
        assert order2.order_number == order1.order_number + 1
