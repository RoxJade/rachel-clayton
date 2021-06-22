from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    vat = total * Decimal(settings.UK_VAT_PERCENTAGE / 100)

    grand_total = total + vat

    vat_percentage = grand_total - (vat * 5)

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'vat': settings.UK_VAT_PERCENTAGE,
        'grand_total': grand_total,
        'vat_percentage': vat_percentage,
    }

    return context
