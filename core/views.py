from django.shortcuts import render
import folium
from folium.plugins import FastMarkerCluster
from .models import EVChargingLocation


# Create your views here.
def index(request):

    # careting a folium map
    stations = EVChargingLocation.objects.all()
    m = folium.Map(location=[stations[0].latitude, stations[0].longitude], zoom_start=9, )
    
    # adding markers to the map
   #for station in stations:

    #   coordinates = (station.latitude, station.longitude)
    #   folium.Marker(coordinates, popup=station.station_name).add_to(m)

    # adding fast marker cluster to the map
    longitude = [station.longitude for station in stations]
    latitude = [station.latitude for station in stations]

    FastMarkerCluster(data=list(zip(latitude, longitude))).add_to(m)


    context = {'map': m._repr_html_()}
    return render(request, 'index.html', context)   