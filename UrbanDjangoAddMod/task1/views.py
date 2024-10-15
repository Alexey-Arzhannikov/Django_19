from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
from task1.models import Game, Buyer

# Create your views here.
def platform(request):
    title = 'Главная страница'
    context = {
        'title': title
    }
    return render(request, 'platform.html', context)

def games(request):
    title = 'Игры'
    Games = Game.objects.all()
    main_page = 'http://127.0.0.1:8000/platform/'

    context = {
        'Games': Games,
        'mp': main_page,
        'title': title
    }
    return render(request, 'games.html', context)

def cart(request):
    title = 'Корзина'
    main_page = 'http://127.0.0.1:8000/platform/'
    game_page = 'http://127.0.0.1:8000/platform/games/'

    context = {
        'mp': main_page,
        'gp': game_page,
        'title': title
    }
    return render(request, 'cart.html', context)

def sign_up_by_html(request):

    users = ['Alex', 'Vika', 'Makar', 'Dima', 'Masha', 'Liza']
    info = {}
    context = {
        'info': info
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if username not in users and password == repeat_password and int(age) >= 18:
            return HttpResponse(f'Приветствуем, {username}!')
        else:
            if username in users:
                info['error'] = 'Пользователь уже существует'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
    return render(request, 'registration_page.html', context)


def sign_up_by_django(request):
    Buyers = Buyer.objects.all()
    info = {}
    context = {
        'info': info
    }

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            else:
                user_exists = False
                for buyer in Buyers:
                    if buyer.name == username:
                        user_exists = True
                        break

                if user_exists:
                    info['error'] = 'Пользователь уже существует'
                else:
                    Buyer.objects.create(name=username, balance=0, age=age)
    else:
        form = UserRegister()
    return render(request, 'registration_page.html', {'form': form, 'info': info})