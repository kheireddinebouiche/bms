from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *

####################################################################################################

                                    ## ACTION SUR LES PROPRIETES ##

####################################################################################################
@login_required(login_url='/login/')
def ListEstate(request):
    if request.user.is_staff:
        result = Proprietes.objects.filter(user = request.user)
        context = {
            'result' : result
        }
        return render(request, 'backend/estate/list-propriete.html', context)

    else:
        return redirect("app:index")

@login_required(login_url='/login/')
def CreatePropreite(request):
    if request.user.is_staff:
        form = ProprieteForm()
        if request.method == 'POST':
            form = ProprieteForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('estate:list-des-propriete')
        
        context = {
            'form' : form,
        }
        return render(request, 'backend/estate/create-propriete.html', context)
    else:
        return redirect('app:index')

@login_required(login_url='/login/')
def UpdatePropriete(request, pk):
    if request.user.is_staff:
        result = Proprietes.objects.get(id=pk)
        form = ProprieteForm(instance=result)
        if request.method == 'POST':
            form = ProprieteForm(request.POST, instance=result)
            if form.is_valid():
                form.save()
                return redirect("estate:list-des-propriete")

        context = {
            'form' : form
        }
        return render(request, 'backend/estate/update-propriete.html', context)
    else:
        return redirect("app:index")

@login_required(login_url='/login/')
def DeletePropreite(request, pk):
    if request.user.is_staff:
        result = Proprietes.objects.get(id=pk)
        result.delete()
        return redirect("estate:list-des-propriete")
    else:
        return redirect("app:index")

@login_required(login_url='/login/')
def DetailsPropreite(request, pk):
    if request.user.is_staff:    
        
        result = Proprietes.objects.get(id=pk)
        try:
            comments = Comments.objects.filter(propriete = result)
            reponse = Response.objects.filter(comments = comments)
            context = {
                'result' : result,
                'comments' : comments,
                'reponse' : reponse,
            }
        except:
            context = {
                'result' : result,              
            }
            return render(request, "backend/estate/details-proprietes.html", context)

    else:
        return redirect("app:index")


####################################################################################################

                                    ## ACTION SUR LES TYPES ##

####################################################################################################

@login_required(login_url='/login/')
def CreateType(request):
    if request.user.is_staff:
        form = TypeForm()
        if request.method == 'POST':
            form = TypeForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('estate:')
        context = {
            'form' : form
        }
        return render(request, 'backend/estate/create-type.html', context)

    else:
        return redirect('app:index')

@login_required(login_url='/login/')
def UpdateType(request, pk):
    if request.user.is_staff:
        result = TypePropriete.objects.get(id=pk)
        form = TypeForm(instance=result)
        if request.method == 'POST':
            form = TypeForm(request.POST, instance=result)
            if form.is_valid():
                form.save()
                return redirect('estate:')
        context = {
            'form': form
        }
        return render(request, 'backend/estate/update-type.html', context)
    else:

        return redirect("app:index")

@login_required(login_url='/login/')
def DeleteType(request, pk):
    if request.user.is_staff:
        result = TypePropriete.objects.get(id=pk)
        result.delete()
        return redirect('estate:')
    else:
        return redirect('app:index')

@login_required(login_url='/login/')
def DetailsType(request, pk):
    if request.user.is_staff:
        result = TypePropriete.objects.get(id=pk)
        context = {
            'result' : result
        }
        return render(request, 'backend/estate/details-type.html', context)
    else:
        return redirect("app:index")

@login_required(login_url='/login/')
def ListeType(request, pk):
    if request.user.is_staff:
        result = TypePropriete.objects.get(id=pk)
        context = {
            'result' : result
        }
        return render(request, 'backend/estate/list-type.html', context)
    else:
        return redirect('app:index')

####################################################################################################

                            ## ACTION SUR LES OPTIONS DES PROPRIETES ##

####################################################################################################

@login_required(login_url='/login/')
def CreatePropOptions(request):
    if request.user.is_staff:
        form = ProprieteOptionForm()
        if request.method == 'POST':
            form = ProprieteOptionForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('estate:liste-proprietee-options')
        context = {
            'form' : form
        }
        return render(request, 'backend/estate/create-prop-option.html', context)
    else:
        return redirect('app:index')


@login_required(login_url='/login/')
def UpdatePropOptions(request,pk):
    if request.user.is_staff:
        result = ProprieteOptions.objects.get(id=pk)
        form = ProprieteOptionForm(instance=result)
        if request.method == 'POST':
            form = ProprieteOptionForm(request.POST, instance=result)
            if form.is_valid():
                form.save()
                return redirect('estate:liste-proprietee-options')
        context = {
            'form' : form,
        }
        return render(request, 'backend/estate/update-prop-option.html', context)
    else:
        return redirect('app:index')

@login_required(login_url='/login/')
def detailsPropOptions(request, pk):
    if request.user.is_staff:
        result = ProprieteOptions.objects.get(id=pk)
        context = {
            'result' : result
        }
        return render(request,'backend/estate/details-prop-option.html', context)
    else:
        return redirect('app:index')

@login_required(login_url='/login/')
def DeletePropOptions(request, pk):
    if request.user.is_staff:
        result = ProprieteOptions.objects.get(id=pk)
        result.delete()
        return redirect('estate:liste-proprietee-options')
    else:
        return redirect('app:index')

@login_required(login_url='/login/')
def ListPropOptions(request):
    if request.user.is_staff:
        result = ProprieteOptions.objects.all()
        context = {
            'result' : result
        }
        return render(request, 'backend/estate/list-prop-options.html', context)

    else:
        return redirect('app:index')

####################################################################################################

                                ## ACTION SUR LES COMMENTAIRES ##

####################################################################################################




####################################################################################################

                            ## ACTION SUR LES REPONSES DES COMMENTAIRES ##

####################################################################################################
