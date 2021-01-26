from django.shortcuts import render
from django.http import JsonResponse
import requests

# Create your views here.
def index(request):
    response = requests.get('https://sls.api.stw-on.de/v1/location')
    return JsonResponse(response.json(), safe=False)

