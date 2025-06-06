from django.shortcuts import render, redirect
from .forms import LeadForm
from .models import Lead
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.urls import reverse

def landing_page(request):
    form = LeadForm()
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()

            send_mail(
                subject="New form submission.",
                message="A new user submitted the form.",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=["wambuguworking@gmail.com"],
            )
            return redirect('success')
    else:
        form = LeadForm

    return render(request, 'leads/landing.html', {'form': form})

def success_page(request):
    return render(request, 'success.html')

def dashboard(request):
    leads = Lead.objects.all().order_by('-created_at')
    return render(request, 'dashboard.html', {'leads': leads})


@csrf_exempt
def mark_followed(request, lead_id):
    lead = Lead.objects.get(id=lead_id)
    lead.is_followed_up = True
    lead.save()
    return HttpResponseRedirect(reverse('admin'))