from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse


def home_view(request: HttpRequest):
    return HttpResponse(
        """Your looking for the assignment's arnt you? Well here it is - Try going to 
/hey/(your name) dont include the () or /age-in/(end year)/(birth year) dont include the () or /order-total/(burgers)/(fries)/(drinks) dont include the ()""")


def hey_view(request, name):
    return HttpResponse(f"Hey, {name.upper()}!")


def age_in_view(request, end, birthyear):
    age = int(end) - int(birthyear)
    return HttpResponse(f"You will be {age} years old!")


def order_total_view(request, burgers, fries, drinks):
    total = int(burgers) * 4.50 + int(fries) * 1.5 + int(drinks) * 1
    return HttpResponse(f"Your total is ${total}")
