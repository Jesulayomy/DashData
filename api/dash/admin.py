from django.contrib import admin
from .models import CandlestickData, LineChartData, BarChartData, PieChartData


@admin.register(CandlestickData)
class CandlestickDataAdmin(admin.ModelAdmin):
    list_display = ("x", "open", "high", "low", "close")


@admin.register(LineChartData)
class LineChartDataAdmin(admin.ModelAdmin):
    list_display = ("label", "value")


@admin.register(BarChartData)
class BarChartDataAdmin(admin.ModelAdmin):
    list_display = ("label", "value")


@admin.register(PieChartData)
class PieChartDataAdmin(admin.ModelAdmin):
    list_display = ("label", "value")
