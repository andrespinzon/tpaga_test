from wallet.views import create_payment, get_purchase_details, list_transactions
from django.urls import path, include

wallet_urlpatterns = [
    path('payment/', create_payment, name='create_payment'),
    path('purchase-details/', get_purchase_details, name='get_purchase_details'),
    path('transactions/', list_transactions, name='list_transactions'),
]
