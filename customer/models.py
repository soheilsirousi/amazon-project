from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class ExtendedUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='detail', verbose_name=_('user'))
    phone_number = models.PositiveBigIntegerField(null=True, blank=True, verbose_name=_('phone number'))
    national_id = models.PositiveBigIntegerField(null=True, blank=True, verbose_name=_('national id'))

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = _('Extended User')
        verbose_name_plural = _('Extended Users')

