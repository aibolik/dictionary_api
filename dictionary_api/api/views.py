from rest_framework import viewsets
from rest_framework import filters

from . import forms
from . import models

class WordsEnglishViewSet(viewsets.ModelViewSet):
    queryset = models.Word.objects.all()
    serializer_class = forms.WordsSerializer

    def get_queryset(self):
        # language = self.kwargs['language']
        # print(language)
        return models.Word.objects.filter(language='en')

class WordsRussianViewSet(viewsets.ModelViewSet):
    queryset = models.Word.objects.all()
    serializer_class = forms.WordsSerializer

    def get_queryset(self):
        # language = self.kwargs['language']
        # print(language)
        return models.Word.objects.filter(language='ru')

class WordsKazakhViewSet(viewsets.ModelViewSet):
    queryset = models.Word.objects.all()
    serializer_class = forms.WordsSerializer

    def get_queryset(self):
        # language = self.kwargs['language']
        # print(language)
        return models.Word.objects.filter(language='kz')

class WordsViewSet(viewsets.ModelViewSet):
    serializer_class = forms.WordsSerializer
    queryset = models.Word.objects.all()

    # def get_queryset(self):
    #     queryset = models.Word.objects.all()
    #     language = self.request.query_params.get('translate', None)
    #     if language is not None:
    #         queryset = queryset.filter(translations__language=language)
    #     return queryset

    # filter_backends = (filters.DjangoFilterBackend,)
    # filter_fields = ('title', 'language')
