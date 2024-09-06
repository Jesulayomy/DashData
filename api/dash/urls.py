from django.urls import path
from . import views


urlpatterns = [
    path('candlestick-data/', views.candlestick_data, name='candlestick_data'),
    path('line-chart-data/', views.line_chart_data, name='line_chart_data'),
    path('bar-chart-data/', views.bar_chart_data, name='bar_chart_data'),
    path('pie-chart-data/', views.pie_chart_data, name='pie_chart_data'),
    path('randomize/', views.randomize, name='randomize'),
    path('status/', views.status, name='status'),
    path('stats/', views.stats, name='stats'),
]
