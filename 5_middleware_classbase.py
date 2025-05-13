
"""
    here we create middlewares with class and check user have to login in if wanna go to some paths
    we have to put midddleware in middlewares in MIDDLEWARES in settings.py and then run run as order that list
"""

from django.shortcuts import redirect
from django.contrib import messages

LOGIN_EXEPT_URLS =[
    '/',
    '/login/',
]

class LoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Before .........
        if not request.user.is_authenticated and request.path not in LOGIN_EXEPT_URLS:
            messages.error(request, "you should login first", "warning")
            return redirect('home:login')
        response = self.get_response(request)
        # After ...........
        return responce

