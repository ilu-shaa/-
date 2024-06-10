from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .forms import SignUpForm, LoginUserForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms  import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import Profile
import random
from sympy import *



from django.db.models import Count

from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
]

class DataMixin:
    paginate_by = 2

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('women'))

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu

        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context


def mat(request):
    return HttpResponse(f"2+2=")



menu = [{'title': "О нас", 'url_name': 'about'}, 
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'},
        ]  

data_db = [
    {'id':1,'title': 'Angelina djoli','content': 'biografi A. D.','is_publi':True},
    {'id':2,'title': 'Margo Robi','content': 'biografi M. R.','is_publi':False},
    {'id':3,'title': 'Djulia Robert','content': 'biografi D. R.','is_publi':True}

]

def index(request):
    data = {
        'title' : 'Главная страница',
        'main_title': "title",
        'menu' : menu,
        'posts': data_db,
        }
    return render(request, 'main/index.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>страница не найдена</h1>")

def about(request):
    return render(request, 'main/about.html', {'title':'O сайте', 'menu': menu})

def home(request):
    return HttpResponseRedirect(reverse('home'))

def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # сохранение номера
            Profile.objects.create(user=user, phone_number=form.cleaned_data.get('phone_number'))
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'main/looogin.html', {'form': form})

LoginUserForm
def login_us(request):
    form = LoginUserForm()
    return render(request, 'main/ri.html', {'form': form})

def plus(request):
    return render(request, 'main/addition-difficulty-selection.html')

def plus_ez(request):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    problem = f"{num1} + {num2}"
    answer = num1 + num2
    return render(request, 'main/addition-complication.html', context={"problem": problem, "pk": answer})

def plus_no(request):
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    num3 = random.randint(1, 50)
    problem = f"{num1} + {num2} + {num3}"
    answer = num1 + num2 + num3
    return render(request, 'main/addition-complication-average.html', context={"problem": problem, "pk": answer})

def plus_har(request):
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    num3 = random.randint(1, 100)
    num4 = random.randint(1, 100)
    problem = f"{num1} + {num2} + {num3} + {num4}"
    answer = num1 + num2 + num3 + num4
    return render(request, 'main/addition-complication-difficulty.html', context={"problem": problem, "pk": answer})


def minus(request):
    return render(request, 'main/subtraction-difficulty-selection.html')

def minus_ez(request):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    problem = f"{num1} - {num2}"
    answer = num1 - num2
    return render(request, 'main/subtraction-complication-light.html', context={"problem": problem, "pk": answer})

def minus_no(request):
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    num3 = random.randint(1, 50)
    problem = f"{num1} - {num2} - {num3}"
    answer = num1 - num2 - num3
    return render(request, 'main/subtraction-complication-average.html', context={"problem": problem, "pk": answer})

def minus_har(request):
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    num3 = random.randint(1, 100)
    num4 = random.randint(1, 100)
    problem = f"{num1} - {num2} - {num3} - {num4}"
    answer = num1 - num2 - num3 - num4
    return render(request, 'main/subtraction-complication-difficulty.html', context={"problem": problem, "pk": answer})


def mult(request):
    return render(request, 'main/multiplication-difficulty-selection.html')

def mult_ez(request):
    num1, num2 = random.randint(1, 10), random.randint(1, 10)
    problem = f"{num1} * {num2}"
    answer = (num1 * num2)
    return render(request, 'main/multiplication-complication-light.html', context={"problem": problem, "pk": answer})

def mult_no(request):
    num1, num2, num3 = random.randint(10, 50), random.randint(10, 50),random.randint(10, 50)
    problem = f"{num1} * {num2} * {num3}"
    answer = (num1 * num2 * num3)
    return render(request, 'main/multiplication-complication-average.html', context={"problem": problem, "pk": answer})

def mult_har(request):
    num1, num2, num3, num4 = random.randint(10, 100), random.randint(10, 100),random.randint(10, 100), random.randint(10, 100)
    problem = f"{num1} * {num2} * {num3} * {num4}"
    answer = (num1 * num2 * num3 * num4)
    return render(request, 'main/multiplication-complication-difficulty.html', context={"problem": problem, "pk": answer})


def divis(request):
    return render(request, 'main/division-difficulty-selection.html')

def divis_ez(request):
    num1, num2 = random.randint(1, 10), random.randint(1, 10)
    problem = f"{num1 * num2} / {num2}"
    answer = (num1 * num2) // num2
    return render(request, 'main/division-complication-light.html', context={"problem": problem, "pk": answer})
"""
def divis_no(request):
    num1, num2, num3 = random.randint(10, 50), random.randint(10, 50), {random.randint(10, 50)}
    problem = f"{num1 * num2} / {num2} / {num3}"
    answer = ((num1 * num2) * 3) // num3
    return render(request, 'main/division-complication-average.html', context={"problem": problem, "pk": answer})

def divis_har(request):
    num1, num2, num3, num4 = random.randint(50, 100), random.randint(50, 100), random.randint(50, 100), random.randint(50, 100)
    problem = f"{num1 * num2 * num3} / {num2} / {num3} / {num4}"
    answer = (num1 * num2 * num3) * (num2) // ((num3) * (num4))
    return render(request, 'main/division-complication-difficulty.html', context={"problem": problem, "pk": answer})
"""
