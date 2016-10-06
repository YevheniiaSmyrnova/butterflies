"""
Main views module
"""
from django.contrib.auth import login
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import TemplateView
from django.views.generic.base import View


class IndexView(TemplateView):
    """
    Main page
    """
    template_name = 'index.html'


class FactsView(TemplateView):
    """
    Interesting facts page
    """
    template_name = 'facts.html'


class PoemsView(TemplateView):
    """
    Poems page
    """
    template_name = 'poems.html'


class ContactView(TemplateView):
    """
    Contact page
    """
    template_name = 'contact.html'


class RegisterFormView(FormView):
    """
    User registration
    """
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = "register.html"

    def form_valid(self, form):
        """
        Save user if form is valid
        :param form:
        :return: base class method
        """
        form.save()
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    """
    User login
    """
    form_class = AuthenticationForm
    template_name = "login.html"
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        """
        User authentication
        :param form:
        :return: base class method
        """
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    """
    User logout
    """
    def get(self, request):
        """
        User logout
        :param request:
        :return: main page
        """
        logout(request)
        return reverse_lazy('index')
