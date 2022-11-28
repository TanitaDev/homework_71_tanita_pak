from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.views import View

from accounts.models import Account


class SubscribeView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        account = get_object_or_404(Account, pk=kwargs.get('pk'))
        if request.user in account.subscribers.all():
            account.subscribers.remove(request.user)
            return redirect('profile', pk=kwargs.get('pk'))
        account.subscribers.add(request.user)
        return redirect('profile', pk=kwargs.get('pk'))
