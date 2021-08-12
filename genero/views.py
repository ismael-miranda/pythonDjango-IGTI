from django.shortcuts import render, get_object_or_404, redirect
from .forms import GeneroForm
from .models import Genero


def cadastro(request):
    form = GeneroForm()
    if request.method == 'POST':
        print('Vou salvar os dados')
        form = GeneroForm(request.POST)
        print(form)
        if form.is_valid():
            form.save(commit=True)
        else:
            print('Error')
        return redirect('/genero')
    genero_list = Genero.objects.order_by('descricao')
    context = {'form': form, 'genero_list': genero_list}
    return render(request, 'genero/genero.html', context)


def genero_update(request, id):
    g_update = get_object_or_404(Genero, pk=id)
    gen_update = GeneroForm(instance=g_update)
    context = {'gen_update': gen_update, 'g_update': g_update}
    if request.method == 'POST':
        # g_update = gen_update = genero update
        gen_update = GeneroForm(request.POST, instance=g_update)
        if gen_update.is_valid():
            g_update = gen_update.save(commit=False)
            g_update.save()
            return redirect('/genero')
    else:
        gen_update = GeneroForm(request.POST, instance=g_update)
    return render(request, 'genero/genero_upd.html', context)


def delete(request, id):
    genero = get_object_or_404(Genero, id=id)
    genero.delete()
    return redirect("/genero")

