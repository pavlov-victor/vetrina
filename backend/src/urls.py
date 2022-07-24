from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Vetrina api",
        default_version='v1',
        description="API for Vetrina",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="vitek@goykt.ru"),
        license=openapi.License(name="BSD License"),
    ),
    url='http://localhost:8899',
    public=True,
    permission_classes=[permissions.AllowAny],
)

api_urls = [
    path('', include('users.api_urls')),
    path('', include('shops.api_urls')),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urls))
]
