from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Transaction, Product


'''
signals for calculating the transaction total amount
'''
@receiver(pre_save, sender=Transaction)
def calculate_total_price(sender, instance, **kwargs):
    if not instance.price_total:
        instance.price_total = instance.quantity * instance.price



'''
signals for updating the stock after saving a transaction
'''
@receiver(post_save, sender=Transaction)
def update_stock(sender, instance, **kwargs):
    product = Product.objects.get(id=instance.product_id)
    if instance.transaction == 1: # checking if transaction is IN or OUT (1 representing IN here, since we defined it that way in our model choices)
        if not product.stock: # since we have set stock field to be null=True in our models we may not have any stock defined. Hence, we need to instantiate it
            product.stock = instance.quantity
        else:
            product.stock += instance.quantity # else, if stock is not null, add upon it
    else: # else case, that is transaction of OUT type
        product.stock -= instance.quantity

    product.save()