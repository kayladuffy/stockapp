from django.db import models

class stocks(models.Model):
    ticker = models.CharField(max_length=10)

    def __str__(self):
        return self.ticker

