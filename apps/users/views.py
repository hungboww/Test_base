from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.models import UserAccountModel
from apps.users.serializers.user_serializers import UserSerializer


class UserListCreateAPIView(generics.ListCreateAPIView):
    # def get(self, request, format=None):
    #     keyword = ''
    #     param = request.GET
    #     if 'keyword' in param:
    #         keyword = param['keyword']
    #     print('param', param)
    #     users = UserAccountModel.objects.filter(client_id__name__icontains=keyword)
    #     serializer = UserSerializer(users, many=True)
    #     return Response(serializer.data)
    #
    # def post(self, request, format=None):
    #     serializer = UserSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    queryset = UserAccountModel.objects.filter(is_deleted=False)
    serializer_class = UserSerializer


class UserDetailUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = UserAccountModel.objects.filter(is_deleted=False)
    serializer_class = UserSerializer
