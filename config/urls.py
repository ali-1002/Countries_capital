from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from rest_framework import permissions
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("countries.urls")),
]

schema_view = get_schema_view(
    openapi.Info(
        title="API hujjati",
        default_version='v1',
        description="Bu API hujjatlari Swagger orqali avtomatik generatsiya qilinadi.",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)