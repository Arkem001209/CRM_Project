from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead

def leads_list(request):
    leads = Lead.objects.all()
    context = {
        "leads" : leads
    }
    return render(request, "leads/lead_list.html", context)

def lead_detail(request, pk):
    print(pk)
    lead = Lead.objects.get(id=pk)
    print(lead)
    return HttpResponse("Here is the detail view")