from rest_framework import serializers

from . import models


class ShortWordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Word
        fields = ('id', 'title', 'definition', 'language')

class WordsSerializer(serializers.ModelSerializer):
    translations = ShortWordsSerializer(many=True, read_only=True)
    synonyms = ShortWordsSerializer(many=True)
    antonyms = ShortWordsSerializer(many=True)

    class Meta:
        model = models.Word
        fields = ('id', 'title', 'definition', 'language', 'url', 'translations', 'synonyms', 'antonyms')
        # fields = ('id', 'title', 'definition', 'language', 'url', 'translations')
