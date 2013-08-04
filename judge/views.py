import json

from django import forms
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from judge.models import Problem, Submission


def problem_detail(request, pk):
    p = get_object_or_404(Problem, pk=pk)

    if request.method == 'POST':
        submission_status = 'fail'
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            submission_status = 'success'
            language = form.cleaned_data['language']
            handle_submission(request.FILES['file'], p, request.user, language )
    else:
        submission_status = 'none'
        form = UploadFileForm()

    context = {'problem':p, 'upload_form': form, 'submission_status': submission_status}

    return render(request, 'judge/problem_detail.html', context)

LANGUAGES = (('C++', 'C++'),
             ('C', 'C'),
             ('Java', 'Java'))


class UploadFileForm(forms.Form):
    language = forms.ChoiceField(choices=LANGUAGES)
    file  = forms.FileField()


def handle_submission(source_file, problem, user, language):
    source = ""
    for chunk in source_file.chunks():
        source += chunk
    s = Submission.create(problem, source, user, language)
    print s
    s.save()


def training_view(request):
    """Render training view page."""
    nodes = [
        ('Haskell Primer', []),
        ('Java Primer', []),
        ('Data Structures', ['Haskell Primer']),
        ('Graph Algorithms', ['Haskell Primer', 'Java Primer']),
        ('Advanced Graph Algorithms', ['Graph Algorithms']),
        ('Hardcore Graph Algorithms', ['Advanced Graph Algorithms']),
    ]
    js_nodes = json.dumps(nodes)
    context = {'training_data' : js_nodes }
    return render(request, 'judge/training.html', context)
