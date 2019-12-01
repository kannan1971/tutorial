from django.conf import settings
from django.shortcuts import redirect
import re
from django.urls import reverse
from django.contrib.auth import logout


EXEMPT_URLS = [re.compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings,'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [re.compile(url) for url in settings.LOGIN_EXEMPT_URLS]

class LoginRequiredMiddleWare:

    def __init__(self,get_response):  # function argument when URL hit the relevant function will go as an arg.
        self.get_response= get_response

    def __call__(self,request):
        response=self.get_response(request)
        return response

# django will call this view before it runs the view function defined in the url

    def process_view(self,request,view_func,view_args,view_kwargs):
        assert hasattr(request,'user')  # request obj has user attribute
        path = request.path_info.lstrip('/')# removes leading forward slash
        print(path)

# Method 1
        # if not request.user.is_authenticated: #no () because only obj will return boolean not function
        #     if not any(url.match(path) for url in EXEMPT_URLS):
        #         return redirect(settings.LOGIN_URL)
# Method 2

        url_is_exempt = any(url.match(path) for url in EXEMPT_URLS)

        if path == reverse('account:logout').lstrip('/'):
            logout(request)

        if request.user.is_authenticated and url_is_exempt:
            return redirect(settings.LOGIN_REDIRECT_URL)
        elif request.user.is_authenticated or url_is_exempt:
            return None
        else:
            return redirect(settings.LOGIN_URL)
