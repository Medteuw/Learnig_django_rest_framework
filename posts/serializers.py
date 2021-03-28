from rest_framework import serializers

from posts.models import *


class PostSerializer(serializers.ModelSerializer):
    # to set a readOnly field we use serializers.ReadOnlyField(source = where the data will come from)
    poster = serializers.ReadOnlyField(source='poster.username')
    poster_id = serializers.ReadOnlyField(source='poster.id')
    votes = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'url', 'poster_id', 'poster', 'created','votes']

    def get_votes(self,post):
        return Vote.objects.filter(post=post).count()

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id']