from django.contrib import admin
from .models import Payment, Order, OrderProduct
# Register your models here.

# Inline model to show OrderProducts inside Order detail view
class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('payment', 'user', 'product', 'quantity', 'product_price', 'ordered')
    extra = 0
# Admin for Order model
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'full_name', 'phone', 'email', 'city', 'order_total', 'tax', 'status', 'is_ordered', 'created_at']
    list_filter = ['status', 'is_ordered']
    search_fields = ['order_number', 'first_name', 'last_name', 'phone', 'email']
    list_per_page = 20
    inlines = [OrderProductInline]

############################################

class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'user', 'quantity', 'product_price', 'ordered', 'created_at']
    search_fields = [
        'product__product_name',     # ForeignKey to Product model
        'order__order_number',       # ForeignKey to Order model
        'user__email',               # ForeignKey to Account model
        'user__first_name',
        'user__last_name'
    ]
    list_filter = ['ordered', 'created_at', 'product', 'user']
    list_per_page = 25

class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user', 'payment_id', 'amount_paid', 'status', 'created_at']  # Table columns
    search_fields = ['payment_id', 'status', 'user__email']  # 🔍 searchable    

    
    



#  Register models with admin site
admin.site.register(Payment,PaymentAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct, OrderProductAdmin)


