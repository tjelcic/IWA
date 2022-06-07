from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseNotAllowed, HttpResponse
from .models import Ticket, Projection
from .forms import *
from . import models
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Count

# Create your views here.

@login_required
def projection_view(request):
    context={}
    projections = Projection.objects.all()
    context['projections'] = projections
    return render(request, "projection_view.html", context)

@login_required
def buy_ticket(request, projection_id):
    projection = Projection.objects.get(pk=projection_id)
    bought_card = Ticket.objects.filter(projection=projection_id).values_list('seat_number', flat=True)
    context = {
        "projection": projection,
        "bought_card": bought_card
    }

    if request.method == 'POST':
        seat_number = request.POST['seat_number']
        Ticket.objects.create(projection=projection, user=request.user, seat_number=seat_number)
        #return redirect('buy')
    return render(request, "buy_ticket.html", context)

@login_required
@user_passes_test(lambda u: u.is_staff)
def count_user_projection(request):
    tickets = Projection.objects.all()
    return render(request, 'search_projection.html', {'tickets':tickets})   


@login_required
@user_passes_test(lambda u: u.is_staff)
def counter_projection(request, p_id):
   #projections = Projection.objects.all()
   ticket = Ticket.objects.filter(projection_id=p_id).count()
   return render(request, 'count_projections.html', {'ticket':ticket})


@login_required
@user_passes_test(lambda u: u.is_staff) 
def projection_users(request):
    tickets = Ticket.objects.all()
    return render(request, 'projection_users.html', {'tickets':tickets})


@login_required 
def user_tickets(request): 
    tickets = Ticket.objects.filter(user=request.user)
    return render(request, 'my_tickets.html', {'tickets':tickets})


@login_required
@user_passes_test(lambda u: u.is_admin) 
def all_users(request):
    users = Person.objects.all()
    return render(request, 'all_users.html', {'users':users})


@login_required
@user_passes_test(lambda u: u.is_admin) 
def set_superuser(request, person_id): 
    person = Person.objects.get(id=person_id)

    if request.method == 'GET':             
        set_form = SuperUserForm(instance=person)
        return render(request, 'set_superuser.html', {'form':set_form})
    elif request.method == 'POST':
        set_form = SuperUserForm(request.POST, instance=person)
        if set_form.is_valid():
            set_form.save()
            return redirect('home')
        else:
            return HttpResponseNotAllowed()


@login_required
@user_passes_test(lambda u: u.is_staff) 
def insert_projection(request):
    if request.method == 'GET':
        projection_form = ProjectionForm()
        return render(request, 'insert_projection.html', {'form':projection_form})
    elif request.method == 'POST':
        projection_form = ProjectionForm(request.POST)
        if projection_form.is_valid():
            projection_form.save()
            return redirect('home')
        else:
            return HttpResponseNotAllowed()

@login_required
@user_passes_test(lambda u: u.is_staff)
def deletion_confirmation(request, projection_id):
    if request.method == 'GET':
        return render(request, 'confirm_deletion.html', {"data":projection_id})
    return HttpResponseNotAllowed()

@login_required
@user_passes_test(lambda u: u.is_staff)
def delete_projection(request, projection_id):
    proj_by_id = Projection.objects.get(id=projection_id)
    if 'yes' in request.POST:
        proj_by_id.delete()
        return HttpResponse('Successfully deleted!')
    return redirect('home')
    
@login_required
@user_passes_test(lambda u: u.is_staff)
def all_projections(request):
    projections = Projection.objects.all()
    return render(request, 'all_projections.html', {'data':projections})

@login_required
@user_passes_test(lambda u: u.is_staff)
def all_projections_update(request):
    projections = Projection.objects.all()
    return render(request, 'all_projections_update.html', {'data':projections})

@login_required
@user_passes_test(lambda u: u.is_staff)
def update_projection(request, projection_id):           
    proj_by_id = Projection.objects.get(id=projection_id)
    
    if request.method == 'GET':
        data_to_update = ProjectionForm(instance=proj_by_id)
        return render(request, 'update_projection.html', {'form': data_to_update})
    elif request.method == 'POST':
        print(request.POST)
        data_to_update = ProjectionForm(request.POST, instance=proj_by_id)
        if data_to_update.is_valid():
            data_to_update.save()
            return redirect('home')
    else:
        return HttpResponse("Something went wrong!")

def home_view(request): 
    projection = Projection.objects.all()
    return render(request, 'home.html', {'projection':projection})

@login_required
@user_passes_test(lambda u: u.is_staff)
def staff_view(request):
    return render(request,'staff.html')

@login_required
@user_passes_test(lambda u: u.is_admin) 
def admin_view(request):
    return render(request,'admin_view.html')


def register(request): 
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            account = form.save()
            #email = form.cleaned_data.get('email')
            #raw_password = form.cleaned_data.get('password1')
            login(request, account)
            return redirect('home')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form

    return render(request, 'registration.html', context)


def logout_view(request): 
    logout(request)
    return redirect('login')

