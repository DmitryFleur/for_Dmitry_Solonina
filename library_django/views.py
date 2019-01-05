from rest_framework import viewsets, routers
from library_django.serializers import GenreSerializer, BookSerializer, BookLocationSerializer, \
    ClientsSerializer, OrderHistorySerializer
from library_django.models import Genre, Book, BookLocation, Clients, OrderHistory
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import timedelta, datetime
from django.db.models import Count


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookLocationViewSet(viewsets.ModelViewSet):
    queryset = BookLocation.objects.all()
    serializer_class = BookLocationSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer


class OrderHistoryViewSet(viewsets.ModelViewSet):
    queryset = OrderHistory.objects.all()
    serializer_class = OrderHistorySerializer


class OutdatedOrdersViewSet(viewsets.ModelViewSet):
    """
        список абонементов, срок возврата книг которых истек.
        так как в задании не было ясно, какой срок возврата книги, мы допустим что этот срок это
        2 недели со дня взятия книги
    """
    http_method_names = ['get']
    queryset = OrderHistory.objects.filter(take_date__lte=datetime.now()-timedelta(days=14),
                                           return_date=None)
    serializer_class = OrderHistorySerializer


class ReturnStatistics(APIView):
    """
        статистика получения/возврата книг по датам
    """

    def get(self, request, format=None):
        take_grouped_by_dates = [i for i in OrderHistory.objects.values('take_date').annotate(count=Count('id'))]
        returned_grouped_by_dates = [i for i in OrderHistory.objects.exclude(return_date=None).values('return_date').annotate(count=Count('id'))]

        resp = dict()
        for date in take_grouped_by_dates:
            print(date)
            resp[date['take_date'].strftime('%Y-%m-%d')] = {'in': date['count'], 'out': 0}

        for date in returned_grouped_by_dates:
            print(date)
            if date['return_date'].strftime('%Y-%m-%d') not in resp:
                resp[date['return_date'].strftime('%Y-%m-%d')] = {'in': 0}
            resp[date['return_date'].strftime('%Y-%m-%d')]['out'] = date['count']

        return Response({'take_grouped_by_dates': take_grouped_by_dates,
                         'returned_grouped_by_dates': returned_grouped_by_dates,
                         'resp': resp})


router = routers.DefaultRouter()
router.register(r'genres', GenreViewSet)
router.register(r'books', BookViewSet)
router.register(r'book_location', BookLocationViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'order_history', OrderHistoryViewSet)
router.register(r'outdated', OutdatedOrdersViewSet)

urlpatterns = router.urls

