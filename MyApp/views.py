from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import messaging
from .models import rooms
from .models import friends
from .serializers import messagingSerializer
from .serializers import roomSerializer
from .serializers import freindsSerializer
from .serializers import userSerializers
from django.db.models import Q
from django.contrib.auth.models import User

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
def getLastRoomMsg(request,idroom):
    if request.method == 'GET':
        msgs = messaging.objects.filter(idRoom=idroom).latest('idmsg')
        serializer = messagingSerializer(msgs, context={'request': request}, many=False)
        data = {}
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
        freind= friends.objects.get(id=iduser)
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

@api_view(['GET'])
def getUsersByEmail_Nom_Prenom(request,text):
    if request.method == 'GET':
        listOfUsers = User.objects.filter(Q(email__contains=text) | Q(first_name__contains=text) | Q(last_name__contains=text))
        serializer = userSerializers(listOfUsers, context={'request': request}, many=True)
        data = {}
        data['list'] = serializer.data
        data['total'] = len(serializer.data)
        return Response(data)

@api_view(['GET'])
def getAllUsers(request):
    if request.method == 'GET':
        listOfUsers = User.objects.all()
        serializer = userSerializers(listOfUsers, context={'request': request}, many=True)
        data = {}
        data['list'] = serializer.data
        data['total'] = len(serializer.data)
        return Response(data)

@api_view(['GET'])
def getUserDetails(request,iduser):
    if request.method == 'GET':
        user = User.objects.get(id=iduser)
        serializer = userSerializers(user, context={'request': request}, many=False)
        data = {}
        data['user'] = serializer.data
        return Response(data)

@api_view(['GET'])
def getRoomDetails(request,idroom,currentuser):
    if request.method == 'GET':
       data = {}
       r = rooms.objects.get(idRoom=idroom)
       room = roomSerializer(r,context={'request': request}, many=False).data
       data['room']=room.data
       if(currentuser != room['idUser1']):
           user = User.objects.get(id=room['idUser1'])
           data['user'] = userSerializers(user, context={'request': request}, many=False).data
       if(currentuser != room['idUser2']):
           user = User.objects.get(id=room['idUser2'])
           data['user'] = userSerializers(user, context={'request': request}, many=False).data
       if( messaging.objects.filter(idRoom=room['idRoom']).exists() == True):
           msg = messaging.objects.filter(idRoom=room['idRoom']).latest('idmsg')
           data['message']=messagingSerializer(msg, context={'request': request}, many=False).data
       else:
           data['message']={}
       return Response(data)





