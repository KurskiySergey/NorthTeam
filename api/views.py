from django.shortcuts import render
from main.models import Candidate
# Create your views here.

def show_candidates(request):
    candidates = Candidate.all()
    context = {
        'candidates': candidates
    }
    return render(request, "api/api_candidates.html", context=context)