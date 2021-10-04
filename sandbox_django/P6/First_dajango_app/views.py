from django.shortcuts import render
from P6.forms import TextForm

# Create your views here.
# def hello_word(request):
#     response = 'hello_word'
#     return render(request, "main.html", context={"welcome": response})


def account(request):
    response = 'my account'
    return render(request, "account.html", context={"info": response, "primer": True})


def news(request):
    response = 'my account'
    return render(request, "news.html", context={"info": response, "primer": True})


def hello_word(request):
    context = {}

    if request.method == 'POST':
        filled_form = TextForm(request.POST)
        if filled_form.is_valid():
            weight = filled_form.cleaned_data['weight_client']
            height = filled_form.cleaned_data['height_client']
            age = filled_form.cleaned_data['age_client']

            imt = weight / ((height / 100) ** 2)
            imt = round(imt, 2)
            text = 'Unreal'
            if imt <= 16.0:
                text = 'The smallest weight'
            elif 16.0 < imt <= 18.5:
                text = 'Small weight'
            elif 18.5 < imt <= 25:
                text = 'Norm'
            elif imt > 25:
                text = 'You are fat pig'


            answer = [f'', f'Age {age}', f'Height {height}', f'Weight {weight}',
                      f'BMI {imt}', f'The answer: "{text}"']

            context['answer'] = answer
        else:
            print('not valid')
            context['forms'] = filled_form
            return render(request, "main.html", context = context)

    print(request.GET)
    print('valid')
    context['forms'] = TextForm()
    return render(request, "main.html", context = context)