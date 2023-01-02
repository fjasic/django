from django.http import HttpResponseNotFound, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

monthly_challenges = {
    "january": "New Year's 1th resolution!",
    "february": "New Year's 2nd resolution!",
    "march": "New Year's 3th resolution!",
    "april": "New Year's 4th resolution!",
    "may": "New Year's 5th resolution!",
    "jun": "New Year's 6th resolution!",
    "july": "New Year's 7th resolution!",
    "august": "New Year's 8th resolution!",
    "september": "New Year's 9th resolution!",
    "october": "New Year's 10th resolution!",
    "novemeber": "New Year's 11th resolution!",
    "december": None,
}

# Create your views here.


def index_view(request):
    months = {}
    months_keys = list(monthly_challenges.keys())
    for month in months_keys:
        months.update({month: reverse("month-challenge", args=[month])})
    return render(request, "challenges/index.html", {"months": months})


def monthly_challenge_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("<h1>month invalid</h1>")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    if month in monthly_challenges.keys():
        text = monthly_challenges.get(month)
        return render(
            request,
            "challenges/challenge.html",
            {"text": text, "month": month},
        )
    else:
        raise Http404()
