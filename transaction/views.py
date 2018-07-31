from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .serializers import TransactionModelSerializer
from .models import Transaction
from rest_framework.decorators import list_route, detail_route
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from .money_wave_utils import *


class TransactionModelViewSet(ModelViewSet):
    model = Transaction
    serializer_class = TransactionModelSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user).order_by('-modified_on')

    @list_route(methods=['post'])
    def get_banks(self, request):
        """
        get all banks for selected country
        :param request:
        :return:  <Response Object>
        """
        country = self.request.data['country']
        banks = get_banks(country)
        return Response({"banks": banks}, status=status.HTTP_200_OK)

    @list_route(methods=['post'])
    def resolve_account(self, request):
        """
        resolve an account
        :param request:
        :return:
        """
        print(request.data)
        bank_code = request.data['bank_code']
        account_number = request.data['account_number']
        currency = request.data['country']
        resolve = resolve_account(account_number, bank_code, currency)
        if resolve:
            return Response({"account": resolve}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)



