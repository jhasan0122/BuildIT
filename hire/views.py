from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from flask_login import login_required

from .models import HirePost


# Create your views here.

# def custom_login_required(additional_constraint):
#     def decorator(view_func):
#         @login_required
#         def _wrapped_view(request, *args, **kwargs):
#             if additional_constraint(request.user):
#                 return view_func(request, *args, **kwargs)
#             return HttpResponseForbidden("You don't have permission to access this section.")
#         return _wrapped_view
#     return decorator
#
# def has_special_permission(user):
#     return user.first_name == 'P' or user.first_name=='E' # Example constraint
#
#
# @custom_login_required(has_special_permission)
def hire(request):
    if request.method == 'POST':
        expart_type = request.POST.get('expart_type')
        description = request.POST.get('description')
        offered_money = request.POST.get('offered_money')

        createHirePost = HirePost(user=request.user, expart_type=expart_type, description=description,
                                  offered_money=offered_money)
        createHirePost.save()

        return redirect('hire')

    hires = HirePost.objects.order_by('-created_at')
    return render(request, 'hire/main.html', {'hires': hires})


def try_view(request):
    return render(request, 'hire/try_view.html')




