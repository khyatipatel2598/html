from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(event, cart):
    keys= cart.keys()
    for id in keys:

        if int(id) == event.id :
            return True

    return False

@register.filter(name='cart_quantity')
def cart_quantity(event, cart):
    keys= cart.keys()
    for id in keys:

        if int(id) == event.id :
            return cart.get(id)

    return 0

@register.filter(name='total_cart_price')
def total_cart_price(events , cart):
    sum = 0 ;
    for p in events:
        sum += p.event_price

    return sum
