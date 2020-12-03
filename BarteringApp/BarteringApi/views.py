from . import mongodb_interface as mongodb
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpRequest
from . import mongodb_interface as mongodb
from rest_framework.parsers import JSONParser
import json


@csrf_exempt
def dispatch_request(request, user_id):
    if request.method == 'GET':
        return retrieve_postings_for_user(request, user_id)
    elif request.method == 'POST':
        return create_posting(request, user_id)

@csrf_exempt
def create_posting(request, user_id):
    posting = JSONParser().parse(request)
    mongodb.insert_posting(user_id, posting)
    return HttpResponse(201)


@csrf_exempt
def retrieve_posting(request):
    id = request.GET.get('id')
    return HttpResponse(json.dumps(mongodb.retrieve(id)), 200)


@csrf_exempt
def retrieve_postings_for_user(request, user_id):
    print('here')
    return HttpResponse(json.dumps(
        mongodb.retrieve_postings_for_user(user_id)), 200)


@csrf_exempt
def update_posting(request):
    return HttpResponse(200)


@csrf_exempt
def delete_posting(request):
    return HttpResponse(200)
