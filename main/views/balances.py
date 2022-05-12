from django.core.exceptions import EmptyResultSet
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from main.serializers.balances_serializers import BalancesSerializer
from main.services.balances_service import get_balances, check_input_network, check_input_address


class BalancesView(APIView):
    @permission_classes([IsAuthenticated])
    def post(self, *args, **kwargs):
        """
        Get network and address and return the balance.
        """
        try:
            network = check_input_network(self.request.data.get('network', None))
            if not network:
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data={"message": "The network is not correct or not listed"})
            address = check_input_address(self.request.data.get('address', None))
            if not address:
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data={"message": "The address is not correct"})
            balance = get_balances(address, network)
            if balance:
                serializer = BalancesSerializer({"balance": balance})
                return Response(status=status.HTTP_200_OK, data=serializer.data)
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"message": "The was en error in connecting to network"})

        except EmptyResultSet:
            return Response(status=status.HTTP_404_NOT_FOUND)
