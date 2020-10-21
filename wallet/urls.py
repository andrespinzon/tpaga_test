from wallet.views import OrdersView
from django.urls import path, include

wallet_urlpatterns = [
    path('order/', OrdersView.as_view()),
    # path('purchase-details/', get_purchase_details, name='get_purchase_details'),
    # path('transactions/', list_transactions, name='list_transactions'),
]
