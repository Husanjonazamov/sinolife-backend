from core.apps.api.enums.order import OrderPaymentChoice
from django.conf import settings
from payme import Payme


payme = Payme(payme_id=settings.PAYME_ID)

def order_payment_type(order):
    order_id = order.id
    amount = order.total
    payment_type = order.payment_type
    
    if payment_type == OrderPaymentChoice.PAYME:
        pay_link = payme.initializer.generate_pay_link(
            id=int(order_id),
            amount=amount,
            return_url="https://sinolife.uz"
        )
    else:
        pay_link = "https://click.uz"
        
        
    return pay_link