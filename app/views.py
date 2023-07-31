from django.shortcuts import render

# Create your views here.

def data_render(request):
    return render(request,'data_render.html',context={'name':'Ashwin', 'age':23, 'hobbies':['cricket','volly']})
def jinja_operations(request):
    return render(request,'jinja_operations.html',context={'a':1000, 'b': 5000, 'c': 200})