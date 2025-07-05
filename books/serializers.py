from rest_framework import serializers, status
from rest_framework.exceptions import ValidationError

from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, data):
        title = data.get('title')
        author = data.get('author')

        # chech title if it contains only alphabet
        if not all(char.isalpha() or char.isspace() for char in title):
            raise ValidationError(
                {
                    "status": False,
                    "message" : "Kitobning nomi va avtori harflardan tashkil topgan bo`lishi kerak!",
                }
            )

        # check title and author from db is exists
        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError(
                {
                    "status": False,
                    "message": "Ushbu kitob allaqachon mavjud!"
                }
            )

        return data

    def validate_price(self, value):
        if value <= 0:
            raise ValidationError(
                {
                    "status": False,
                    "message": "Narx musbat bo'lishi kerak!"
                }
            )
        return value