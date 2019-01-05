from rest_framework import serializers
from library_django.models import Genre, BookLocation, Book, Clients, OrderHistory


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class BookLocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BookLocation
        fields = '__all__'


class BookSerializer(serializers.HyperlinkedModelSerializer):
    genre = GenreSerializer(read_only=True)
    location = BookLocationSerializer(read_only=True)

    class Meta:
        model = Book
        fields = '__all__'


class ClientsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Clients
        fields = '__all__'


class OrderHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderHistory
        fields = '__all__'
