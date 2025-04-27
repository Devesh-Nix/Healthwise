from django.db import models

class Medicine(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    available_quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class MedicineOrder(models.Model):
    full_name = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    ordered_at = models.DateTimeField(auto_now_add=True)
    medicines = models.ManyToManyField(Medicine, through='MedicineOrderItem')

class MedicineOrderItem(models.Model):
    order = models.ForeignKey(MedicineOrder, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
