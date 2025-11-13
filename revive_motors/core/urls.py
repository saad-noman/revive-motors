



from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'),   
    path('shop/filtered_shop', views.filtered_shop, name='filtered_shop'),
    path('shop/car_detail/<int:car_id>', views.car_detail, name='car_detail'),
    path('shop/buy_car/<int:car_id>', views.buy_car, name='buy_car'),
    path('shop/delete_car/<int:car_id>', views.delete_car, name='delete_car'),
    path('shop/sell_car', views.sell_car, name='sell_car'),
    path('shop/update_car/<int:car_id>', views.update_car, name='update_car'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('about_us/', views.about_us, name='about_us'),
    path('shop/transaction_history', views.transaction_history, name='transaction_history'),
    path('contact_admin/', views.contact_us, name='contact_us'),
]