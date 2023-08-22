from django.shortcuts import render
from .quotes import quotes
import random


def homepage(request):
    quotes_size = len(quotes)

    quoteNumber = random.randint(0, quotes_size - 1)

    random_quote = quotes[quoteNumber]

    context = {"data": random_quote}
    return render(request, "index.html", context)
