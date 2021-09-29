from django.shortcuts import render
count_main = 0
count_acc = 0
# Create your views here.


def hello_word(request):
    global count_main
    count_main = count_main + 1
    response = f'hello_world \n' \
               f'count of updates {count_main}'
    return render(request, "main.html", context={"welcome": response})


def account(request):
    global count_acc
    count_acc = count_acc + 1
    response = f'my account' \
               f'count of updates {count_acc}'
    return render(request, "account.html", context={"info": response, "primer": True})
