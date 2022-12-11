from django.shortcuts import render, redirect

from .forms import FormulariodeContacto

from django.core.mail import EmailMessage

def contacto(request):
    formulario = FormulariodeContacto()
    if request.method == "POST":
        formulario = FormulariodeContacto(data=request.POST)
        if formulario.is_valid():
            nombre = request.POST.get('nombre')
            email = request.POST.get('email')
            mensaje = request.POST.get('mensaje')

            email = EmailMessage("Mensaje desde F1 Stats",
            "El usuario con nombre {} con la direccion {} escribe lo siguiente: \n\n {}".format(nombre, email, mensaje),"",["     "],reply_to=[email])

            try:
                email.send()
                return redirect("/contacto?valido")

            except:
                return redirect("/contacto?novalido")
            return redirect("/contacto?valido")
            
    return render(request, "contacto/contacto.html", {'miFormulario': formulario})
