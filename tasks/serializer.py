#creamos una clase
from rest_framework import serializers
from .models import Task
import re
from datetime import datetime

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
    
    def validate_title(self, value):
        if not value:
            raise serializers.ValidationError({"status": "Bad Request", "detail": "Title must not be empty."})
        if len(value) > 50:
            raise serializers.ValidationError({"status": "Bad Request", "detail": "The length of 'Title' must be 50 characters or fewer."})
        if not re.match(r'^[\w\s]+$', value):
            raise serializers.ValidationError({"status": "Bad Request", "detail": "Title contains invalid characters. Only letters, numbers, and spaces are allowed."})
        return value
