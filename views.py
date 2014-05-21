from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from context.models import Beacon

def index(request):

	foos = Beacon.objects.all()

	data = serializers.serialize('json', foos)
	return HttpResponse(data, mimetype='application/json')

# Create your views here.
