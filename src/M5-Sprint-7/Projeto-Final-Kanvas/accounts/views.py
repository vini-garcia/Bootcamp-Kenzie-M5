from rest_framework.generics import ListCreateAPIView

from accounts.models import Account
from accounts.serializers import AccountSerializer


class AccountView(ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
