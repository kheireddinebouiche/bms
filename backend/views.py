from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from app.models import *
from app.forms import *
from django.contrib.auth.decorators import login_required

def BackIndex(request):

    if request.user.profile.is_entreprise == True or request.user.is_authenticated:

        if request.user.profile.is_configured == False:

            configure = Profile.objects.get(user = request.user)

            context = {
                'configure' : configure,
            }

            return render(request,"backend/index.html", context)

        else:

            return HttpResponse("Vous n'avez pas encore configurer les informations de votre entreprise")

    else:

        return redirect('app:index')

############################################## GESTION DE LA SOCIETE ##################################################################
@login_required(login_url='/login/')
def ConfigreMySociete(request):

    if request.user.is_entreprise == True:


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

    else: 

        return redirect('app:index')

############################################## ! GESTION DE LA SOCIETE ################################################################

############################################## GESTION DES PROFILS ####################################################################
@login_required(login_url='/login/')
def ListPros(request):

    if request.user.is_staff == True:

        result = Profile.objects.filter(is_entreprise = True)
        context = {
            'result' : result,
        }

        return render(request, 'backend/profiles/list_pros.html', context)

    else:

        return redirect('app:index')

@login_required(login_url='/login/')
def ListClient(request):

    if request.user.is_staff == True:

        result = Profile.objects.filter(is_client = True)
        context = {
            'result': result,
        }
        return render(request, 'backend/profiles/list_client.html', context)
    else:

        return redirect('app:index')

@login_required(login_url='/login/')
def SellerIndividual(request):
    if request.user.is_staff:
        result = Profile.objects.filter(is_seller_individual = True)
        context = {
            'result' : result,
        }
        return render(request, 'backend/profiles/list-seller.html',context)
    else:
        return redirect('app:index')

@login_required(login_url='/login/')
def SellerEntreprise(request):
    result = Profile.objects.filter(is_seller_entrepris = True)
    context = {
        'result' : result,
    }
    return render(request, 'backend/list-seller.html', context)

@login_required(login_url='/login/')
def ListDemandeAgImm(request):
    if request.user.is_staff:
        result = Profile.objects.filter(user__is_active = False)
        context = {
            'result' : result,
        }
        return render(request, 'backend/profiles/demandes-ins-ag-im.html', context)
    else:
        return redirect('app:index')

@login_required(login_url='/login/')
def ActivateProfile(request, pk):
    if request.user.is_staff == True:
        result = User.objects.get(id = pk)
        result.is_active = True
        result.save()
        return redirect('backend:liste-profs')
    else:
        return redirect('app:index')

@login_required(login_url='/login/')
def DeactivateProfile(request, pk):
    if request.user.is_staff == True:

        result = User.objects.get(id=pk)
        result.is_active = False
        result.save()
        return redirect('backend:liste-profs')

    else:

        return redirect('app:index')

@login_required(login_url='/login/')
def DetailsProfile(request, pk):
    if request.user.is_entreprise == True:

        result = Profile.objects.filter(id = pk)
        context = {
            'result' : result,
        }
        return render(request, 'backend/details-profile.html', context)

    else: 

        return redirect('app:index')

@login_required(login_url='/login/')
def SuspendProfile(request, pk):
    if request.user.is_staff == True:

        result = Profile.objects.get(id = pk)
        result.is_active = False
        result.save()
        return redirect('backend:details-compte')

    else:

        return redirect('app:index')

@login_required(login_url='/login/')
def RemovePofile(request, pk):
    if request.user.is_staff == True:
        result = Profile.objects.get(id = pk)
        result.Delete()
        return redirect('backend:index')
    else:

        return redirect('app:index')

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

############################################## GESTION DES SERVICES ##################################################################

################################################ GESTION DES CATEGORIES ##############################################################

@login_required(login_url='/login/')
def CreateCategorie(request):
    if request.user.is_staff:
        form = CategorieForm()
        if request.method == 'POST':
            form = CategorieForm(request.POST)
            form.save()

            return redirect('backend:list-categorie')
        
        context = {
            'form': form,
        }

        return render(request, 'backend/create-categorie.html', context)
    else:
        return redirect('app:index')

@login_required(login_url='/login/')
def ListeCategorie(request):
    if request.user.is_staff:
        result = Categorie.objects.all()
        context = {
            'result' : result
        }
        return render(request, 'backend/list-categorie.html', context)
    else:
        return redirect('app:index')

@login_required(login_url='/login/')
def UpdateCategorie(request, pk):
    if request.user.is_staff == True:
        result = Categorie.objects.get(id=pk)
        form = CategorieForm(instance=result)
        if request.method == 'POST':
            form = CategorieForm(request.POST, instance=result)
            if form.is_valid():
                form.save()
                return redirect('backend:list-categorie')
            else:
                return HttpResponse('erreur')
        
        context = {
            'form' : form
        }

        return render(request, 'backend/update-categorie.html', context)

    else:

        return redirect('backend:index')

