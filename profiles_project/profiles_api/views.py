from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render


class HelloAPiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'uses HTTP mothods as function (get, post, patch, put, delete',
            'Is similar to a traditional django view',
            'Gives you the most control over your appliaction logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})