from django.urls import path
from .views import UserCreate, UnitCreate, UnitListView, EquipmentSummaryView, EquipmentDetailView, AddToCartView, CartView, CheckoutView, ReturnEquipmentView

urlpatterns = [
    path('register/', UserCreate.as_view(), name='user-create'),
    path('unit/', UnitCreate.as_view(), name='unit-create'),
    path('unit/all/', UnitListView.as_view(), name='unit-list'),
    path('equipment-summary/', EquipmentSummaryView.as_view(), name='equipment-summary'), 
    path('equipment/<int:equipment_id>/', EquipmentDetailView.as_view(), name='equipment-detail'),
    path('cart/', CartView.as_view(), name='cart'),
    path('equipment/add-to-cart/', AddToCartView.as_view(), name='add-to-cart'),
    path('equipment/checkout/', CheckoutView.as_view(), name='checkout'),
    path('equipment/return/', ReturnEquipmentView.as_view(), name='return-equipment'),
    
]