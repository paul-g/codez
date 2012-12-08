from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from judge.models import News
from judge.models import Problem

urlpatterns = patterns('',
	url(r'^$',
		ListView.as_view(
			queryset=News.objects.order_by('-pub_date')[:5],
			context_object_name='latest_news_list',
			template_name='judge/index.html',
		)
	),
        url(r'^news/(?P<pk>\d+)',    DetailView.as_view(model=News)),
        url(r'^problem/(?P<pk>\d+)', DetailView.as_view(model=Problem))
)
