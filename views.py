from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from context.models import Beacon
from context.models import Interaction

def index(request):

	foos = Beacon.objects.all()

	data = serializers.serialize('json', foos)
	return HttpResponse(data, mimetype='application/json')

def beaconInteraction(request, _uuid):

	connections = Interaction.objects.filter(beacon__uuid=_uuid)

	data = serializers.serialize('json', connections)
	return HttpResponse(data, mimetype='application/json')

# Create your views here.
