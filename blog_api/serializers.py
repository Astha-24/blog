from rest_framework import serializers
from blog_api import models

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password','about')
        extra_kwargs = {
            'password': {
                'write_only' : True,
                'style': {'input_type': 'password'}
            }
        }
        def create(self, validated_data):
            """Create and return a new user"""
            user=models.UserProfile.objects.create_user(
                email=validated_data['email'],
                name=validated_data['name'],
                password=validated_data['password'],
                about=validated_data['about']
            )

            return user

class StoryFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""
    # category = serializers.SlugRelatedField(
    #     read_only=True,
    #     slug_field='category_name'
    #  )
    class Meta:
        model = models.Story
        fields = ('id','title','content','author','category','created_on')
        extra_kwargs = {'author':{'read_only': True}}
        depth = 1
