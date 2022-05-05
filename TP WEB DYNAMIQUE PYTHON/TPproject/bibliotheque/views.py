from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import LivreForm
from .forms import ArmeForm

from . import  models
# Create your views here.
def ajout(request):
    if request.method == "POST":
        form = LivreForm(request)
        if form.is_valid():
            livre = form.save()
            return HttpResponseRedirect("/bibliotheque/")
        else:
            return render(request,"bibliotheque/ajout.html",{"form": form})
    else :
        form = LivreForm()
        return render(request,"bibliotheque/ajout.html",{"form" : form})

def traitement(request):
    lform = LivreForm(request.POST)
    if lform.is_valid():
        livre = lform.save()
        return HttpResponseRedirect("/bibliotheque/")
    else:
        return render(request,"bibliotheque/ajout.html",{"form": lform})


def main(request):
    liste = list(models.Livre.objects.all())
    return render(request, 'bibliotheque/main.html', {'liste': liste})

def affiche(request, id):
    livre = models.Livre.objects.get(pk=id)
    return render(request,"bibliotheque/affiche.html",{"livre" : livre})

def delete(request, id):
    livre = models.Livre.objects.get(pk=id)
    livre.delete()
    return HttpResponseRedirect("/bibliotheque/")

def update(request, id):
    lform = LivreForm(request.POST)
    if lform.is_valid():
        livre = lform.save()
        return HttpResponseRedirect("/bibliotheque/")
    else:
        return render(request, "bibliotheque/update.html", {"form": lform})

def traitementupdate(request, id):
    lform = LivreForm(request.POST)
    if lform.is_valid():
        livre = lform.save(commit=False)
        livre.id = id;
        livre.save()
        return HttpResponseRedirect("/bibliotheque/")
    else:
        return render(request, "bibliotheque/update.html", {"form": lform, "id": id})




def ajout2(request):
    if request.method == "POST":

        form = ArmeForm(request)
        if form.is_valid():
            arme = form.save()
            return render(request,"bibliotheque/ajout2.html",{"arme" : arme})

        else:
            return render(request,"bibliotheque/ajout2.html",{"form": form})
    else :
        form = ArmeForm()
        return render(request,"bibliotheque/ajout2.html",{"form" : form})

def traitement2(request):
    mform = ArmeForm(request.POST)
    if mform.is_valid():
        arme = mform.save()
        return render(request,"bibliotheque/affiche.html",{"arme" : arme})
    else:
        return render(request,"bibliotheque/ajout2.html",{"form": mform})


def delete2(request, id):
    arme = models.Arme.objects.get(pk=id)
    arme.delete()
    return HttpResponseRedirect("/bibliotheque/")

def update2(request, id):
    mform = ArmeForm(request.POST)
    if mform.is_valid():
        arme = mform.save()
        return HttpResponseRedirect("/bibliotheque/")
    else:
        return render(request, "bibliotheque/update.html", {"form": mform})

def traitementupdate2(request, id):
    mform = ArmeForm(request.POST)
    if mform.is_valid():
        arme = mform.save(commit=False)

        arme.id = id ;
        arme.save()
        return HttpResponseRedirect("/bibliotheque/ajout2")
    else:
        return render(request, "bibliotheque/update.html", {"form": mform, "id": id})