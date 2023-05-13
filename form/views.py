from django.shortcuts import render
from form.forms import custForm
# Create your views here.
def index(request):
    context = {'form':custForm}
    return render(request,'index.html',context)