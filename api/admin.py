from django.contrib import admin
from .models import Invoice, User

admin.site.register(Invoice)
admin.site.register(User)