from rest_framework import serializers
from .models import *


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = "__all__"
