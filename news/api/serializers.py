from rest_framework import serializers
from ..models import Article


class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    body = serializers.CharField()
    location = serializers.CharField()
    publication_date = serializers.DateField()
    activate = serializers.BooleanField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.author = validated_data.get('author', instance.author)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.body = validated_data.get('body', instance.body)
        instance.location = validated_data.get('location', instance.location)
        instance.publication_date = validated_data.get('publication_date', instance.publication_date)
        instance.activate = validated_data.get('activate', instance.activate)
        instance.save()
        return instance

    def validate(self, attrs):
        """Check that description and title are diffrent"""
        if attrs["title"] == attrs["description"]:
            raise serializers.ValidationError("Title and desc must be different")
        return attrs

    def validate_title(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("The title has to be at least 10 chars long")
        return value