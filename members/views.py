from django.shortcuts import render


class UserRegisterView(generic.CreateView):
    # form_class = UserCreationForm
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')