from rest_framework import serializers

from posts.models import *


class PostSerializer(serializers.ModelSerializer):
    # to set a readOnly field we use serializers.ReadOnlyField(source = where the data will come from)
    poster = serializers.ReadOnlyField(source='poster.username')
    poster_id = serializers.ReadOnlyField(source='poster.id')

    class Meta:
        model = Post
        fields = ['id', 'title', 'url', 'poster_id', 'poster', 'created']

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id']