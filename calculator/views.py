from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Result
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def calculate(request):
    try:
        expression = request.GET.get('expression', '')
        result = eval(expression)
        return JsonResponse({"result": result})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

@csrf_exempt   
def home(request):
    return JsonResponse({"message": "Welcome to the Calculator App!"})
@csrf_exempt
def add(request):
    return HttpResponse("CALCULATOR")

@csrf_exempt
def calculate_and_store(request):
    if request.method == "POST":
        expression = request.POST.get('expression')
        try:
            # Safely evaluate the mathematical expression
            result = eval(expression)
            Result.objects.create(expression=expression, result=str(result))
            return redirect('display_results')
        except Exception as e:
            return render(request, 'calculate.html', {'error': str(e)})

    return render(request, 'calculate.html')

@csrf_exempt
def display_results(request):
    results = Result.objects.all()
    return render(request, 'results.html', {'results': results})