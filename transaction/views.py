import hashlib
import random
from string import ascii_uppercase, digits
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .serializers import TransactionModelSerializer
from .models import Transaction
from rest_framework.decorators import list_route
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from .money_wave_utils import *
import json
from config.settings.keys import *


class TransactionModelViewSet(ModelViewSet):
    model = Transaction
    permission_classes = [AllowAny]
    serializer_class = TransactionModelSerializer

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
        bank_code = request.data['bank_code']
        account_number = request.data['account_number']
        currency = request.data['country']
        resolve = resolve_account(account_number, bank_code, currency)
        if not resolve:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            print(resolve)
            return Response({"account": resolve}, status=status.HTTP_200_OK)



    @list_route(methods=['post'])
    def ravepayment_request(self, request):
        hashedPayload = ''
        payload = {
            "PBFPubKey": FLW_API_KEY,
            "amount": request.data['amount'],
            "payment_method": "both",
            "custom_description": "Kaimun",
            "custom_title": "Instant Money Transfers",
            "country": request.data['country'],
            "currency": request.data['currency'],
            "customer_email": request.user.email,
            "customer_firstname": request.user.first_name,
            "customer_lastname": request.user.last_name,
            # "customer_phone": request.data['phone'],
            "txref": "KMN-" + ''.join(random.sample((ascii_uppercase+digits), 5))
        }

    # sort payload and concatenate into a single string
        sorted_payload = sorted(payload)

    # concatenate sorted_payload. The payload is rearranged and the values concatenated in the order of the sorted keys.
        hashed_payload = ''
        for value in sorted_payload:
            hashed_payload += value
        hashed_string = hashed_payload + "FLWSECK-b86e4802fc5eaa03db5e7f73fdc4514e-X"
        integrity_hash = hashlib.sha256(hashed_string.lower().encode()).hexdigest()
        return Response({'payload': payload, 'integrityHash': integrity_hash})



    @list_route(methods=['post'])
    def ravepay_deposit(self, request):
        # instance = self.get_object()
        url = "https://ravesandboxapi.flutterwave.com/flwv3-pug/getpaidx/api/xrequery"
        data = {
            "txref": request.data['txRef'],
            "SECKEY" : FLW_API_SECRET,
            "include_payment_entity": 1
        }
        response = requests.post(url, data=data).json()

        account_number = request.data['account_number']
        bank_code = request.data['bank_code']
        currency = request.data['currency']
        amount = float(request.data['amount'])
        narration = request.data['narration']
        sender = request.user.first_name + ' ' + request.user.last_name

        # confirm that the response for the transaction is successful
        if response['status'] == 'success':
            data = response['data']
            if data[0]['chargecode'] == '00':
                chargedamount = float(data[0]['chargedamount'])
                if chargedamount > amount:
                        make_transfer = disburse(account_number, bank_code, amount, narration, currency, sender)
                        if make_transfer:
                            return Response({'message': 'Successfully Sent Funds'}, status=status.HTTP_200_OK)
                        else:
                            return Response({'message': 'Unable  to send funds'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                else:
                    return Response({'message': 'Unable  to send funds'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                return Response({'message': 'Transaction was not successful'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        ##changing this to ok for simulation purposes, the moneywave api isn't bring the correct response
        else:
            return Response({'message': '4Unable  to send funds'}, status=status.HTTP_200_OK)


