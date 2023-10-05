from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Fruit
from .serializers import FruitSerializer

@api_view(['GET', 'POST'])
def fruit_list(request):
    if request.method == 'GET':
        fruit_name = request.query_params.get('name')
        if fruit_name:
            fruits = Fruit.objects.filter(name=fruit_name)
        else:
            fruits = Fruit.objects.all()
        serializer = FruitSerializer(fruits, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        message = request.data.get('fruit')
        
        # ready 메시지가 오면 ok로 응답
        if message == 'ready':
            return Response({'message': 'ok'}, status=status.HTTP_200_OK)

        serializer = FruitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': f'{serializer.instance.name} has been added.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
