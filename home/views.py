from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import iris
from django.views import generic


# Create your views here.
def rend(request):
    # return HttpResponse("I am here")
    num_predictions = iris.objects.all().count()
    # return HttpResponse("Number of irises :: "+str(num_predictions))
    # context={
    #     'num_predictions' : num_predictions,
    # }

    return render(request,'index.html',{"num_predictions" : num_predictions})

def inp(request):
    return render(request, 'new.html')

class list_of_iris(generic.ListView):
    model = iris
    context_object_name = "predictions_list"
    queryset = iris.objects.all()
    template_name = 'iris_list.html'

def success(request):
    if request.method == 'POST':
        s_length = request.POST['sepal_length']
        s_width = request.POST['sepal_width']
        p_length = request.POST['petal_length']
        p_width = request.POST['petal_width']

        content = [s_length, s_width, p_length, p_width]

        obj = iris()
        obj.input(content)
        obj.get_species()
        # obj.save()
        return render(request, 'success.html', {'iris':obj})
    else:
        return redirect('input')