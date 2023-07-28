from django.urls import path
from .views import index, top_sellers

urlpatterns = [
    path('', index, name='main-page'),
    path('top-sellersssss', top_sellers, name='top-sellers')
]



