from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer, SerializerMethodField, IntegerField, Serializer
from rest_framework.viewsets import ModelViewSet, ViewSet

from .models import PostMeta


class PostMetaSerializer(ModelSerializer):
    class Meta:
        model = PostMeta
        fields = '__all__'


class PostMetaUpdateEmojiSerializer(serializers.Serializer):
    emoji_key = serializers.IntegerField(min_value=1, max_value=4)


class PostMetaEmojiSerializer(Serializer):
    emoji = SerializerMethodField()

    def get_emoji(self, obj):
        return {'yes': 3}

    class Meta:
        model = PostMeta
        fields = ('emoji',)


class PostMetaView(ModelViewSet):
    queryset = PostMeta.objects.all()
    serializer_class = PostMetaSerializer

    @action(detail=True, methods=['post'], url_name='add', url_path='add')
    def add_reaction(self, request, pk):
        obj = get_object_or_404(PostMeta, id=pk)
        obj.add_emoji(request.POST.get('emoji_id', None))
        return Response(PostMetaSerializer(obj).data)


class PostMetaView2(ViewSet):
    def list(self, request):
        queryset = PostMeta.objects.all()
        serializer = PostMetaEmojiSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = PostMeta.objects.get_or_create(post_key=pk)
        serializer = PostMetaSerializer(queryset[0])
        return Response(serializer.data)

    def update(self, request, pk=None):
        data = PostMetaUpdateEmojiSerializer(data=request.data)
        data.is_valid(raise_exception=True)

        queryset = PostMeta.objects.all()
        obj = get_object_or_404(queryset, post_key=pk)
        obj.add_emoji(data.validated_data.get('emoji_key'))
        serializer = PostMetaSerializer(obj)
        return Response(serializer.data)
