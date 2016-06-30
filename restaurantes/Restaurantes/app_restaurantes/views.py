from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from app_restaurantes.models import Restaurante, Platos
from django.contrib.auth.decorators import login_required
from django import forms
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from app_restaurantes.models import Restaurante
from app_restaurantes.serializers import RestauranteSerializer



# Create your views here.

def index (request):
	lista = Restaurante.objects.all()
	context= {'mensaje': 'restaurantes!','restaurante': lista [:]}
	return render (request, 'base.html', context)

@login_required
def like_category(request):

    cat_id = None
    if request.method == 'GET':
        cat_id = request.GET.get('me_gusta','')

    likes = 0
    if cat_id:
        cat = Restaurante.objects.get(id=cat_id)
        if cat:
            likes = cat.me_gusta + 1
            cat.me_gusta =  likes
            cat.save()

    print cat_id

    return HttpResponse(likes)

@csrf_exempt
@api_view(['GET','POST'])

def restauranteCollection(request):
    if request.method == 'GET':
        restaurante = Restaurante.objects.all()
        serializer = RestauranteSerializer(restaurante, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = RestauranteSerializer(data=request.data)
       

        if serializer.is_valid():
            serializer.save()
            print('vale')
            return JsonResponse(serializer.data, status=201)
   
    return JsonResponse(serializer.errors, status=400)

   





    #if request.method == 'DELETE':



@api_view(['GET','PUT','DELETE'])
def restauranteElement(request,pk):
    try:
        restaurante = Restaurante.objects.get(id=pk)
    except Restaurante.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = RestauranteSerializer(restaurante)
        return Response(serializer.data)
        
    if request.method == 'DELETE':
        restaurante.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'PUT':
        nombreR = Restaurante.objects.get(nombre=nombre)
        direccionR = Restaurante.objects.get(direccion=direccion)
        imagenR = Restaurante.objects.get(imagen=imagen)
        me_gustaR = Restaurante.objects.get(me_gusta=me_gusta)
        nombreR.save()
        direccionR.save()
        imagenR.save()
        me_gustaR.save()
    return Response(status=status.HTTP_201_OK)








#MongEngine esto no funciona del todo 
class PlatosForm(forms.Form):
    nombre = forms.CharField(max_length=128, label='Anadir tapa')
    precio = forms.FloatField(label='Anadir precio')
    imagen = forms.CharField(max_length=150, label='Anadir imagen')
    
def add_plato(request,nombre):
    context={}
    form=PlatosForm()

    try:
        restaurante = Restaurante.objects.get(nombre=nombre)
        platos = Platos.objects.filter(nombre=restaurante)
        context={'restaurante':restaurante,'platos':platos,'form':form},


        if request.method == 'POST':
            form = PlatosForm(request.POST)
            context['form'] = form
            if form.is_valid():
                try:
                    plato = form.save(commit=false)
                    plato.restaurante = restaurante

                    if 'imagen' in request.FILES:
                        plato.imagen= request.FILES['imagen']


                    plato.save()

                except IntegrityError as e:
                    messages.error(request,str(e))

    except Restaurante.DoesNotExist:
        pass

    return render (request,'app_restaurantes/add_plato.html',context)




