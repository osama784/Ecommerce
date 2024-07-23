from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/', views.product, name='product'),
    path('cart/', views.cart, name="cart"),
    path('shop/', views.shop, name="shop"),
    path('vendor-name/', views.vendor, name='vendor'),
    path('about-us/', views.about_us, name='about-us'),
    path('contact/', views.contact, name='contact'),
    path('purchase-guide/', views.purchase_guide, name='purchase-guide'),
    path('terms-of-service/', views.terms_of_service, name='terms-of-service'),
    path('privacy-policy/', views.privacy_policy, name='privacy-policy'),
    path('dashboard/', views.user_info, name='user-info')
    
]