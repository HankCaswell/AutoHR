from django.urls import path
from .views import UserCreate, UnitCreate

urlpatterns = [
    path('register/', UserCreate.as_view(), name='user-create'),
    path('unit/', UnitCreate.as_view(), name='unit-create'),

]