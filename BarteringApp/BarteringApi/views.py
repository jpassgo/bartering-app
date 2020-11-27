from . import mongodb_interface as mongodb
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpRequest
from . import mongodb_interface as mongodb
from rest_framework.parsers import JSONParser
import json

@csrf_exempt
def create_posting(request):
    posting = JSONParser().parse(request)
    mongodb.create(posting)
    return HttpResponse(201)


@csrf_exempt
def retrieve_posting(request):
    id = request.GET.get('id')
    return HttpResponse(json.dumps(mongodb.retrieve(id)), 200)

@csrf_exempt
def retrieve_postings_for_user(request):
    id = request.GET.get('id')
    return HttpResponse(json.dumps(mongodb.retrieve_postings_for_user(id)), 200)


@csrf_exempt
def update_posting(request):
    return HttpResponse(200)


@csrf_exempt
def delete_posting(request):
    return HttpResponse(status=200)

