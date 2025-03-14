#Mixins are used to give extra functionality to a class
#django's one mixin is LoginRequiredMixin which uses dispatch() and check if user is login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

class LoginRequired(LoginRequiredMixin):
    ''' Sends user to denied.html if not login '''
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return render(request, 'denied.html')
        return super().dispatch(request, *args, **kwargs)