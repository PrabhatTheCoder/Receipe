from django.shortcuts import render, HttpResponse, redirect
from vege.models import *
from django.http import HttpResponse

# Create your views here.

def receipes(request):
    if request.method == "POST":
        data = request.POST
        
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')
        
        Receipe.objects.create(
            receipe_image =receipe_image,
            receipe_name = receipe_name,
            receipe_description =  receipe_description,
        )
        return redirect('/receipe')

    queryset = Receipe.objects.all()
    if request.GET.get('search'):
        print(request.GET.get('search'))
        queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))

    context = {'receipes' : queryset}
    print(queryset)
    return render(request, 'receipes.html', context)


def delete_receipe(request, id ):
    print(id)
    queryset = Receipe.objects.get(id=id)
    queryset.delete()
    
    return redirect('/receipe')

def update_receipe(request,id):
    queryset = Receipe.objects.get(id=id)

    if request.method == "POST":
        data = request.POST
        
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')
        
        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description
        
        if receipe_image:
            queryset.receipe_image = receipe_image
        
        queryset.save()
        return redirect('/receipe')
        
    context = {'receipe': queryset}
    return render(request, 'update_receipe.html',context)
    