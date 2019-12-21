from django.contrib.auth.decorators import user_passes_test
from django.db import connection
from django.db.models import Q
from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.views import generic

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from BarchuckBank.forms import RegisterForm, TransferForm, SQLInjectionForm
from BarchuckBank.models import Transfer


def index(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')
    return render(request, "index.html")


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('/')
    context = {
        'transfers': Transfer.objects.filter(
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


@csrf_exempt
@user_passes_test(lambda user: user.is_superuser)
def admin_confirm_transfers(request):
    transfers_to_confirm = []

    if request.method == 'POST':
        print(request.POST)
        for transfer in request.POST:
            Transfer.objects.filter(id=transfer).update(confirmed=True)

    for item in Transfer.objects.filter(confirmed=False):
        transfers_to_confirm.append(item)

    context = {
        'transfers': transfers_to_confirm
    }
    return render(request, 'admin_confirmation.html', context)


@csrf_exempt
@user_passes_test(lambda user: user.is_superuser)
def admin_transfers(request):
    context = {
        'transfers': Transfer.objects.all()
    }

    return render(request, 'admin_transfers.html', context)


def new_transfer(request):
    if request.method == 'POST':
        form = TransferForm(request.POST)
        if form.is_valid():
            context = {
                'form': form,
                'transfer': form.cleaned_data
            }
            return render(request, 'confirm_transfer.html', context)
    else:
        form = TransferForm()
    return render(request, 'new_transfer.html', {'form': form})


@csrf_exempt
def sql_injection(request):
    form = SQLInjectionForm()

    if request.method == 'POST':
        form = SQLInjectionForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            title = data.get('title')

            with connection.cursor() as c:
                c.execute(f'select * from public."BarchuckBank_transfer" where title ilike \'%{title}%\'')

                context = {
                    'form': form,
                    'response': c.fetchall()
                }

                return render(request, 'sql_injection.html', context)

    context = {
        'form': form,
        'response': {}
    }

    return render(request, 'sql_injection.html', context)


class Register(generic.CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'
