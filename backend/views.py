from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from app.models import *
from app.forms import *
from django.contrib.auth.decorators import login_required

def index(request):
    configure = Profile.objects.get(user = request.user)

    context = {
        'configure' : configure,
    }

    return render(request,"backend/index.html", context)

############################################## GESTION DE LA SOCIETE ##################################################################
def ConfigreMySociete(request):
    form = CreateSocieteForm()
    if request.method == 'POST':
        form = CreateSocieteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('backend:index')

        else:
            return render(request, 'lien vers page erreur')

    context = {
        'form' : form,
    }

    return render(request, 'backend/configuration-societe.html', context)

############################################## ! GESTION DE LA SOCIETE ################################################################

############################################## GESTION DES PROFILS ####################################################################
@login_required(login_url='/login/')
def ListPros(request):
    result = Profile.objects.filter(is_entreprise = True)
    context = {
        'result' : result,
    }

    return render(request, 'backend/list_pros.html', context)

@login_required(login_url='/login/')
def ListClient(request):
    result = Profile.objects.filter(is_entreprise = False)
    context = {
        'result': result,
    }
    return render(request, 'backend/list_client.html', context)

@login_required(login_url='/login/')
def ActivateProfile(request, pk):
    result = User.objects.get(id = pk)
    result.is_active = True
    result.save()
    return redirect('backend:liste-profs')

@login_required(login_url='/login/')
def DeactivateProfile(request, pk):
    result = User.objects.get(id=pk)
    result.is_active = False
    result.save()
    return redirect('backend:liste-profs')

@login_required(login_url='/login/')
def DetailsProfile(request, pk):
    result = Profile.objects.filter(id = pk)
    context = {
        'result' : result,
    }
    return render(request, 'backend/details-profile.html', context)

@login_required(login_url='/login/')
def SuspendProfile(request, pk):
    result = Profile.objects.get(id = pk)
    result.is_active = False
    result.save()
    return redirect('backend:details-compte')

@login_required(login_url='/login/')
def RemovePofile(request, pk):
    result = Profile.objects.get(id = pk)
    result.Delete()
    return redirect('backend:index')

##############################################! GESTION DES PROFILS ###################################################################

############################################## GESTION DES SERVICES ###################################################################
@login_required(login_url='/login/')
def CreatService(request):
    form = CreateServiceForm()
    if request.method == 'POST':
        form = CreateServiceForm(request.POST)
        if form.is_valid():
            designation = form.cleaned_data.get('designation')

            service =  Services(
                designation = designation,
                entreprise = request.user.societe
            )

            service.save()
            return redirect('backend:liste-des-services')
    context = {
        'form' : form,
    }

    return render(request, 'backend/ajout-service.html', context)

@login_required(login_url='/login/')
def ShowServicesBySociete(request):
    societe = Societe.objects.get(gerant = request.user)
    result = Services.objects.filter(entreprise = societe)

    context = {
        'result': result,
    }

    return render(request, 'backend/mes-services.html', context)

@login_required(login_url='/login/')
def ListService(request):
    result = Services.objects.all()

    context = {
        'result': result,
    }
    return render(request, 'backend/list-services.html', context)

@login_required(login_url='/login/')
def UpdateService(request, pk):
    result = Services.objects.get(id=pk)
    form = UpdateServiceForm(instance=result)

    context = {
        'form' : form,
    }
    return render(request, 'backend/mise-a-jour-service.html', context)

@login_required(login_url='/login/')
def UpdateMyService(request):
    pass

@login_required(login_url='/login/')
def RemoveService(request):
    pass

@login_required(login_url='/login/')
def SearchService(request):
    pass

######################################### ! GESTION DES SERVICES #####################################################################

def ConfigurationSociete(request):
    form = ConfigurationSocieteForm()
    if request.method == 'POST':
        form = ConfigurationSocieteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('backend:index')

    context = {
        'form' : form,
    }

    return render(request, 'backend/configration-societe.html', context)

########################################################## GESTION DES TICKETS ###########################################################

def CreateTicket(request):
    form = CreateTicketForm()
    if request.method == 'POST':
        form = CreateTicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('backend:index')

    context={
        'form' : form,
    }

    return render(request, 'backend/creer-ticket.html', context)

def UpdateTicket(request):
    pass

def ListeTicket(request):
    result = Ticket.objects.all()

    context = {
        'result': result,
    }

    return render(request, 'backend/list-tickets.html',context)

def ListDeMesTicket(request):
    result = Ticket.objects.filter(user = request.user)

    context = {
        'result' : result,
    }

    return render(request, 'backend/list-de-mes-ticket.html', context)

def RemoveTicket(request, pk):
    result = Ticket.objects.get(id = pk)
    result.delete()
    return redirect('backend:liste-des-tickets')

def SearchTicket(request):
    pass

def CreateTicketType(request):
    form = CreateTypeTicketForm()
    if request.method == 'POST':
        form = CreateTypeTicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('backend:index')

    context = {
        'form' : form,
    }

    return render(request, 'backend/creer-type-ticket.html',context)

def UpdateTicketType(request):
    pass

def ListeTicketType(request):
    result = TypeTicket.objects.all()

    context = {
        'result' : result,
    }

    return render(request, 'backend/list-type-tickets.html', context)

def RemoveTicketType(request):
    pass

def SearchTicketType(request):
    pass

########################################################## !GESTION DES TICKETS ###########################################################

###################################################### GESTION DES EMAILS DE CONTACT ###############################################


def ListContact(request):
    result = Contact.objects.all()
    context = {
        'result' : result,
    }
    return render(request, 'backend/liste-contact.html', context)

def DetailsContact(request, pk):
    result = Contact.objects.get(id=pk)
    context = {
        'result' : result,
    }
    return render(request, 'backend/detail-contact.html', context)

def RemoveContact(request, pk):
    result = Contact.objects.get(id=pk)
    result.delete()
    return redirect('backend:list-contact')

def SearchContact(request):
    pass

def ReponsContact(request):
    pass

###################################################### ! GESTION DES EMAILS DE CONTACT #############################################

def Tables(request):
    return render(request, 'backend/tables.html')
