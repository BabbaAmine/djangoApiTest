from django.contrib.auth.models import User
from rest_framework import serializers
from .models import messaging
from .models import rooms
from .models import friends
from rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter
from rest_auth.serializers import UserDetailsSerializer

class MyRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    def get_cleaned_data(self):
        super(MyRegisterSerializer, self).get_cleaned_data()
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', '')
}
    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        return user

class CustomUserDetailsSerializer(UserDetailsSerializer):
    phone = serializers.CharField(source="profile.phone")
    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ('phone',)
    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', {})
        phone = profile_data.get('phone')
        instance = super(CustomUserDetailsSerializer, self).update(instance, validated_data)

        profile = instance.profile
        if profile_data and phone:
            profile.phone = phone
        profile.save()
        return instance


class messagingSerializer(serializers.ModelSerializer):
    class Meta:
        model = messaging
        fields = '__all__'

class roomSerializer(serializers.ModelSerializer):
    class Meta:
        model = rooms
        fields = '__all__'

class freindsSerializer(serializers.ModelSerializer):
    class Meta:
        model = friends
        fields = '__all__'

class userSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

