from django.http import HttpResponse
from django.shortcuts import render
from.models import Place,Team

# Create your views here.
#def home(request):
  # return HttpResponse("HOME")
def demo(request):
   obj=Place.objects.all()
   tm=Team.objects.all()
   return  render(request,"index.html", {'result':obj,'rest':tm})
#def contact(request):
#    return HttpResponse("hello am contact")
#def detail(request):
 #   return render(request,"detail.html")
# thanx(request):
#    return HttpResponse("thank you everyone")



