from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import Context, loader
from expenses.models import *
from django.core import serializers
from django.http import JsonResponse
from django.db.models import Max
import random
import json
import socket

def index (request):
    template = loader.get_template("expenses/template/index.html")
    return HttpResponse(template.render())

def checkUser(request):
	username = request.POST['uname']
	userexist = Expenses.objects.filter(username = username)
	count = userexist.count()
	data = {'count' : count}
	return HttpResponse(json.dumps(data), content_type='application/json')
	
