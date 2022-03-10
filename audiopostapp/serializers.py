from rest_framework import serializers
from audiopostapp.models import AudioLanguage, AudioPost, AudioTag

class AudioLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioLanguage
        fields = "__all__"

class AudioPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioPost
        fields = "__all__"

class AudioTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioTag
        fields = "__all__"