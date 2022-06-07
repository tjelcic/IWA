from django.shortcuts import render
from django.http import HttpResponse
from .models import Projekcija, Karta
from django.contrib.auth.models import User

# Create your views here.

def create_movies (request):
  # m1 = Projekcija(movie_name = 'Monty Python and the Holy Grail', movie_time = '17:00:00', capacity = 100)
  # m1.save()
  # m2 = Projekcija(movie_name = "Monty Python's Life of Brian", movie_time = '20:00:00', capacity = 50)
  # m2.save()
  # m3 = Projekcija(movie_name = "Monty Python's The Meaning of Life", movie_time = '22:00:00', capacity = 70)
  # m3.save()

  return HttpResponse('<h1>Done!</h1>')

def buy(request):
    m1 = Projekcija.objects.get(pk = 1)
    u1 = User.objects.get(pk = 1)
    n1 = Karta.objects.filter(movie_id = 1).count()

    m2 = Projekcija.objects.get(pk = 2)
    u2 = User.objects.get(pk = 2)
    n2 = Karta.objects.filter(movie_id = 2).count()

    m3 = Projekcija.objects.get(pk = 3)
    u3 = User.objects.get(pk = 3)
    n3 = Karta.objects.filter(movie_id = 3).count()

    if(n1 < m1.capacity):
      ticket = Karta(seat_number = n1 + 1, movie = m1, user = u1)
      ticket.save()
      seats = m1.capacity - 1
      m1.capacity = seats
      m1.save()
    else:
      return HttpResponse("<h1>This projection is at capacity!</h1>")

    if(n2 < m2.capacity):
      ticket = Karta(seat_number = n2 + 1, movie = m2, user = u2)
      ticket.save()
      seats = m2.capacity - 1
      m2.capacity = seats
      m2.save()
    else:
      return HttpResponse("<h1>This projection is at capacity!</h1>")

    if(n3 < m3.capacity):
      ticket = Karta(seat_number = n3 + 1, movie = m3, user = u3)
      ticket.save()
      seats = m3.capacity - 1
      m3.capacity = seats
      m3.save()
    else:
      return HttpResponse("<h1>This projection is at capacity!</h1>")
    
    movies = Projekcija.objects.all()
    return render(request, 'projekcije.html', {'data': movies})

def tickets(request):
  tickets = Karta.objects.filter(user=request.GET["id"])
  return render(request, 'tickets.html', {'data': tickets})
