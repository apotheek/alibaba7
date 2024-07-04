from django.shortcuts import render
from .models import Trip,TripAttribute,Attribute

# Create your views here.

def tripListView(request):
    trips = Trip.objects.all()  # Correct usage of the manager to get all Trip objects

    context = {                 
        "triptlist": trips, 
        "tripcount": trips.count(), 
    } 

    return render(request, "ticketsales/triplist.html", context)  # Rendering the triplist.html template with the context


def tripDetailsView(request,trip_id):
    trips=Trip.objects.get(pk=trip_id) # dar inja miravad va primary_key = PK az database migirad va barabareh trip_id ma midahad -> concertlist tag <a href="tarif mishavad">

    context={                        
        "tripDetails":trips,        #key

        
    }
    
    return render(request,"ticketsales/tripDetails.html",context) # ->concertDetails.html miravaim va kodei ke be an pass dadeh mishavad ra dar anja namayesh midahim


def tripTimeView(request):
    times=Trip.objects.all()

    context={                        
        "tripTime":times,        #key

        
    }
    
    return render(request,"ticketsales/timelist.html",context) # ->concertDetails.html miravaim va kodei ke be an pass dadeh mishavad ra dar anja namayesh midahim

