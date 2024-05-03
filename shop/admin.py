from django.contrib import admin
from shop.models import *
from django.contrib.admin import register


class ProductAttributeInline(admin.TabularInline):
    model = ProductAttribute
    extra = 1


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_active', 'category')
    inlines = (ProductAttributeInline, ProductImageInline)


@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('parent', 'name', 'is_active')


@register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('code', 'expire_time', 'type', 'value')
