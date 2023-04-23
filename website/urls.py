from django.urls import path
from .views import *
app_name = 'website'
urlpatterns = [
    path('', index, name = 'index'),
    path('portfolio', portfolio_details, name = 'portfolio'),
]
