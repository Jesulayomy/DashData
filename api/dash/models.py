from django.db import models


class CandlestickData(models.Model):
    x = models.DateField()
    open = models.DecimalField(max_digits=10, decimal_places=2)
    high = models.DecimalField(max_digits=10, decimal_places=2)
    low = models.DecimalField(max_digits=10, decimal_places=2)
    close = models.DecimalField(max_digits=10, decimal_places=2)


class LineChartData(models.Model):
    label = models.CharField(max_length=100)
    value = models.IntegerField()


class BarChartData(models.Model):
    label = models.CharField(max_length=100)
    value = models.IntegerField()


class PieChartData(models.Model):
    label = models.CharField(max_length=100)
    value = models.IntegerField()
