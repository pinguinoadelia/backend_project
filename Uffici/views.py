from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from .models import Reparto
from .forms  import RepartoForm

def is_office_chief(user):
    return user.is_superuser or user.groups.filter(name='Office Chiefs').exists()

@user_passes_test(is_office_chief)
def reparti_list(request):
    reparti = Reparto.objects.all()
    return render(request, 'uffici/reparti_list.html', {'reparti': reparti})

@user_passes_test(is_office_chief)
def reparto_edit(request, pk):
    reparto = get_object_or_404(Reparto, pk=pk)
    if request.method == 'POST':
        form = RepartoForm(request.POST, instance=reparto)
        if form.is_valid():
            form.save()
            return redirect('reparti_list')
    else:
        form = RepartoForm(instance=reparto)

    return render(request, 'uffici/reparto_edit.html', {
        'reparto': reparto,
        'form': form,
    })
