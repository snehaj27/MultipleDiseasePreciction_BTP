from django.shortcuts import render


def heart(request):
    return render(request, 'diseases/heart.html')


def liver(request):
    return render(request, 'diseases/liver.html')


def kidney(request):
    return render(request, 'diseases/kidney.html')


def diabetes(request):
    return render(request, 'diseases/diabetes.html')


def breastCancer(request):
    return render(request, 'diseases/breastCancer.html')
