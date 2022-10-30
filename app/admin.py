from django.contrib import admin
from .models import Quiz, Phy101, Phy103, Gns101, Che101

# Register your models here.
admin.site.register(Quiz)
admin.site.register(Phy101)
admin.site.register(Gns101)
admin.site.register(Phy103)
admin.site.register(Che101)
