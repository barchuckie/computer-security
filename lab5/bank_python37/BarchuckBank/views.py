from django.db.models import Q
from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.views import generic

# Create your views here.
from BarchuckBank.forms import RegisterForm, TransferForm
from BarchuckBank.models import Transfer


def index(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')
    return render(request, "index.html")


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('/')
    context = {
        'transactions': Transfer.objects.filter(
            Q(sender=request.user) | Q(recipient_name=request.user.username)
        ).order_by("-date"),
    }
    return render(request, "dashboard.html", context)


def confirm_transfer(request):
    if request.method == 'POST':
        form = TransferForm(request.POST)
        if form.is_valid():
            transfer = form.save(commit=False)
            transfer.sender = request.user
            transfer.save()

            return render(request, 'transfer_complete.html', form.cleaned_data)
    return redirect('/dashboard')


def new_transfer(request):
    if request.method == 'POST':
        form = TransferForm(request.POST)
        if form.is_valid():
            # new_form = form.save(commit=False)
            # new_form.sender = request.user
            # new_form.save()
            context = {
                'form': form,
                'transfer': form.cleaned_data
            }
            return render(request, 'confirm_transfer.html', context)
    else:
        form = TransferForm()
    return render(request, 'new_transfer.html', {'form': form})


class Register(generic.CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'
