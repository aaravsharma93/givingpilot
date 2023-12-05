from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse

import stripe

stripe.api_key = "sk_test_51JIJYUAaEfbqTh3lNmfAaIFx5bNmMyiDFoHo51RYLxcAfng3o60y5W1XdYUc9tVXLYrv32OFfGqvEJNkSqPrrJg400VrNXwJb0"


def index(request):
    return render(request, 'index.html')


def thanks(request):
    return render(request, 'thanks.html')
