from django.shortcuts import render

# Create your views here.
def hello_word(request):
    response = 'hello_word'
    return render(request, "main.html", context={"welcome": response})


def account(request):
    response = 'my account'
    return render(request, "account.html", context={"info": response, "primer": True})
