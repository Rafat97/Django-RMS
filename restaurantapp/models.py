from django.db import models


class Restaurant(models.Model):
    id = models.BigAutoField(primary_key=True)
    restaurant_name = models.CharField(
        max_length=30, blank=False, help_text="Give a Restaurant Name")
    restaurant_description = models.CharField(
        max_length=500, blank=True, help_text="Give a Short Description of Restaurant")
    restaurant_start_time = models.TimeField(
        blank=True, help_text="Restaurant Opening time")
    restaurant_off_time = models.TimeField(
        blank=True, help_text="Restaurant Closing time")
    is_open = models.BooleanField(
        default=False, help_text="Is Restaurant Open Currently")
    meta_data = models.JSONField(null=True, default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.restaurant_name


class Menu(models.Model):
    id = models.BigAutoField(primary_key=True)
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.SET_NULL, null=True, help_text="Relation of Restaurant")
    is_active = models.BooleanField(
        default=False, help_text="Is Restaurant Open Currently")
    meta_data = models.JSONField(null=True, default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.restaurant.restaurant_name + " -- " + str(self.created_at) + " -- " + str(self.id)

    def save(self, *args, **kwargs):
        if self.id:
            find = Menu.objects.get(id__exact=self.id)
            if find.is_active == self.is_active:
                super().save(*args, **kwargs)
            else:
                find2 = Menu.objects.filter(
                    restaurant=self.restaurant, is_active__exact=True)
                if find2:
                    find2.update(is_active=False)
        else:
            find2 = Menu.objects.filter(
                restaurant=self.restaurant, is_active__exact=True)
            if find2:
                find2.update(is_active=False)

        super().save(*args, **kwargs)


class Item(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500, blank=True)
    menu = models.ForeignKey(
        Menu,  on_delete=models.SET_NULL, null=True, help_text="Relation of Menu")
    is_available = models.BooleanField(
        default=True, help_text="This item is available or not")
    meta_data = models.JSONField(null=True, default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
