from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from .models import User, Client
from .serializers import UserSerializer, ClientSerializer

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permissions_classes = (permissions.AllowAny, )

class UserLoginView(ObtainAuthToken):
    def post(self,request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = response.data.get('token')
        user = User.objects.get(id=response.data.get('user_id'))
        client = Client.objects.get(user=user)
        serializer = ClientSerializer(client)
        return Response({'token':token,'user':serializer.data})
    
class UserProfileView(APIView):
    permission_classes = (permissions.IsAuthenticated, )
    def get(self, request, *args, **kwargs):
        client = Client.objects.get(user=request.user)
        serializer = ClientSerializer(client)
        return Response(serializer.data)
    
