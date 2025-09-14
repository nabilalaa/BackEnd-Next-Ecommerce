from django.contrib import admin
from .models import *



class CartItemInline(admin.TabularInline):  # أو StackedInline
    model = CartItem
    extra = 0

class CartAdmin(admin.ModelAdmin):
    list_display = ("user", "date_added", "total_items","total_price")
    inlines = [CartItemInline]

    def total_items(self, obj):
        return sum(item.quantity for item in obj.items.all())
    
    def total_price(self,obj):
        return sum(item.quantity * item.product.price for item in CartItem.objects.filter(cart__user__username=obj))


admin.site.register(Category)
admin.site.register(Item)
admin.site.register(CartItem)
admin.site.register(Cart,CartAdmin)
admin.site.register(Order)
