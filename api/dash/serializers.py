from rest_framework import serializers
from .models import CandlestickData, LineChartData, BarChartData, PieChartData


class CandlestickDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandlestickData
        fields = ['x', 'open', 'high', 'low', 'close']


class LineChartDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineChartData
        fields = ['label', 'value']


class BarChartDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BarChartData
        fields = ['label', 'value']


class PieChartDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PieChartData
        fields = ['label', 'value']
