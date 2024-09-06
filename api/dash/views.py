from django.shortcuts import render
from django.http import JsonResponse
from .models import CandlestickData, LineChartData, BarChartData, PieChartData
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import (
    CandlestickDataSerializer,
    LineChartDataSerializer,
    BarChartDataSerializer,
    PieChartDataSerializer,
)


def status(request):
    return JsonResponse({"status": "ok"})


def stats(request):
    candle_data = CandlestickData.objects.count()
    line_data = LineChartData.objects.count()
    bar_data = BarChartData.objects.count()
    pie_data = PieChartData.objects.count()
    return JsonResponse(
        {
            "candlestick_data": candle_data,
            "line_chart_data": line_data,
            "bar_chart_data": bar_data,
            "pie_chart_data": pie_data,
        }
    )


@api_view(["GET", "POST"])
def candlestick_data(request):
    if request.method == "GET":
        data = CandlestickData.objects.values(
            "x", "open", "high", "low", "close"
        )
        return Response({"data": list(data)})
    elif request.method == "POST":
        serializer = CandlestickDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(["GET", "POST"])
def line_chart_data(request):
    if request.method == "GET":
        data = LineChartData.objects.values("label", "value")
        return Response(
            {
                "labels": list(data.values_list("label", flat=True)),
                "data": list(data.values_list("value", flat=True)),
            }
        )
    elif request.method == "POST":
        serializer = LineChartDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(["GET", "POST"])
def bar_chart_data(request):
    if request.method == "GET":
        data = BarChartData.objects.values("label", "value")
        return Response(
            {
                "labels": list(data.values_list("label", flat=True)),
                "data": list(data.values_list("value", flat=True)),
            }
        )
    elif request.method == "POST":
        serializer = BarChartDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(["GET", "POST"])
def pie_chart_data(request):
    if request.method == "GET":
        data = PieChartData.objects.values("label", "value")
        return Response(
            {
                "labels": list(data.values_list("label", flat=True)),
                "data": list(data.values_list("value", flat=True)),
            }
        )
    elif request.method == "POST":
        serializer = PieChartDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


def randomize(request):
    CandlestickData.objects.all().delete()
    LineChartData.objects.all().delete()
    BarChartData.objects.all().delete()
    PieChartData.objects.all().delete()

    CandlestickData.objects.bulk_create([
        CandlestickData(
            x="2024-04-01", open=125, high=130, low=80, close=128
        ),
        CandlestickData(
            x="2024-09-02", open=108, high=135, low=10, close=90
        ),
        CandlestickData(
            x="2024-02-03", open=130, high=170, low=120, close=135
        ),
        CandlestickData(
            x="2024-05-04", open=15, high=155, low=10, close=140
        ),
        CandlestickData(
            x="2024-01-05", open=140, high=150, low=100, close=145
        ),
    ])

    LineChartData.objects.bulk_create(
        [
            LineChartData(label="Jan", value=100),
            LineChartData(label="Feb", value=20),
            LineChartData(label="Mar", value=70),
            LineChartData(label="Apr", value=70),
            LineChartData(label="May", value=40),
        ]
    )

    BarChartData.objects.bulk_create(
        [
            BarChartData(label="Product A", value=100),
            BarChartData(label="Product B", value=120),
            BarChartData(label="Product C", value=80),
            BarChartData(label="Product D", value=50),
            BarChartData(label="Product E", value=110),
        ]
    )

    PieChartData.objects.bulk_create(
        [
            PieChartData(label="Red", value=10),
            PieChartData(label="Blue", value=20),
            PieChartData(label="Yellow", value=30),
            PieChartData(label="Green", value=40),
            PieChartData(label="Purple", value=50),
        ]
    )

    return JsonResponse({"status": "success"})
