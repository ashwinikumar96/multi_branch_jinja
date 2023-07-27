from django.shortcuts import render

# Create your views here.

def data_render(request):
    return render(request,'data_render.html',context={'name':'Ashwin', 'age':23})