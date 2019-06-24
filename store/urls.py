from django.urls import path


from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name="search"),
    path('<int:device_id>/', views.detail, name="detail"),
    path('cart/', views.cart, name="cart"),
    ]