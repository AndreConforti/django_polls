from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Client


def clients_index(request):
    latest_five_clients = Client.objects.order_by('-date_register')[:5]
    context = {
        'latest_five_clients': latest_five_clients,
    }
    return render(request, 'clients/clients_index.html', context)


def clients_details(request, id):
    client = get_object_or_404(Client, id=id)
    return render(request, 'clients/clients_detail.html', {'client': client})


def clients_edit(request, id):
    return HttpResponse(f"You're editing the client of number {id}")


def clients_delete(request, id):
    return HttpResponse(f"You're deleting the client of number {id}")
