from django.shortcuts import render

# Create your views here.


from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import HUser, Circle, CircleMember
from .permissions import IsHUserOwner
from .serializers import HUserRegisterSerializer,HUserUpdateSerializer
from .serializers import CircleListSerializer, CircleUpdateSerializer
from .serializers import CircleMemberListSerializer, CircleMemberSerializer



class HUserViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = HUser.objects.all()
    serializer_class = HUserRegisterSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        if self.request.method == 'DELETE':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsHUserOwner(),)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            HUser.objects.create_user(**serializer.validated_data)
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

        print serializer.errors

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def update(self, request, id=None):
    #     print request
    #     print "id is {}".format(id)

    #     serializer = self.serializer_class(data=request.data)
    #     if serializer.is_valid():
    #         print "valid"
    #         return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
    #     print serializer.errors
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HUserEditViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = HUser.objects.all()
    serializer_class = HUserUpdateSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        if self.request.method == 'PUT':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsHUserOwner(),)


class CircleListViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Circle.objects.all()
    serializer_class = CircleListSerializer


    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        if self.request.method == 'DELETE':
            return (permissions.AllowAny(),)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        print("I am inside of create call")
        if serializer.is_valid():

            Circle.objects.create_circle(**serializer.validated_data)
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

        print serializer.errors

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CircleEditViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Circle.objects.all()
    serializer_class = CircleUpdateSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        if self.request.method == 'PUT':
            return (permissions.AllowAny(),)

        if self.request.method == 'DELETE':
            return (permissions.AllowAny(),)


class CircleMemberListViewSet(viewsets.ModelViewSet):
    queryset = CircleMember.objects.all()
    serializer_class = CircleMemberListSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        if self.request.method == 'DELETE':
            return (permissions.AllowAny(),)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        print("I am inside of create call")
        if serializer.is_valid():

            CircleMember.objects.create_circlemember(**serializer.validated_data)
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

        print serializer.errors

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CircleMemberEditViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = CircleMember.objects.all()
    serializer_class = CircleMemberSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        if self.request.method == 'POST':
            return (permissions.AllowAny(),)
        if self.request.method == 'PUT':
            return (permissions.AllowAny(),)

        if self.request.method == 'DELETE':
            return (permissions.AllowAny(),)