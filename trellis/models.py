from pyexpat import model
from django.db import models

# Crop model
class Crop(models.Model):
    name = models.CharField(max_length=100)
    selected = models.BooleanField(default=False)
    spacing = models.IntegerField(blank=True, null=True, default=0) # spacing between plants in inches
    row_spacing = models.IntegerField(blank=True, null=True, default=0) # Space between rows
    start_to_tp = models.IntegerField(blank=True, null=True, default=0) # Days
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='crops')

    class Meta:
        unique_together = ['name', 'owner']
        ordering = ['name']

    def __str__(self):
        return self.name

# Variety model
class Variety(models.Model):
    PLANTING_METHODS = (
        ('DS', 'Direct Seeding'),
        ('TP', 'Transplanting'),
    )
    name = models.CharField(max_length=100)
    method = models.CharField(max_length=2, choices=PLANTING_METHODS)
    dtm = models.IntegerField() # Days to Maturity
    seeds_oz = models.IntegerField() # Number of seeds per ounce
    quantity = models.IntegerField()
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE, related_name='varieties')
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='varieties')

    def __str__(self):
        return self.name

# Planting model
class Planting(models.Model):
    variety = models.ForeignKey(Variety, on_delete=models.CASCADE, related_name='plantings')
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    tp_date = models.DateField(auto_now=False, auto_now_add=False)
    quantity = models.IntegerField()
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='plantings')

    # def __str__(self):
    #     return self.name
