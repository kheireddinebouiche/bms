import datetime
from django.db import transaction
from http.client import HTTPResponse
from django.shortcuts import render,redirect,HttpResponse
from django.http import HttpResponse, JsonResponse
from .forms import *
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from backend.models import *
from django.core.mail import send_mail
from django.conf import settings
from search_views.search import SearchListView
from search_views.filters import BaseFilter


def index(request):
    form = CreateContactForm()
    search = SocieteSearchForm()
    
    
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
        'search' : search,
        
    }  
    return render(request, 'frontend/index.html', context)

@login_required(login_url='/login/')
def MyProfile(request):

    if not request.user.profile.is_entreprise or request.user.profile.is_seller_entreprise or request.user.profile.is_seller_individual:
        
        result = Profile.objects.get(user = request.user)
        tickets = Ticket.objects.filter(user = request.user)
        messages = SendMessage.objects.filter(user = request.user)

        context = {
            'result' : result,
            'tickets' : tickets,
            'messages' : messages,
        }
        return render(request,'frontend/profile.html', context)

    else: 
        return EnterBackEnd(request)

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


def ListeSociete(request):
    return render(request, 'frontend/liste-societe.html')

def CGU(request):
    return render(request, 'frontend/cgu.html')

def Terms(request):
    return render(request, 'frontend/terms.html')

####################################################### GESTION DES ERREURE ##########################################################

def ServeurError(request):
    pass

def Error404(request):
    return render(request, "frontend/404.html")

###################################################### ! GESTION DES ERREURS #########################################################

#############################################################  INSCRIPTION CLIENT & PRO ##############################################
######################################################################################################################################

def PlaneChoice(request):
    return render(request, 'frontend/pricing.html')


@transaction.atomic
def RegisterClient(request):
    if not request.user.is_authenticated:
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
    else:
        return redirect('app:index')
    
@transaction.atomic
def RegisterPro(request):
    if not request.user.is_authenticated:

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
                user.profile.pays = form2.cleaned_data.get('pays')
                user.profile.adresse = form2.cleaned_data.get('adresse')
                user.profile.telephone = form2.cleaned_data.get('telephone')
                user.save()

                return redirect('app:notification-register')

        context = {
            'form' : form,
            'form2' : form2,
        }   
        return render(request, 'registration/register-pro.html',context )
    else:
        return redirect('app:index')

#a traiter
@transaction.atomic
def RegisterSellerParticulier(request):
    if not request.user.is_authenticated:

        form1 = SellerUserForm()
        form2 = SellerProfileForm()

        if request.method == 'POST':
            form1 = SellerUserForm(request.POST)
            form2 = SellerProfileForm(request.POST)

            if form1.is_valid() and form2.is_valide():
                user = form1.save()
                user.is_active = False
                user.profile.is_seller_individual == True
                user.profile.pays = form2.cleaned_data.get('pays')
                user.profile.adresse = form2.cleaned_data.get('adresse')
                user.profile.telephone = form2.cleaned_data.get('telephone')
            
                user.save()

                return redirect('app:notification-register')

        context = {
            'form1' : form1,
            'form2' : form2,
        }

        return render(request, 'frontend/seller-register.html', context)
    else:
        return redirect('app:index')

@transaction.atomic
def RegisterSellerEntreprise(request):
    if not request.user.is_authenticated:

        form1 = SellerUserForm()
        form2 = SellerProProfileForm()

        if request.method == 'POST':
            form1 = SellerUserForm(request.POST)
            form2 = SellerProProfileForm(request.POST)

            if form1.is_valid() and form2.is_valide():
                user = form1.save()
                user.is_active = False
                user.profile.is_seller_entreprise == True
                user.profile.secteur = form2.cleaned_data.get('secteur')
                user.profile.categorie = form2.cleaned_data.get('categorie')
                user.profile.pays = form2.cleaned_data.get('pays')
                user.profile.adresse = form2.cleaned_data.get('adresse')
                user.profile.telephone = form2.cleaned_data.get('telephone')

                
                user.save()

                return redirect('app:notification-register')

        context = {
            'form1' : form1,
            'form2' : form2,
        }

        return render(request, 'frontend/seller-register.html', context)
    else:
        return redirect('app:index')

#a traiter
#redirection aprés inscription
def RedirectRegister(request):

    subject = "Demande de création de compte pro"
    message = "Une nouvelle demande de création de compte à été initier."
    # send the email to the recipent
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, ['test@com.fr'])
    
    return render(request,'frontend/redirect-success-pro.html')


def RedirectRegisterClient(request):

    subject = "Notification d'inscription"
    message = "Un nouveau compte client créer"
    # send the email to the recipent
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, ['test@com.fr'])
    
    return render(request,'frontend/redirect-success-pro.html')


#############################################################  ! INSCRIPTION CLIENT & PRO  ###########################################
######################################################################################################################################


#############################################################  SECTEUR ###############################################################
######################################################################################################################################

@login_required(login_url='/login/')
def CreateSecteur(request):

    if request.user.is_staff:

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
    if request.user.is_staff:

        result = Secteur.objects.all()

        context = {
            'result' : result,
        }

        return render(request, 'backend/list-des-secteurs.html', context)
    
    else:

        return redirect('app:index')

@login_required(login_url='/login/')
def UpdateSecteur(request, pk):

    if request.user.is_staff:

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
    if request.user.is_staff:

        result = Secteur.objects.get(id=pk)
        result.delete()
        return redirect('backend:liste-des-secteurs')

    else:

        return redirect('app:index')

######################################################################################################################################
#############################################################  ! SECTEUR #############################################################

@login_required(login_url='/login/')
def EnterBackEnd(request):
    if request.user.profile.is_entreprise == True and request.user.is_authenticated:
        if request.user.profile.is_configured ==True:

            return render(request, 'backend/index.html')

        else:

            return redirect('backend:configuration-societe')
    else:
        return redirect('app:index')




###################################### RECHERCHE ET FILTRAGE #########################################################################

class SocieteFilter(BaseFilter):
    search_fields = {
        'search_text' : ['secteur__designation','categorie__designation', 'designation'],

    }

class SocieteSearchList(SearchListView):
  
  model = Societe
  paginate_by = 30
  template_name = "frontend/filter/search-societe-list.html"
  form_class = SocieteSearchForm
  filter_class = SocieteFilter


###################################### FIN RECHERCHE ET FILTRAGE #####################################################################

def getCategorie(request):
    return JsonResponse("working" , safe=True)
           