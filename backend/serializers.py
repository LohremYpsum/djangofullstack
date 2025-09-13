from rest_framework import serializers
from .models import User, MusicAd, AdCategory, WatchlistItem

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class AdCategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the AdCategory model.
    """
    class Meta:
        model = AdCategory
        fields = '__all__'

class MusicAdSerializer(serializers.ModelSerializer):
    """
    Serializer for the MusicAd model.
    """
    user = UserSerializer(read_only=True)
    categories = AdCategorySerializer(many=True, read_only=True)
    
    class Meta:
        model = MusicAd
        fields = '__all__'

class WatchlistItemSerializer(serializers.ModelSerializer):
    """
    Serializer for the WatchlistItem model, which links a User to a MusicAd.
    """
    ad = MusicAdSerializer(read_only=True)
    
    class Meta:
        model = WatchlistItem
        fields = ['id', 'user', 'ad', 'added_at']
        read_only_fields = ['added_at']