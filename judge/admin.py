from judge.models import News
from django.contrib import admin
from judge.models import *


class NewsInline(admin.TabularInline):
        model = News
        extra = 3

class NewsAdmin(admin.ModelAdmin):
        fieldsets = [
                (None, {'fields' : ['question']}),
                ('Date information', {'fields' : ['pub_date'], 'classes' : ['collapse']})
        ]
        inlines = [NewsInline]
        list_display = ('question', 'pub_date', 'was_published_recently')
        list_filter  = ['pub_date']
        search_fields = ['question']
        date_hierarchy = 'pub_date'

admin.site.register(News)
admin.site.register(Submission)
admin.site.register(Problem)
admin.site.register(TestRun)
admin.site.register(TestCase)
admin.site.register(Tutorial)
admin.site.register(UserTutorial)
admin.site.register(TutorialProblem)
admin.site.register(TutorialDependencies)
