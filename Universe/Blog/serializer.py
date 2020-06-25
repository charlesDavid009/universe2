from rest_framework import serializers
from Blog.models import Items

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Iteems
        field = ['title ', 'picture', 'details', 'author', 'likes', 'created_at']

    def  create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data,get('title', instance.title)
        instance.picture = validated_data, get('picture', instance.picture)
        instance.details = validated_data, get('details', instance.details)
        instance.author = validated_data, get('author', instance.author)
        instance.likes = validated_data, get('likes ', instance.likes)
        intsance.created_at = validated_data.get('created_at', instance.created_at)
        instance.save()
        return instance

