from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Lead

# Create your views here.
def index(request):
    return render(request, 'index.html')

def submit_lead(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')

        # Optional: Save lead data to the database
        Lead.objects.create(name=name, email=email)

        # Redirect to a thank-you page with the download link
        return redirect('thank_you')
    return HttpResponse("Invalid request", status=400)

def thank_you(request):
    return render(request, 'thank_you.html')
