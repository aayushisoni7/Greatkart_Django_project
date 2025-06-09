from django.contrib import admin
from .models import Product, Variation, ReviewRating, ProductGallery
# import admin_thumbnails

# @admin_thumbnails.thumbnail('image')
# class ProductGalleryInline(admin.TabularInline):
#     model = ProductGallery
#     extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')

     ############33🔶 SEARCH FUNCTIONALITY ENABLE yeh line add karo
    search_fields = ['product_name', 'category__category_name']
    prepopulated_fields = {'slug': ('product_name',)}
    inlines = []

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('product', 'variation_category', 'variation_value')

     ######## 🔶 CHANGE HERE – Yeh line search bar enable karegi
    search_fields = ['product__product_name', 'variation_category', 'variation_value']

    # #################✅ Custom Admin Class
class ProductGalleryAdmin(admin.ModelAdmin):
    list_display = ['product']  
    search_fields = ['product__product_name'] 


 ####Register Model with Custom Admin
admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)
admin.site.register(ReviewRating)
admin.site.register(ProductGallery,ProductGalleryAdmin)
