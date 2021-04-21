from rest_framework import serializers
from .models import categories,desserts

class categoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = categories
        fields = '__all__'


class dessertSerializer(serializers.ModelSerializer):
    class Meta:
        model = desserts
        fields = '__all__'