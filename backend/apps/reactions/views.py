from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet

from .models import PostMeta


class PostMetaView(ModelViewSet):
    class PostMetaSerializer(ModelSerializer):
        class Meta:
            model = PostMeta
            fields = '__all__'

    queryset = PostMeta.objects.all()
    serializer_class = PostMetaSerializer

    @action(detail=True, methods=['post'], url_name='add', url_path='add')
    def add_reaction(self, request, pk):
        obj = get_object_or_404(PostMeta, id=pk)
        obj.add_emoji(request.POST.get('emoji_id', None))
        return Response(PostMetaView.PostMetaSerializer(obj).data)
