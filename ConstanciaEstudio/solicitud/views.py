from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic.edit import FormView
from .forms import SolicitudForm
from django.http import HttpResponse

# Aqui hacemos que funcione el formulario y se envie la informacion correctamente

def solicitud(request):
    
    solicitud_form = SolicitudForm()
        
    if request.method == "POST":
        solicitud_form = SolicitudForm(request.POST)
            
        if solicitud_form.is_valid():
                
                
            solicitud_form.save()
                
                
                
            messages.success(request, 'Tu solicitud ha sido un exito')
            return redirect('inicio')
    
    
    
    
    return render(request, 'solicitud.html', {
        'title': 'Solicitud',
        'solicitud_form': solicitud_form
    })