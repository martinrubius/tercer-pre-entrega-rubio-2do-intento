from django.shortcuts import render
from app1.models import *
from django.http import HttpResponse
from app1.forms import *
from django.db.models import Q

# Create your views here.
def inicio(request):
    return render(request, 'app1/inicio.html')

def medicos(request):
    queryset = request.GET.get('buscar')
    print(queryset)
    
    if queryset:
        formulario=Medico.objects.filter(
            Q(nombre__icontains = queryset) |
            Q(apellido__icontains = queryset) |
            Q(especialidad__icontains = queryset)
        )
        print(formulario)
        return render(request,'app1/verBusqueda.html',{"formulario":formulario})
    else:
        return render(request,'app1/medicos.html')

def pacientes(request):
    queryset = request.GET.get('buscar')
    print(queryset)
    
    if queryset:
        formulario=Paciente.objects.filter(
            Q(nombre__icontains = queryset) |
            Q(apellido__icontains = queryset) |
            Q(email__icontains = queryset)
        )
        print(formulario)
        return render(request,'app1/verBusqueda.html',{"formulario":formulario})
    else:
        return render(request,'app1/pacientes.html')

def turnos(request):
    return render(request,'app1/turnos.html')

def buscar(request):
    return render(request,'app1/buscar.html')


def medicoFormulario(request):
    if request.method == "POST":
        miFormulario = MedicoFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            medico = Medico(int(informacion['id']),str(informacion['nombre']),str(informacion['apellido']), informacion['email'], informacion['especialidad'])
            medico.save()
            return render(request, "app1/inicio.html")
    else:
        miFormulario = MedicoFormulario()

    return render(request, "app1/medicoFormulario.html", {"miFormulario": miFormulario})

def pacienteFormulario(request):
    if request.method == "POST":
        miFormulario = PacienteFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            paciente = Paciente(int(informacion['id']),str(informacion['nombre']),str(informacion['apellido']), informacion['email'], informacion['dni'])
            paciente.save()
            return render(request, "app1/inicio.html")
    else:
        miFormulario = PacienteFormulario()

    return render(request, "app1/pacienteFormulario.html", {"miFormulario": miFormulario})

def turnoFormulario(request):
    if request.method == "POST":
        miFormulario = TurnoFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            turno = Paciente(int(informacion['id']),int(informacion['dniPaciente']),str(informacion['fecha']), informacion['apellidoMedico'])
            turno.save()
            return render(request, "app1/inicio.html")
    else:
        miFormulario = TurnoFormulario()

    return render(request, "app1/turnoFormulario.html", {"miFormulario": miFormulario})


def leerMedicos(request):
    medicos= Medico.objects.all() # trae a todos los medicos
    contexto= {"medicos": medicos}
    return render(request, "app1/leerMedicos.html",contexto)

def leerPacientes(request):
    pacientes= Paciente.objects.all() # trae a todos los pacientes
    contexto= {"pacientes": pacientes}
    return render(request, "app1/leerPacientes.html",contexto)

def leerTurnos(request):
    turnos= Turno.objects.all() # trae a todos los turnos
    contexto= {"turno": medicos}
    return render(request, "app1/leerTurnos.html",contexto)















