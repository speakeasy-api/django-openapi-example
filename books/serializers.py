from drf_spectacular.utils import extend_schema_field, OpenApiTypes
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        published_date = serializers.SerializerMethodField()

    @extend_schema_field(OpenApiTypes.DATETIME)
    def get_field_custom(self, object):
        return '2020-03-06 20:54:00.104248'