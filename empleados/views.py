# Create your views here.
from django.shortcuts import render


def index(request):
    nombrempleado = ['Alicia','Susana','Martin', 'Carmen','Marcos','Liliana','Pedro']
    total_empleados = len(nombrempleado)
    context = {
            'nombrempleado' : nombrempleado,
            # Extra
            'total_empleados': total_empleados
               }
    return render(request, "index.html", context)


