from django.urls import path
from . import views

app_name = "kobosh"

urlpatterns = [
    path('payment/', views.payment, name='payment'),
    path('thebasement/', views.home, name='thebasement'),
    path('', views.home, name='home'),
    path('categories/', views.home, name='cate'),
    path('search/', views.search, name='search'),
    path('<slug:category_slug>/', views.home, 
        name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,
        name = 'product_detail'),
]