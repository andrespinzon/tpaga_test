from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK

from wallet.services import OrdersService


class OrdersView(APIView):

    def post(self, request: Request) -> Response:
        service = OrdersService()
        data = service.create_order_from_view(data=request.data)
        return Response(data=data, status=HTTP_201_CREATED)

    def get(self, request: Request) -> Response:
        data = OrdersService.get_all()
        return Response(data=data, status=HTTP_200_OK)
