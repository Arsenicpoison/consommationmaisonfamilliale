from django.http import HttpRequest
from django.shortcuts import render
from app.models import Prevision,Acheter

def index(request):
    total_prevision=Prevision.objects.count()
    total_acheter=Acheter.objects.count()
    total=totalModel1(Prevision.objects.all())
    totale =totalModel2(Acheter.objects.all())
    previsions = Prevision.objects.all()
    acheter = Acheter.objects.all()
    
    return render(
        request,
        'app/home/index.html',
        {
            'total_prevision': total_prevision,
            'total_acheter':total_acheter,
            'total': total,
            'totale': totale,
            'previsions': previsions,
            'acheter': acheter

        }
    )
def totalModel1(models):
  return sum(model.total for model in models)

def totalModel2(models):
    return sum(model.total for model in models)
   
