from django.shortcuts import render, redirect
from .models import Adresses, Contacts
from .forms import ContactForm


def list_contact(request):
    contacts = Contacts.objects.all()
    return render(request, 'contacts.html', {'contacts': contacts})


def create_contact(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_contact')

    return render(request, 'contacts_form.html', {'form': form})


def update_contact(request, id):
    contacts = Contacts.objects.get(id=id)
    form = ContactForm(request.POST or None, instance=contacts)

    if form.is_valid():
        form.save()
        return redirect('list_contact')

    return render(request, 'contacts_form.html', {'form': form, 'contact': contacts})


def delete_contact(request, id):
    contacts = Contacts.objects.get(id=id)

    if request.method == 'POST':
        contacts.delete()
        return redirect('list_contact')

    return render(request, 'contacts_delete.html', {'contact': contacts})


def list_addresses(request, id):
    contact = Contacts.objects.get(id=id)
    adresses = contact.adresses_set.all()
    return render(request, 'adresses.html', {'adresses': adresses})
