from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

from django.views import View

class SignUpView(View):

    template_name = 'signup.html'
    form_class = UserCreationForm

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username, password)
            if user:
                login(request, user)
                return redirect('/')
        return render(request, self.template_name, {'form': form})

    def get(self, request):
        return render(request, self.template_name, {'form': UserCreationForm()})