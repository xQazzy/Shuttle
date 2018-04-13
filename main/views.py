from django.shortcuts import render


def main(request):  # запрашиваем страницу
    return render(request, 'main.html', locals())  # возвращаем отрисованную страницу
