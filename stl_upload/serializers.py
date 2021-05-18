from rest_framework import serializers
from .models import UserProcess, UserStl

class UserProcessSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserProcess
    fields = ['user', 'center_x', 'center_y', 'center_z', 'orientation_x', 'orientation_y', 'orientation_z', 'opacity', 'filename']



class UploadStlSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserStl
    fields = ['user', 'file']