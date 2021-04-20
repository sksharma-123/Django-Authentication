from django.shortcuts import redirect, render
from django.contrib.auth.models import User

def index(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request, 'Index page/index.html')

def about(request):
    return render(request, 'Index page/about.html')


# ---------------------------- Profile ----------------------------


def profile(request, user):
   return render(request, 'Profile/profile.html')




def login_request(request):
    return render(request, 'Profile/login_request.html')


def settings(request):
    return render(request, 'Profile/settings.html')

def delete_account(request):
    return render(request, 'Profile/delete_account.html')

def account_deleted(request):
    if request.method == 'POST':
        username = request.user
        # email = request.POST['email']
        # password = request.POST['password']

        query = User.objects.get(username=username)
        query.delete()

    return redirect("/")
