from django.shortcuts import render, redirect
from django.http import QueryDict
from .models import Contact

def index(request):
    return redirect(contact, contact_num=1)

def contact(request, contact_num):
    return render(request, 'app/contact.html', {'contact_num': contact_num})

def contact_info(request, contact_num):
    contact = Contact.objects.get(id=contact_num) # type: ignore

    if request.method == 'PUT':
        params = QueryDict(request.body).dict()
        contact.first_name = params.get("firstName")
        contact.last_name = params.get("lastName")
        contact.email_address = params.get("email")
        contact.save()

    return render(request, 'app/contact_info.html', {'contact': contact})

def edit_contact_info(request, contact_num):
    contact = Contact.objects.get(id=contact_num) # type: ignore
    return render(request, 'app/edit_contact_form.html', {'contact': contact})
