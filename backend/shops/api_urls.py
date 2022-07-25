from django.urls import path, include

from shops.api.api_v1 import MarketAllListAPIView, UserMarketListCreateAPIView, TagsListAPIView, \
    UserMarketDetailAPIView, MarketItemListAPIView, UserMarketItemListCreateAPIView, UserMarketItemDetailAPIView

api_v1 = [
    path('markets/', MarketAllListAPIView.as_view(), name='markets-list'),
    path('markets/me/', UserMarketListCreateAPIView.as_view(), name='markets-me-list-create'),
    path('markets/me/<pk>/', UserMarketDetailAPIView.as_view(), name='markets-me-detail'),
    path('markets/tags/', TagsListAPIView.as_view(), name='markets-tags-list'),
    path('markets/items/', MarketItemListAPIView.as_view(), name='markets-items-list'),
    path(
        'markets/me/<market_pk>/items/',
        UserMarketItemListCreateAPIView.as_view(),
        name='markets-me-items-list-create'
    ),
    path(
        'markets/me/<market_pk>/items/<pk>/',
        UserMarketItemDetailAPIView.as_view(),
        name='markets-me-items-detail'
    ),
]

urlpatterns = [
    path('v1/', include(api_v1))
]
