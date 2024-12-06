from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    header = 'Данные пользователя'  # обычная переменная
    langs = ['Python', 'C++']  # список
    user = {'name': 'Dima', 'age': 16}  # словарь
    address = ('Истомина', '22А', 91)  # кортеж

    data = {'header': header, 'langs': langs, 'user': user, 'address': address}
    return render(request, 'blog/index.html', context=data)



