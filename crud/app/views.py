from django.shortcuts import render, redirect
from .models import Person
from .forms import AddForm


def index(request):
    make_men()
    people = Person.objects.all()
    return render(request, 'app/index.html', context={'people': people})


def create(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            age = form.cleaned_data['age']
            gender = form.cleaned_data['gender']

            men, _ = Person.objects.get_or_create(name=name, surname=surname,
                                                  age=age, gender=gender)
            return redirect('home')
        else:
            form = AddForm()
            return render(request, 'app/create.html', context={'form': form})
    else:
        form = AddForm()
        return render(request, 'app/create.html', context={'form': form})


def update(request, id):
    try:
        men = Person.objects.get(id=id)
        if request.method == 'POST':
            men.name = request.POST.get('name')
            men.surname = request.POST.get('surname')
            men.age = request.POST.get('age')
            men.gender = request.POST.get('gender')

            return redirect('home')
        else:
            return render(request, 'app/update.html', context={'men': men})
    except:
        return redirect('create')


def delete(request):
    try:
        men = Person.objects.get(id=id)
        men.delete()

        return redirect('home')
    except:
        return redirect('create')


def make_men():
    p, _ = Person.objects.get_or_create(name='Marry', surname='Christmas',
                                        age=2023,
                                        gender=True)
    p, _ = Person.objects.get_or_create(name='Thomas', surname='Shelby', age=16,
                                        gender=True)
    p, _ = Person.objects.get_or_create(name='Rail', surname='Galimov', age=23,
                                        gender=False)
    p, _ = Person.objects.get_or_create(name='Nu', surname='Pogodi', age=17,
                                        gender=True)
