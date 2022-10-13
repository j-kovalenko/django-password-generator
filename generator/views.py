from django.shortcuts import render
from random import choice
# from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'generator/home.html')

def password(request):
    length = int(request.GET.get('length', 12))
    passw = generate_password(length, request.GET.get('uppercase'), request.GET.get('numbers'), request.GET.get('special'))
    print(passw)
    return render(request, 'generator/password.html', {'password': passw})

def madeby(request):
    return render(request, 'generator/author.html')

def generate_password(length: int, has_upper=False, has_nums=False, has_special=False) -> str:
    if length <= 0:
        length = 12
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = list(lower.upper())
    chrs = list(lower)
    nums = list('0123456789')
    special = list('!?@#$%^&*()_+-;:"')
    if has_upper:
        chrs.extend(upper)
    if has_nums:
        chrs.extend(nums)
    if has_special:
        chrs.extend(special)
    password = ''
    for _ in range(length):
        password += choice(chrs)
    return password