from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created ! You can logged in') 
            return redirect("/login")
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'users/profile.html', args)

# def edit_profile(request):
#     if request.method == 'POST':
#         form = EditProfileForm(request.POST, instance=request.user)

#         if form.is_valid():
#             form.save()
#             return redirect(reverse('users:users_profile'))
#     else:
#         form = EditProfileForm(instance=request.user)
#         args = {'form': form}
#         return render(request, 'users/edit_profile.html', args)

# def change_password(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(data=request.POST, user=request.user)

#         if form.is_valid():
#             form.save()
#             update_session_auth_hash(request, form.user)
#             return redirect(reverse('accounts:view_profile'))
#         else:
#             return redirect(reverse('accounts:change_password'))
#     else:
#         form = PasswordChangeForm(user=request.user)

#         args = {'form': form}
#         return render(request, 'accounts/change_password.html', args)