from django.shortcuts import render, HttpResponse, redirect
from users.models import Estilista
from sucursal.models import Sucursal
from services.models import Servicio


# Create your views here.
def index(request):
    return render(request, "mainapp/index.html")


def servicios(request):
    servicio = Servicio.objects.filter(status=True)
    return render(request, "mainapp/servicios.html", {
        'servicios': servicio
    })


def contacto(request):
    if request.method == 'POST':
        name = request.POST.get('nombre')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        mensaje = request.POST.get('mensaje')
        print(name, telefono, correo, mensaje)

    sucursales = Sucursal.objects.filter(status=True)
    print(sucursales)
    return render(request, "mainapp/contacto.html", {
        'sucursales': sucursales
    })


def cita(request):
    if request.method == 'POST' and request.user.is_authenticated:
        pass
    else:
        sucursales = Sucursal.objects.filter(status=True)
        cart = request.session.get('carrito', [])
        servicio_list = []
        total = 0
        servicio_list_distinct = []
        servicio_list_distinct_counter = []
        for producto_id in cart:
            servicio = Servicio.objects.get(pk=producto_id)
            servicio_list.append(servicio)
            total += servicio.precio
            if servicio not in servicio_list_distinct:
                servicio_list_distinct.append(servicio)

        for ser in servicio_list_distinct:
            servicio_list_distinct_counter.append(servicio_list.count(ser))

        return render(request, "mainapp/cita.html", {
            'sucursales': sucursales,
            'servicios': servicio_list,
            'servicios_distintos': servicio_list_distinct,
            'servicios_contador': servicio_list_distinct_counter,
            'total': total
        })


def estilistas(request, sucursal):
    if request.is_ajax():
        estilistas_list = Estilista.objects.filter(sucursal=sucursal)
        options = ""
        for estilista in estilistas_list:
            options += f"<option value={estilista.user.id}>{estilista.user.first_name} {estilista.user.last_name}</option> \n"
        return HttpResponse(options)
    else:
        return HttpResponse("Error 404")


def add_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get("idservicio")
        cart = request.session.get('carrito', [])
        cart.append(product_id)
        request.session['carrito'] = cart
    return redirect('servicios')


def delete_cart(request):
    if request.method == 'POST':
        cart = request.session.get('carrito', [])
        position = request.POST.get('position')
        cart.remove(position)
        request.session['carrito'] = cart
    return redirect('cita')
