from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ReadOnlyUserSerializer, WriteOnlyUserSerializer
from .models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class ApiTokenAuth(ObtainAuthToken):
    """
    API for obtaining an Authentication Token
    """
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


class UsersView(APIView):
    """
    API for viewing all of the users via GET-request
    or creating a new user via POST-request
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = User.objects.all()
        serializer = ReadOnlyUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WriteOnlyUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=400)


class UsersViewById(APIView):
    """
    API for viewing, updating (including partial update)
    or deleting a specific user
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        user = User.objects.get(id=pk)
        serializer = ReadOnlyUserSerializer(user, many=False)
        return Response(serializer.data)

    def put(self, request, pk):
        user = User.objects.get(id=pk)
        serializer = WriteOnlyUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=400)

    def patch(self, request, pk):
        user = User.objects.get(id=pk)
        serializer = WriteOnlyUserSerializer(
            user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=400)

    def delete(self, request, pk):
        user = User.objects.get(id=pk)
        user.delete()
        return Response(status=204)
