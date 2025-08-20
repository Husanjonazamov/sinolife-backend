from core.apps.api.enums.order import OrderPaymentChoice
from django.conf import settings
from payme import Payme
from click_up import ClickUp
from config.env import env



payme = Payme(payme_id=env("PAYME_ID"))
click_up = ClickUp(service_id=env("CLICK_SERVICE_ID"), merchant_id=env("CLICK_MERCHANT_ID")) 


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
    elif payment_type == OrderPaymentChoice.CLICK:
        pay_link = click_up.initializer.generate_pay_link(
            id=int(order_id),
            amount=amount,
            return_url="https://sinolife.uz"
        )
    else:
        pay_link = "https://"
        
        
        
    return pay_link