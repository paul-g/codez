import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

MAX_PROBLEM_NAME = 20
MAX_LANG_ID = 10
MAX_TESTCASE_RESULT = 10
MAX_FILE_PATH = 100
MAX_TUTORIAL_DESC = 100

class Problem(models.Model):
    """A problem statement."""
    name               = models.CharField(max_length=MAX_PROBLEM_NAME)
    problem_statement  = models.CharField(max_length=MAX_FILE_PATH) #filename
    input_description  = models.CharField(max_length=2000)
    output_description = models.CharField(max_length=2000)
    solution           = models.CharField(max_length=MAX_FILE_PATH)

    def __unicode__(self):
        return self.name

    def sample_cases(self):
        return TestCase.objects.filter(problem=self, sample=True)

class Tutorial(models.Model):
    """A tutorial groups an ordered list of problem statements. It may
    have one or more other tutorials as pre-requisites."""
    title = models.CharField(max_length=MAX_TUTORIAL_DESC)
    description = models.CharField(max_length=MAX_TUTORIAL_DESC)

    def __str__(self):
        return self.title

class UserTutorial(models.Model):
    """Mapping from users to completed tutorials."""
    user = models.ForeignKey(User)
    tutorial = models.ForeignKey(Tutorial)
    complete = models.BooleanField()

class TutorialProblem(models.Model):
    """Foreign key relation for tutorial and problems."""
    problem = models.ForeignKey(Problem)
    tutorial = models.ForeignKey(Tutorial)

class TutorialDependencies(models.Model):
    """Relation for tutorial dependencies."""
    tutorial = models.ForeignKey(Tutorial)
    tutorial_dep = models.ForeignKey(Tutorial, related_name='tutorial_test')

    def __str__(self):
        return str(self.tutorial) + " depends on " + str(self.tutorial_dep)

class TestCase(models.Model):
    problem     = models.ForeignKey(Problem)
    input_data  = models.CharField(max_length=MAX_FILE_PATH)
    output_data = models.CharField(max_length=MAX_FILE_PATH)
    sample      = models.BooleanField()

class Submission(models.Model):
    problem         = models.ForeignKey(Problem)
    source_code     = models.CharField(max_length=MAX_FILE_PATH)
    author          = models.ForeignKey(User)
    language        = models.CharField(max_length=MAX_LANG_ID)
    submittedAt     = models.DateTimeField()
    evaluated       = models.BooleanField()
    compiler_output = models.CharField(max_length=MAX_FILE_PATH)
    overall_result  = models.CharField(max_length=MAX_TESTCASE_RESULT)

    def __unicode__(self):
        out = "Submission(" + str(self.problem) + ", "
        out += str(self.author) + ", "  + self.language + ", "
        out += str(self.submittedAt) + ")\n"
        out += "-------Source-----\n"
        out += self.source_code + "\n"
        out += "-----End Source---"
        return out

    @classmethod
    def create(cls, problem, source_code, author, language):
        return cls(
            problem=problem,
            source_code=source_code,
            author=author,
            language=language,
            submittedAt=timezone.now(),
            evaluated=False,
            compiler_output = "",
            overall_result  = "")

class TestRun(models.Model):
    submission = models.ForeignKey(Submission)
    result     = models.CharField(max_length=MAX_TESTCASE_RESULT)
    time       = models.DateTimeField()

class News(models.Model):
    title  = models.CharField(max_length=200)
    text   = models.CharField(max_length=2000)
    pub_date = models.DateTimeField('date published')

    @classmethod
    def create(cls, title, text):
        return cls(title=title, text=text, pub_date=timezone.now())

    def __unicode__(self):
        return self.text
