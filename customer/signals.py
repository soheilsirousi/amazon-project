from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from customer.models import ExtendedUser


@receiver(post_save, sender=User)
def create_user_details(sender, instance, created, *args, **kwargs):
    if created:
        user = ExtendedUser.objects.create(user=instance)