from django.shortcuts import render
import random

# Create your views here.
def generatepassword(request):
    # Provide a default value of 8 if 'selection' is not in the GET request
    selection = int(request.GET.get('selection', 8))
    upper = request.GET.get('upper', 'off') == 'on'
    number = request.GET.get('number', 'off') == 'on'
    symbole = request.GET.get('symbole', 'off') == 'on'

    chars = list('qwertyuiopasdfghjklzxcvbnm')
    if upper:
        chars.extend('QWERTYUIOPASDFGHJKLZXCVBNM')
    if number:
        chars.extend('1234567890')    
    if symbole:
        chars.extend('!@#$%^&*()_+}{[]')
    
    thepassword = ''.join(random.choice(chars) for i in range(selection))
    
    return render(request, 'password/generatepassword.html', {'thepassword': thepassword})
