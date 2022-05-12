from rest_framework import serializers


class BalancesSerializer(serializers.Serializer):
    """
    Serialize the Balances
    """
    balance = serializers.CharField()
