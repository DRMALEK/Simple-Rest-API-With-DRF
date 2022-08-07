from http.client import HTTPResponse
from django.http import JsonResponse, HttpResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET', 'POST'])
def drink_list(request):
    if request.method == 'GET':
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        return JsonResponse({"drinks": serializer.data}, safe=False)

    if request.method == 'POST':
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"drinks": serializer.data}, safe=False, status=status.HTTP_201_CREATED)