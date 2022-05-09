from django.forms import ValidationError
from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = '__all__'

    def validate_title(self, value):
        if value == 'rio':
            raise ValidationError('No rio please')
        return value

    def validate(self, attrs):
        if attrs['number_of_pages'] >= 200 and attrs['quantity'] >= 200:
            raise ValidationError('Too heavy for inventory')
        return super().validate(attrs)

    def get_description(self, data):
        return f'This book is called {data.title} and it is {data.number_of_pages} long.'
