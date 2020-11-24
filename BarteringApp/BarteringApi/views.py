from . import mongodb_interface as mongodb
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpRequest
from rest_framework.parsers import JSONParser
from pymongo import MongoClient
import json

@csrf_exempt
def create_post(request):
    return HttpResponse(status=201)


@csrf_exempt
def retrieve_post(request):
    return HttpResponse(status=200)


@csrf_exempt
def update_post(request):
    return HttpResponse(status=200)

