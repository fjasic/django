from django.shortcuts import render
from django.http import (
    HttpResponse,
    HttpResponseNotFound,
    HttpResponseRedirect,
)
from django.urls import reverse

monthly_challenges = {
    "january": "New Year 1 resolution!",
    "february": "New Year 2 resolution!",
    "march": "New Year 3 resolution!",
    "april": "New Year 4 resolution!",
    "may": "New Year 5 resolution!",
    "jun": "New Year 6 resolution!",
    "july": "New Year 7 resolution!",
    "august": "New Year 8 resolution!",
    "september": "New Year 9 resolution!",
    "october": "New Year 10 resolution!",
    "novemeber": "New Year 11 resolution!",
    "december": "New Year 12 resolution!",
}

# Create your views here.


def index_view(request):
    list_item = ""
    months = list(monthly_challenges.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_item += f"<li><a href='{month_path}'>{capitalized_month}</a></li>"
    response_data = f"""
        <ul>
        {list_item}
        </ul>
    """
    return HttpResponse(response_data)


def monthly_challenge_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("<h1>month invalid</h1>")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    if month in monthly_challenges.keys():
        response_data = f"<h1>{monthly_challenges.get(month)}</h1>"
        return HttpResponse(response_data)
    else:
        return HttpResponseNotFound("<h1>this month doesnt exist!</h1>")
