from django.test import TestCase

from django.test import TestCase
from .models import CandlestickData, BarChartData, LineChartData, PieChartData
from datetime import date
from decimal import Decimal


class CandlestickDataTestCase(TestCase):
    def setUp(self):
        CandlestickData.objects.create(
            x=date(2023, 10, 1),
            open=Decimal('100.00'),
            high=Decimal('110.00'),
            low=Decimal('90.00'),
            close=Decimal('105.00')
        )

    def test_candlestick_data_creation(self):
        data = CandlestickData.objects.get(x=date(2023, 10, 1))
        self.assertEqual(data.open, Decimal('100.00'))
        self.assertEqual(data.high, Decimal('110.00'))
        self.assertEqual(data.low, Decimal('90.00'))
        self.assertEqual(data.close, Decimal('105.00'))

    def test_candlestick_data_change(self):
        data = CandlestickData.objects.get(x=date(2023, 10, 1))
        data.open = Decimal('101.00')
        data.high = Decimal('111.00')
        data.low = Decimal('91.00')
        data.close = Decimal('106.00')
        data.save()

        updated_data = CandlestickData.objects.get(x=date(2023, 10, 1))
        self.assertEqual(updated_data.open, Decimal('101.00'))
        self.assertEqual(updated_data.high, Decimal('111.00'))
        self.assertEqual(updated_data.low, Decimal('91.00'))
        self.assertEqual(updated_data.close, Decimal('106.00'))


class LineChartDataTestCase(TestCase):
    def setUp(self):
        LineChartData.objects.create(
            label="Sample Label",
            value=100
        )

    def test_line_chart_data_creation(self):
        data = LineChartData.objects.get(label="Sample Label")
        self.assertEqual(data.value, 100)

    def test_line_chart_data_change(self):
        data = LineChartData.objects.get(label="Sample Label")
        data.value = 200
        data.save()

        updated_data = LineChartData.objects.get(label="Sample Label")
        self.assertEqual(updated_data.value, 200)


class BarChartDataTestCase(TestCase):
    def setUp(self):
        BarChartData.objects.create(
            label="Sample Bar Label",
            value=100
        )

    def test_bar_chart_data_creation(self):
        data = BarChartData.objects.get(label="Sample Bar Label")
        self.assertEqual(data.value, 100)

    def test_bar_chart_data_change(self):
        data = BarChartData.objects.get(label="Sample Bar Label")
        data.value = 200
        data.save()

        updated_data = BarChartData.objects.get(label="Sample Bar Label")
        self.assertEqual(updated_data.value, 200)


class PieChartDataTestCase(TestCase):
    def setUp(self):
        PieChartData.objects.create(
            label="Sample Pie Label",
            value=100
        )

    def test_pie_chart_data_creation(self):
        data = PieChartData.objects.get(label="Sample Pie Label")
        self.assertEqual(data.value, 100)

    def test_pie_chart_data_change(self):
        data = PieChartData.objects.get(label="Sample Pie Label")
        data.value = 200
        data.save()

        updated_data = PieChartData.objects.get(label="Sample Pie Label")
        self.assertEqual(updated_data.value, 200)
