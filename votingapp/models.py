from django.db import models
from django.contrib.auth.models import User, Group
from restaurantapp.models import Restaurant,Menu

# Create your models here.

class Vote(models.Model):
    id = models.BigAutoField(primary_key=True)
    restaurant_menu = models.ForeignKey(
        Menu, on_delete=models.SET_NULL, null=True, help_text="Relation with Restaurant")
    User = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, help_text="Relation with User")
    vote_type =  models.BigIntegerField(default=1)
    meta_data = models.JSONField(null=True, default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
