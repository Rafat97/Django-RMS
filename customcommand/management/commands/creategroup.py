from django.contrib.auth.models import User, Group, Permission
from django.core.management.base import BaseCommand
import os


class Command(BaseCommand):
    help = 'Added superuser'

    ALL_PERMISSION = ['account', 'token_blacklist',
                      'employapp', 'restaurantapp', 'votingapp']

    def handle(self, *args, **options):
        # user_obj = User.objects.get(id=2)
        new_group, created = Group.objects.get_or_create(name='Employ')
        # new_group.has_permissions('token_blacklist.delete_blacklistedtoken')
        # new_group.permissions.add(self.ALL_PERMISSION)
        # group = Group.objects.filter(user=user_obj)
        # all_permissions_in_groups = user_obj.get_group_permissions()

        # perm_list = user_obj.user_groups.all()
        # new_group, created = Group.objects.get_or_create(name='Employ')
    #    new_group.permissions.add(permission)
        for app_name in self.ALL_PERMISSION:
            permission = Permission.objects.filter(
                content_type__app_label=app_name
                # content_type="content_type",
            )
            for per in permission:
                new_group.permissions.add(per)
            self.stdout.write(self.style.SUCCESS(f"Added -- {app_name}"))
