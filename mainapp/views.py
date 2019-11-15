from django.shortcuts import render

def index(request):
    return render(request, 'mainapp/homePage.html')

def contact(request):
    return render(request, 'mainapp/basic.html', {'values':
     ['If you have any questions or propositions please contact me:', '+33 6 66 58 56 91','andjey1810@gmail.com']})
