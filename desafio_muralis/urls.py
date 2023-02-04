from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers
from rest_framework.authtoken.views import obtain_auth_token

from desafio_muralis.funcionario.api.viewsets import FuncionarioAPI
from desafio_muralis.funcionario_fabrica.api.viewsets import FuncionarioFabricaAPI

schema_view = get_schema_view(
    openapi.Info(
      title="Desafio Muralis APIs",
      default_version='v1',
      description="Projeto de desafio da muralis",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="barros.ismael@outlook.com"),
      license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)


router = routers.DefaultRouter()
router.register('funcionario', FuncionarioAPI)
router.register('funcionario-fabrica', FuncionarioFabricaAPI)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', obtain_auth_token),
    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger'), name='schema-swagger-ui'),
    path('', schema_view.with_ui('redoc', cache_timeout=0), name='index'),
]
