from django.contrib import admin
from context.models import User,Beacon,Activity,Interaction,UserBeacon,UserBeaconActivity,InteractionSpacebrewRoutes

admin.site.register(User)
admin.site.register(Beacon)
admin.site.register(Activity)
admin.site.register(Interaction)
admin.site.register(UserBeacon)
admin.site.register(UserBeaconActivity)
admin.site.register(InteractionSpacebrewRoutes)

# Register your models here.
