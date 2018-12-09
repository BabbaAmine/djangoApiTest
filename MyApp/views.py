from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import messaging
from .models import rooms
from .models import friends
from .serializers import messagingSerializer
from .serializers import roomSerializer
from .serializers import freindsSerializer
from django.db.models import Q

#Model messaging api methods
@api_view(['POST'])
def addMsgToRoom(request):
    if request.method == 'POST':
        serializer = messagingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getRoomMsgs(request,idroom):
    if request.method == 'GET':
        msgs = messaging.objects.filter(idRoom=idroom)
        serializer = messagingSerializer(msgs, context={'request': request}, many=True)
        data={}
        data['list'] = serializer.data
        data['total'] = len(serializer.data)
        return Response(data)

@api_view(['GET'])
def getUserRooms(request,iduser):
    if request.method == 'GET':
        listOfRooms = rooms.objects.filter(Q(idUser1=iduser) | Q(idUser2=iduser))
        serializer = roomSerializer(listOfRooms, context={'request': request}, many=True)
        data = {}
        data['list'] = serializer.data
        data['total'] = len(serializer.data)
        return Response(data)

@api_view(['POST'])
def addRoom(request):
    if request.method == 'POST':
        serializer = roomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def addFreind(request):
    if request.method == 'POST':
        serializer = freindsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def accept_ignore_Freind(request,iduser):
    try:
        freind= friends.objects.get(idUser=iduser)
    except friends.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = freindsSerializer(freind, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getUserFreinds(request,iduser):
    if request.method == 'GET':
        listOfFreinds = friends.objects.filter(Q(senderId=iduser) | Q(receiverId=iduser))
        serializer = freindsSerializer(listOfFreinds, context={'request': request}, many=True)
        data = {}
        data['list'] = serializer.data
        data['total'] = len(serializer.data)
        return Response(data)



