from rest_framework import serializers
from .models import Product, Lead
from django.contrib.auth import get_user_model


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ['id', 'name', 'email', 'phone_number', 'interested_products', 'created_at']

    def validate(self, data):
        if not data.get('name') or not data.get('email'):
            raise serializers.ValidationError({
                'name': 'Name is required.',
                'email': 'Email is required.'
            })
        return data

User=get_user_model()
class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)

    class Meta:
        model=User
        fields=('id','username','password','email')
    
    def create(self,validated_data):
        return User.objects.create_user(**validated_data)
    




