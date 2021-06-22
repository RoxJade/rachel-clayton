from decimal import Decimal
from django.conf import settings


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0

    vat = total * Decimal(settings.UK_VAT_PERCENTAGE / 20)

    grand_total = total + vat

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'vat': settings.UK_VAT_PERCENTAGE,
        'grand_total': grand_total,
    }

    return context
