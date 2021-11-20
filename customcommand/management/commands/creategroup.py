from django.contrib.auth.models import User, Group, Permission
from django.core.management.base import BaseCommand
import os
from django.contrib.contenttypes.models import ContentType
from restaurantapp.models import Restaurant,Menu,Item

class Command(BaseCommand):
    help = 'Added superuser'

    EMPLOY_GROUP = {
        "DIRECT_APP_NAME" :  ['account', 'token_blacklist','employapp', 'votingapp'],
        "DIRECT_PERMISSION_NAME" : ['view_restaurant','view_item','view_menu',]
    }
    

    def handle(self, *args, **options):
        # user_obj = User.objects.get(id=2)
        # perm_list = user_obj.groups.all()
        # content_type = ContentType.objects.get_for_model(Restaurant)
        # print(content_type)
        # new_group.has_permissions('token_blacklist.delete_blacklistedtoken')
        # new_group.permissions.add(self.ALL_PERMISSION)
        # group = Group.objects.filter(user=user_obj)
        # all_permissions_in_groups = user_obj.get_group_permissions()
        # perm_list = user_obj.user_groups.all()
        # new_group, created = Group.objects.get_or_create(name='Employ')
        # new_group.permissions.add(permission)
        
        new_group, created = Group.objects.get_or_create(name='Employ')
        if created:
            self.stdout.write(self.style.SUCCESS(f"---------START APP LEVEL PERMISSION----------"))
            for app_name in self.EMPLOY_GROUP['DIRECT_APP_NAME']:
                permission = Permission.objects.filter(
                    content_type__app_label=app_name
                    # content_type="content_type",
                )
                for per in permission:
                    new_group.permissions.add(per)
                self.stdout.write(self.style.SUCCESS(f"Added -- {app_name}"))

            self.stdout.write(self.style.SUCCESS(f"---------START CODENAME LEVEL PERMISSION----------"))    
            for code_name in self.EMPLOY_GROUP['DIRECT_PERMISSION_NAME']:
                permission = Permission.objects.get(
                    codename=code_name
                    # content_type="content_type",
                )
                new_group.permissions.add(permission)
                self.stdout.write(self.style.SUCCESS(f"Added -- {code_name}"))
        else:
            self.stdout.write(self.style.SUCCESS(f"Already have this group"))
