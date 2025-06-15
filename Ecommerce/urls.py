from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import register, user_login, user_logout

urlpatterns = [
    path('', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order'),
    path('search/', views.product_search, name='product_search'),
    path('add_product/', views.add_product, name='add_product'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)