from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'categorias', views.CategoriasViewSet)


urlpatterns = [
    # path('contact/<str:name>/', views.contact, name='contact'),
    # path('categorias/', views.categorias, name='categorias'),
    # path('productos/', views.productoFormView, name='productos'),
    # path('saludo/', views.index),
    # path('', include(router.urls))
    path('categorias/', views.CategoriaCreateView.as_view()),
    path('categorias/cantidad/', views.categoria_count),
    path('productos/filrar/unidades/', views.productos_en_unidades),
    path('productos/reporte/', views.reporte_productos),
    path('contact/', views.enviar_mensaje),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
