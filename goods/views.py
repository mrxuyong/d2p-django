from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from models import Goods
import json
from pprint import pprint


# Create your views here.
def index(request):
    token = request.META.get('HTTP_AUTHORIZATION', None)
    print token
    if token is None:
        return HttpResponse(json.dumps(dict(result='fail', msg=' Invalid Authorization header. No credentials provided.')))

    list = json.dumps([g.json() for g in Goods.objects.all()])
    return HttpResponse(list)
