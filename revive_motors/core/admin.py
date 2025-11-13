from django.contrib import admin
from .models import ContactDetail, Car, OwnershipRecord, Transaction, Rating


admin.site.register(ContactDetail)
admin.site.register(Car)
admin.site.register(OwnershipRecord)
admin.site.register(Transaction)
admin.site.register(Rating)