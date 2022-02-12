from django.db import models

# Crop model
class Crop(models.Model):
    name = models.CharField(max_length=100)
    selected = models.BooleanField(default=False)
    spacing = models.IntegerField() # spacing between plants in inches
    row_spacing = models.IntegerField() # Space between rows
    seeds_oz = models.IntegerField() # Number of seeds per ounce
    start_to_tp = models.IntegerField() # Days
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='crops')

    def __str__(self):
        return self.name

# Variety model
class Variety(models.Model):
    name = models.CharField(max_length=100)
    dtm = models.IntegerField() # Days to Maturity
    spacing = models.IntegerField() # spacing between plants in inches
    row_spacing = models.IntegerField() # Space between rows
    seeds_oz = models.IntegerField() # Number of seeds per ounce
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE, related_name='varieties')
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='varieties')

    def __str__(self):
        return self.name

# Planting model
class Planting(models.Model):
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    tp_date = models.DateField(auto_now=False, auto_now_add=False)
    dtm = models.IntegerField() # Days to Maturity
    variety = models.ForeignKey(Variety, on_delete=models.CASCADE, related_name='plantings')
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='plantings')

    def __str__(self):
        return self.name
