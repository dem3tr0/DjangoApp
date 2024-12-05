from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h2>Главная</h2>')


def about(request, name, age):
    return HttpResponse(f'''
        <h2>О пользователе</h2>
        <p>Имя: {name}</p>
        <p>Возраст: {age}</p>
    ''')


def contacts(request):
    return HttpResponse('<h2>Контакты</h2>')


def user(request, name='undefined', age=0):
    return HttpResponse(f'''
    <h2>Имя: {name}</h2>
    <h2>Возраст: {age}</h2>
''')

