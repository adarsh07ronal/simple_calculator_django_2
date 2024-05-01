from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse


def calculate(request):
    try:
        expression = request.GET.get('expression', '')
        result = eval(expression)
        return JsonResponse({"result": result})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
    
def home(request):
    return JsonResponse({"message": "Welcome to the Calculator App!"})