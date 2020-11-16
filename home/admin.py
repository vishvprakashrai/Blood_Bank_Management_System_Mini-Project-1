from django.contrib import admin
from .models import seeker, donor, bloodseeker, blooddonor

# Register your models here.
admin.site.register(seeker)
admin.site.register(donor)
admin.site.register(blooddonor)
admin.site.register(bloodseeker)