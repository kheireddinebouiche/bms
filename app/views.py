import datetime
from django.db import transaction
from http.client import HTTPResponse
from django.shortcuts import render,redirect,HttpResponse
from django.http import HttpResponse
from .forms import *
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from backend.models import *
from django.core.mail import send_mail
from django.conf import settings


def index(request):
    form = CreateContactForm()
    
    subject = "Sending an email with Django"
    message = "Une nouvelle demande de création de compte à été initier."
    # send the email to the recipent
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, ['test@com.fr'])

    if request.method=='POST':
        form = CreateContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:index')

    context = {
        'form' : form,
    }  
    return render(request, 'frontend/index.html', context)

@login_required(login_url='/login/')
def MyProfile(request):
    result = Profile.objects.get(user = request.user)
    tickets = Ticket.objects.filter(user = request.user)
    messages = SendMessage.objects.filter(user = request.user)

    context = {
        'result' : result,
        'tickets' : tickets,
        'messages' : messages,
    }
    return render(request,'frontend/profile.html', context)

@login_required(login_url='/login/')
def UpdateProfile(request):
    user_form = UserUpdateForm(instance = request.user)
    profile_form = ProfileUpdateForm(instance= request.user.profile)
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance = request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user)
        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()

            user.profile.adresse = profile_form.cleaned_data.get('adresse')
            user.profile.telephone = profile_form.cleaned_data.get('telephone')
            user.profile.date_naissance = profile_form.cleaned_data.get('date_naissance')
            user.profile.updated_at = datetime.time()

            user.save()

            return redirect('app:mon-profile')

    context = {
        'user_form' : user_form,
        'profile_form' : profile_form,
    }

    return render(request, 'frontend/update-profile.html', context)

@login_required(login_url='/login/')
def DeleteProfile(request):
    pass

@login_required(login_url='/login/')
def ListPro(request):
    result = Profile.objects.filter(is_entreprise = True)
    context = {
        'result' : result,
    }
    return render(request, 'frontend/liste-pros-3.html', context)

def SearchByCat(request):
    pass


def CGU(request):
    return render(request, 'frontend/cgv.html')

def Terms(request):
    return render(request, 'frontend/terms.html')

####################################################### GESTION DES ERREURE ##########################################################

def ServeurError(request):
    pass

def Error404(request):
    pass

###################################################### ! GESTION DES ERREURS #########################################################

#############################################################  INSCRIPTION CLIENT & PRO ##############################################
######################################################################################################################################

def PlaneChoice(request):
    return render(request, 'frontend/pricing.html')

@transaction.atomic
def RegisterClient(request):
    form = ClientCreateForm()
    if request.method == 'POST':
        form = ClientCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.profile.is_client = True
            user.save()
            redirect('app:login')

    context = {
        'form': form,
    }

    return render(request, 'registration/register.html',context)
    
@transaction.atomic
def RegisterPro(request):
    form = ProCreateForm()
    form2 = ProfileProForm()
    if request.method == 'POST':
        form = ProCreateForm(request.POST)
        form2 = ProfileProForm(request.POST)
        if form.is_valid() and form2.is_valid():
            user = form.save() 
            user.is_active = False
            user.profile.is_entreprise = True
            user.profile.is_configured = False
            user.profile.adresse = form2.cleaned_data.get('adresse')
            user.profile.telephone = form2.cleaned_data.get('telephone')
            user.save()     

            return redirect('app:notification-register')
    context = {
        'form' : form,
        'form2' : form2,
    }   
    return render(request, 'frontend/register-pro.html',context )


def RedirectRegister(request):
    return render(request,'frontend/redirect-success-pro.html')

#############################################################  ! INSCRIPTION CLIENT & PRO  ###########################################
######################################################################################################################################


#############################################################  SECTEUR ###############################################################
######################################################################################################################################

@login_required(login_url='/login/')
def CreateSecteur(request):

    if request.user.is_entreprise == True:

        form = SecteurCreateForm()
        if request.method == 'POST':
            form = SecteurCreateForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('backend:index')
            else:
                return HttpResponse('Une erreur est survenu lors du traitement de la request')

        context = {
            'form':form,
        }

        return render(request, 'backend/creer-un-secteur.html', context)
    
    else:

        return redirect('app:index')

@login_required(login_url='/login/')
def ListeSecteur(request):
    if request.user.is_entreprise == True:

        result = Secteur.objects.all()

        context = {
            'result' : result,
        }

        return render(request, 'backend/list-des-secteurs.html', context)
    
    else:

        return redirect('app:index')

@login_required(login_url='/login/')
def UpdateSecteur(request, pk):

    if request.user.is_entreprise == True:

        result = Secteur.objects.get(id=pk)
        form = SecteurCreateForm(instance=result)
        if request.method == "POST":
            form = SecteurCreateForm(request.POST, instance=result)
            if form.is_valid():
                form.save()

                return redirect('backend:liste-des-secteurs')
        

        context = {
            'form': form,
        }

        return render(request, 'backend/mise-a-jours-secteur.html', context)
    else:

        return redirect(request, 'app:index')

@login_required(login_url='/login/')
def RemoveSecteur(request, pk):
    if request.user.is_entreprise == True:

        result = Secteur.objects.get(id=pk)
        result.delete()
        return redirect('backend:liste-des-secteurs')

    else:

        return redirect('app:index')

######################################################################################################################################
#############################################################  ! SECTEUR #############################################################

@login_required(login_url='/login/')
def EnterBackEnd(request):
    if request.user.profile.is_entreprise == True:
        return render(request, 'backend/index.html')
    else:
        return render(request, 'frontend/index.html')




           