from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    name = models.CharField(max_length=100, verbose_name=_('name'))
    is_active = models.BooleanField(default=True, verbose_name=_('is active'))
    created_time = models.DateTimeField(auto_now_add=True, verbose_name=_('created time'))
    updated_time = models.DateTimeField(auto_now=True, verbose_name=_('updated time'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class Product(models.Model):
    PERCENTAGE = 1
    INSTANT = 2

    choices = (
        (PERCENTAGE, 'Percentage'),
        (INSTANT, 'Instant'),
    )

    name = models.CharField(max_length=100, verbose_name=_('name'), null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('category'), null=False, blank=False)
    price = models.PositiveBigIntegerField(verbose_name=_('price'), null=False, blank=False)
    description = models.TextField(verbose_name=_('description'), null=True, blank=True)
    discount_type = models.PositiveSmallIntegerField(choices=choices, default=PERCENTAGE, verbose_name=_('discount type'))
    discount_value = models.PositiveBigIntegerField(null=True, blank=True, verbose_name=_('discount value'))
    is_active = models.BooleanField(default=True, verbose_name=_('is active'))
    created_time = models.DateTimeField(auto_now_add=True, verbose_name=_('created time'))
    updated_time = models.DateTimeField(auto_now=True, verbose_name=_('updated time'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


class Discount(models.Model):
    PERCENTAGE = 1
    INSTANT = 2

    choices = (
        (PERCENTAGE, 'Percentage'),
        (INSTANT, 'Instant')
    )

    code = models.CharField(max_length=30, null=False, blank=False, verbose_name=_('code'))
    type = models.PositiveSmallIntegerField(choices=choices, default=PERCENTAGE, verbose_name=_('type'))
    value = models.PositiveBigIntegerField(null=False, blank=False, verbose_name=_('value'))
    expire_time = models.DateTimeField(null=True, blank=True, verbose_name=_('expire time'))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='coupons', verbose_name=_('product')
                                , null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='coupons', verbose_name=_('category')
                                , null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='coupons', verbose_name=_('user')
                                , null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name=_('is active'))
    created_time = models.DateTimeField(auto_now_add=True, verbose_name=_('created time'))
    updated_time = models.DateTimeField(auto_now=True, verbose_name=_('updated time'))

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = _('Discount')
        verbose_name_plural = _('Discounts')


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', verbose_name=_('product'))
    image = models.ImageField(upload_to='product_image', verbose_name=_('image'))
    is_active = models.BooleanField(default=True, verbose_name=_('is active'))
    created_time = models.DateTimeField(auto_now_add=True, verbose_name=_('created time'))
    updated_time = models.DateTimeField(auto_now=True, verbose_name=_('updated time'))

    def __str__(self):
        return f'{self.product}'

    class Meta:
        verbose_name = _('Product Image')
        verbose_name = _('Products Image')


class ProductAttribute(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name=_('name'))
    value = models.CharField(max_length=100, null=False, blank=False, verbose_name=_('value'))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='attributes', verbose_name=_('product'))
    is_active = models.BooleanField(default=True, verbose_name=_('is active'))
    created_time = models.DateTimeField(auto_now_add=True, verbose_name=_('created time'))
    updated_time = models.DateTimeField(auto_now=True, verbose_name=_('updated time'))

    def __str__(self):
        return f'{self.attribute} : {self.product}'

    class Meta:
        verbose_name = _('Product Attribute')
        verbose_name_plural = _('Products Attributes')
