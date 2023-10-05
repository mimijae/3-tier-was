from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Fruit
from .serializers import FruitSerializer

@api_view(['GET', 'POST'])
def fruit_list(request):
    if request.method == 'GET':
        fruits = Fruit.objects.all()
        serializer = FruitSerializer(fruits, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FruitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
