from wallet.views import OrdersView, OrderView, OrderStatusView
from django.urls import path, include

wallet_urlpatterns = [
    path('order/', include([
        path('', OrdersView.as_view()),
        path('<str:original_id>/', OrderView.as_view()),
        path('<str:original_id>/status/', OrderStatusView.as_view()),
    ])),
]
