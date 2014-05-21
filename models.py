from django.db import models

# Create your models here.

class User(models.Model):
	name = models.CharField(max_length=200)
	device_id = models.IntegerField(default=0)

	def __unicode__(self):
		return self.name

class Interaction(models.Model):
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=500)
	num_users = models.IntegerField(default=0)

	def __unicode__(self):
		return self.name

class Beacon(models.Model):
	uuid = models.CharField(max_length=100)
	name = models.CharField(max_length=200)
	location = models.CharField(max_length=200)
	interaction = models.ForeignKey(Interaction)

	def __unicode__(self):
		return self.name

class Activity(models.Model):
	activityID = models.IntegerField(default=0)
	name = models.CharField(max_length=200)

	def __unicode__(self):
		return self.name


# Joining tables

class UserBeacon(models.Model):
	user = models.ForeignKey(User)
	beacon = models.ForeignKey(Beacon)
	option1 = models.IntegerField(default=0)

class UserBeaconActivity(models.Model):
	timestamp = models.DateTimeField(True)
	user = models.ForeignKey(User)
	beacon = models.ForeignKey(Beacon)
	activity = models.ForeignKey(Activity)

class InteractionSpacebrewRoutes(models.Model):
	interaction = models.ForeignKey(Interaction)
	isPublish = models.BooleanField(default=False)
	clientName = models.CharField(max_length=200)
	interactionName = models.CharField(max_length=200)
	dataType = models.CharField(max_length=20)

