from django.contrib import admin
from .models import  Medicine,  MedicineOrder , MedicineOrderItem 

admin.site.register(Medicine)
admin.site.register(MedicineOrder)
admin.site.register(MedicineOrderItem) 