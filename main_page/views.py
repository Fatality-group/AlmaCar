from django.db.migrations import serializer
from django.http import HttpResponse
from rest_framework import viewsets, status, permissions
from rest_framework import viewsets, status, permissions, mixins, serializers
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import DetailCarSerializer, AwardSerializer, AboutCompanySerializer, RentAutoSerializer
from .models import DetailCar, Award, AboutCompany, RentCar


class DetailCarViewSet(viewsets.ModelViewSet):
    queryset = DetailCar.objects.all()
    serializer_class = DetailCarSerializer
    parser_classes = (MultiPartParser,)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly | IsAdminUser]

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [permissions.IsAdminUser]
        elif self.request.method == 'PUT':
            self.permission_classes = [permissions.IsAdminUser]
        elif self.request.method == 'DELETE':
            self.permission_classes = [permissions.IsAdminUser]
        elif self.request.method == 'LIST':
            self.permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return [permission() for permission in self.permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            response = {
                'message': 'Детальная информация о машине успешно создана',
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED, headers=headers)
        else:
            response = {
                'message': 'Детальная информация о машине не создана',
                'errors': serializer.errors
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            car = DetailCar.objects.get(pk=pk)
            serializer = DetailCarSerializer(car, data=request.data)
            if serializer.is_valid():
                serializer.save()
                response_200 = {
                    "message": "Детальная информация о машине успешно обновлена",
                }
                return Response(response_200, status=status.HTTP_200_OK)
            response_400 = {
                "message": "Детальная информация о машине не обновлена",
                "errors": serializer.errors
            }
            return Response(response_400, status=status.HTTP_400_BAD_REQUEST)
        except DetailCar.DoesNotExist:
            response_404 = {
                "message": "Машина не найдена",
            }
        return Response(response_404, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            car = DetailCar.objects.get(pk=pk)
            car.delete()
            response_200 = {
                "message": "Детальная информация о машине успешно удалена",
            }
            return Response(response_200, status=status.HTTP_200_OK)
        except DetailCar.DoesNotExist:
            response_404 = {
                "message": "Детальная информация о машине не найдена",
            }
        return Response(response_404, status=status.HTTP_404_NOT_FOUND)


class AwardViewSet(viewsets.ModelViewSet):
    queryset = Award.objects.all()
    serializer_class = AwardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly | IsAdminUser]

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [permissions.IsAdminUser]
        elif self.request.method == 'PUT':
            self.permission_classes = [permissions.IsAdminUser]
        elif self.request.method == 'DELETE':
            self.permission_classes = [permissions.IsAdminUser]
        elif self.request.method == 'LIST':
            self.permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return [permission() for permission in self.permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            response_data = {
                'message': 'Достижение успешно создано',
                'data': serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            response_data = {
                'message': 'Достижение не создано',
                'errors': serializer.errors
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            self.perform_update(serializer)
            response_data = {
                'message': 'Достижение успешно обновлено',
                'data': serializer.data
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            response_data = {
                'message': 'Достижение не обновлено',
                'errors': serializer.errors
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        response_data = {
            'message': 'Достижение успешно удалено'
        }
        return Response(response_data, status=status.HTTP_200_OK)


class AboutCompanyViewSet(viewsets.ModelViewSet):
    queryset = AboutCompany.objects.all()
    serializer_class = AboutCompanySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly | IsAdminUser]

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [permissions.IsAdminUser]
        elif self.request.method == 'PUT':
            self.permission_classes = [permissions.IsAdminUser]
        elif self.request.method == 'DELETE':
            self.permission_classes = [permissions.IsAdminUser]
        elif self.request.method == 'LIST':
            self.permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return [permission() for permission in self.permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            response_data = {
                'message': 'О компании успешно создано',
                'data': serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            response_data = {
                'message': 'О компании не создано',
                'errors': serializer.errors
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            self.perform_update(serializer)
            response_data = {
                'message': 'О компании успешно обновлено',
                'data': serializer.data
            }
            return Response(response_data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        response_data = {
            'message': 'О компании успешно удалено'
        }
        return Response(response_data, status=status.HTTP_200_OK)


class RentAutoView(viewsets.ModelViewSet):
    queryset = RentCar.objects.all()
    serializer_class = RentAutoSerializer

