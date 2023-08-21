from django.shortcuts import HttpResponse, render, redirect
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

# -- bulk update
def seg_form(request):
    return render(request, 'app/contacts_table_rows.html', {
        'contacts': Contact.objects.all(), # type: ignore
    })

def bulk_update(request):
    return render(request, 'app/bulk_update_form.html')

def activate_rows(request):
    params = QueryDict(request.body).dict()
    for id_ in params.get('ids', []):
        contact = Contact.objects.get(id=int(id_)) # type: ignore
        contact.active = True
        contact.save()
    return seg_form(request)

def deactivate_rows(request):
    params = QueryDict(request.body).dict()
    for id_ in params.get('ids', []):
        contact = Contact.objects.get(id=int(id_)) # type: ignore
        contact.active = False
        contact.save()
    return seg_form(request)

