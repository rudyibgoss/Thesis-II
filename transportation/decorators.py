# decorators.py
from functools import wraps #used to preserve metadata of the original view function
from django.shortcuts import redirect #used to redirect unauthorized users

#custom decorator that checks if the user's role is in the list of allowed roles
#if not, it redirects them to a specified URL
def role_required(allowed_roles, redirect_url):
    def decorator(view_func): #the actual decorator that wraps around the view function
        @wraps(view_func) #preserves the original function’s name and docstring
        def _wrapped_view(request, *args, **kwargs):

            #check if the user's role is not in the allowed roles
            if request.user.roles not in allowed_roles:

                #redirect to the provided URL if role is not permitted
                return redirect(redirect_url)

            #otherwise, allow access to the view
            return view_func(request, *args, **kwargs)
        return _wrapped_view #return the wrapped view
    return decorator #return the decorator function itself
