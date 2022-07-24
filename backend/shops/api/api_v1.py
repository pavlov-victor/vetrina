from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import MultiPartParser

from shops.models import Market, MarketTag, MarketItem
from shops.serializers import PublicMarketListSerializer, UserMarketListCreateSerializer, TagSerializer, \
    UserMarketDetailSerializer, MarketItemListSerializer, UserMarketItemListCreateSerializer, \
    UserMarketItemDetailSerializer


class MarketAllListAPIView(ListAPIView):
    queryset = Market.objects.all().prefetch_related('tags')
    serializer_class = PublicMarketListSerializer
    search_fields = ['tags__name', 'name']
    filterset_fields = ['tags']
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]


class UserMarketListCreateAPIView(ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserMarketListCreateSerializer
    parser_classes = (MultiPartParser,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Market.objects.filter(owner=self.request.user)


class UserMarketDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserMarketDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Market.objects.filter(owner=self.request.user)


class TagsListAPIView(ListAPIView):
    queryset = MarketTag.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    serializer_class = TagSerializer


class MarketItemListAPIView(ListAPIView):
    serializer_class = MarketItemListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name']
    filterset_fields = ['market']

    def get_queryset(self):
        return MarketItem.objects.all()


class UserMarketItemListCreateAPIView(ListCreateAPIView):
    serializer_class = UserMarketItemListCreateSerializer

    def perform_create(self, serializer):
        serializer.save(market_id=self.kwargs['market_pk'])

    def get_queryset(self):
        return MarketItem.objects.filter(market__owner=self.request.user, market_id=self.kwargs['market_pk'])


class UserMarketItemDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserMarketItemDetailSerializer

    def get_queryset(self):
        return MarketItem.objects.filter(market__owner=self.request.user, market_id=self.kwargs['market_pk'])
