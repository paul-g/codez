from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from judge.models import News, Problem, Submission
from judge import views

urlpatterns = patterns('',
	url(r'^$',
		ListView.as_view(
			queryset=News.objects.order_by('-pub_date')[:5],
			context_object_name='latest_news_list',
			template_name='judge/index.html',
		)
	),
        url(r'^news/(?P<pk>\d+)',    DetailView.as_view(model=News)),
        url(r'^problem/(?P<pk>\d+)', views.problem_detail, name='problem'),
        url(r'^problems$',
		ListView.as_view(
			queryset=Problem.objects.all(),
			context_object_name='problems_list',
			template_name='judge/problems.html',
		)
	),
        url(r'^submission/(?P<pk>\d+)', DetailView.as_view(model=Submission)),
        url(r'^submissions$',
		ListView.as_view(
			queryset=Submission.objects.all().order_by('-submittedAt'),
			context_object_name='submissions_list',
			template_name='judge/submissions.html',
		)
	),
        url(r'^training/', views.training_view),
)
