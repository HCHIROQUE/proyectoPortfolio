from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .forms import InputForm
from .forms import aniade_item_forms
from django.contrib import messages

# #Con funciones
# def index_view(request):
#     if request.method == "GET":
#         print("GET")
#     elif request.method == "POST":
#         print("POST")
#         return HttpResponse("Index POST")

#     context = {}
#     context["name"] = "Juan"
#     return render(request, "index.html",context)

#Con clases
class index_view(View):
    #Añadimos el template como atributo
    template = "index.html"
    #context = {"name":"Juan"}

    def get(self, request):
        print("GET")

        #Usando el renderizado de un template
        return render(request, self.template, {}) #self.context

    def post(self, request):
        if request.method == "POST":
            login = InputForm(request.POST)
            if login.is_valid():
                print("POST")
                request.session['password'] = str(login.cleaned_data["password"])
                return redirect("username", username= login.cleaned_data["username"])
        

def form_view(request):
    if request.method == "POST":
        login = InputForm(request.POST)
        if login.is_valid():
            # return HttpResponse(
            #     "Ingresaste el aula "
            #     + form.cleaned_data["aula"]
            #     + " y tiene la hora de entrada "
            #     + str(form.cleaned_data["hora_entrada"])
            # )   
            
            # Uso de la sesión para añadir un nuevo dato
            request.session['password'] = str(login.cleaned_data["password"])

            return redirect("username", username= login.cleaned_data["username"])
    context = {}
    context['login']= InputForm()        
    return render(request, "index.html", context)

def aula_view(request, username):
    # Uso de la sesión para obtener el dato
    password = request.session["password"]
    context = {}
    context['name']= "portfolios"        
    return render(request, "index.html", context)
    #return HttpResponse(f"Bienvenido {username}, tu password es {password}")
    


def aniade_item_views(request):
    form = aniade_item_views(request.POST or None)
    if form.is_valid():
        form.save()		
        messages.success(request, 'Item insertada correctamente.')
        form = aniade_item_views()
    else:
        messages.error(request, 'Error al insertar Item. Revise los datos.')
    context = {}   
    #context['form']= "portfolios"    
    return render(request, 'items.html', context)
