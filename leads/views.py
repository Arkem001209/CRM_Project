from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead, Agent
from .forms import LeadForm


def leads_list(request):
    leads = Lead.objects.all()
    context = {
        "leads" : leads
    }
    return render(request, "leads/lead_list.html", context)

def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead" : lead
    }
    return render(request, "leads/lead_detail.html", context)

def lead_create(request):
    form = LeadForm()
    if request.method=="POST":
        print("receiving post request")
        form = LeadForm(request.POST)
        if form.is_valid():
            print("The form is Valid!")
            print(form.cleaned_data)
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            agent = Agent.objects.first()
            Lead.objects.create(
                first_name=first_name,
                last_name=last_name,
                age=age,
                agent=agent
            )
            print("lead has been created")
    context = {
        "form" : form
    }
    return render(request, "leads/lead_create.html", context)