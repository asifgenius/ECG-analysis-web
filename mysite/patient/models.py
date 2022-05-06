from django.db import models
from datetime import datetime
class Weight(models.Model):
    amount = models.DecimalField(max_digits=19, decimal_places=10)
    datetime = models.DateTimeField(default=datetime.now(), blank=True)


   