@login_required(login_url='/login/')
def DeleteSecteur(request, pk):
    if request.user.is_staff:
        result = Categorie.objects.get(id=pk)
        result.delete()
        return redirect('backend:list-categorie')
    else:
        return redirect('app:index')

############################################# FIN GESTION DES CATEGROEIS #############################################################


######################################### ! GESTION DES SERVICES #####################################################################

@login_required(login_url='/login/')
def ConfigurationSociete(request):
    if request.user.profile.is_entreprise or request.user.profile.is_seller_entreprise:
        form = ConfigurationSocieteForm()
        if request.method == 'POST':
            form = ConfigurationSocieteForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('backend:index')

        context = {
            'form' : form,
        }

        return render(request, 'backend/configuration-societe.html', context)

    else:

        return redirect('app:index')

@login_required(login_url='/login/')
def DetailsSociete(request, pk):
    if request.user.is_entreprise or request.user.is_seller_entreprise:
        pass

@login_required(login_url='/login/')
def UpdateSocieteDetails(request, pk):
    if request.user.is_entreprise or request.user.is_seller_entreprise:
        pass

@login_required(login_url='/login/')
def DeleteSociete(request, pk):
    if request.user.is_entreprise or request.user.is_seller_entreprise:
        pass
    pass


########################################################## GESTION DES TICKETS ###########################################################

@login_required(login_url='/login/')
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

@login_required(login_url='/login/')
def NotificationCreateTicket():
    pass

@login_required(login_url='/login/')
def UpdateTicket(request):
    pass

@login_required(login_url='/login/')
def NotificationUpdateTicket():
    pass

@login_required(login_url='/login/')
def ListeTicket(request):
    result = Ticket.objects.all()

    context = {
        'result': result,
    }

    return render(request, 'backend/list-tickets.html',context)

@login_required(login_url='/login/')
def ListDeMesTicket(request):
    result = Ticket.objects.filter(user = request.user)

    context = {
        'result' : result,
    }

    return render(request, 'backend/list-de-mes-ticket.html', context)

@login_required(login_url='/login/')
def RemoveTicket(request, pk):
    result = Ticket.objects.get(id = pk)
    result.delete()
    return redirect('backend:liste-des-tickets')


@login_required(login_url='/login/')
def NotificationUpdateTicket():
    pass

@login_required(login_url='/login/')
def NotificationRemove():
    pass

@login_required(login_url='/login/')
def SearchTicket(request):
    pass

@login_required(login_url='/login/')
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


@login_required(login_url='/login/')
def NotificationCreateTicketType():
    pass

@login_required(login_url='/login/')
def UpdateTicketType(request):
    pass

@login_required(login_url='/login/')
def NotificationUpdateTicketType():
    pass

@login_required(login_url='/login/')
def ListeTicketType(request):
    result = TypeTicket.objects.all()

    context = {
        'result' : result,
    }

    return render(request, 'backend/list-type-tickets.html', context)

@login_required(login_url='/login/')
def RemoveTicketType(request):
    pass

@login_required(login_url='/login/')
def SearchTicketType(request):
    pass


########################################################## !GESTION DES TICKETS ###########################################################

###################################################### GESTION DES EMAILS DE CONTACT ###############################################

@login_required(login_url='/login/')
def ListContact(request):
    result = Contact.objects.all()
    context = {
        'result' : result,
    }
    return render(request, 'backend/liste-contact.html', context)

@login_required(login_url='/login/')
def DetailsContact(request, pk):
    result = Contact.objects.get(id=pk)
    context = {
        'result' : result,
    }
    return render(request, 'backend/detail-contact.html', context)

@login_required(login_url='/login/')
def RemoveContact(request, pk):
    result = Contact.objects.get(id=pk)
    result.delete()
    return redirect('backend:list-contact')

@login_required(login_url='/login/')
def SearchContact(request):
    pass

@login_required(login_url='/login/')
def ReponsContact(request):
    pass

###################################################### ! GESTION DES EMAILS DE CONTACT #############################################

def Tables(request):
    return render(request, 'backend/tables.html')

###################################################### GESTION DU PROFILE ENTREPRISE ###############################################

@login_required(login_url='/login/')
def EntrepriseProfile(request):
    if request.user.profile.is_entreprise == True:
        result = Profile.objects.filter(user = request.user)
        context = {
            'result' : result,
        }
        return render(request, 'backend/profile-entreprise.html', context)
    else:
        return redirect('app:index')


##################################################### !GESTION DU PROFILE ENTREPRISE ###############################################