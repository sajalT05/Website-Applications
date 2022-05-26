from mainApp.models import apiItems
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import apiItemserializers

@api_view(['GET'])
def getData(request):
    items=apiItems.objects.all()
    serializer=apiItemserializers(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postData(request):
    serializer=apiItemserializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

