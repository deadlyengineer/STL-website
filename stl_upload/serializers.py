from django.db.models.fields import PositiveBigIntegerField
from rest_framework import serializers
from .models import UserProcess

class UserProcessSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserProcess
    fields = ['user', 'center_x', 'center_y', 'center_z', 'orientation_x', 'orientation_y', 'orientation_z', 'opacity', 'filename']