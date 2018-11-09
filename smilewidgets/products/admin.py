from django.contrib import admin

# Register your models here.
from .models import Product 
from .models import GiftCard
from .models import ProductPrice
admin.site.register(ProductPrice)
admin.site.register(Product)
admin.site.register(GiftCard)

