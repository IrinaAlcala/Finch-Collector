from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

class Finch:
  def __init__(self, name, type, description, age):
    self.name = name
    self.type = type
    self.description = description
    self.age = age
finches = [
  Finch('Tenor', 'house finch', 'great for households', 1),
  Finch('Squeak', 'european finch', 'likes cold weather', 2),
  Finch('Queen', 'purple finch', 'beautiful purple color', 3)
]
# Define the home view
def home(request):
  return HttpResponse('<h1>Hello</h1>')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {'finches': finches })