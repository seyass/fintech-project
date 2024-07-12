from django.shortcuts import render

# Create your views here.


def view_chart(request):
    return render(request, 'chart.html')