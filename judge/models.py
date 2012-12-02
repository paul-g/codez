import datetime
from django.db import models
from django.contrib.auth.models import User 

MAX_PROBLEM_NAME = 20
MAX_LANG_ID = 10
MAX_TESTCASE_RESULT = 10
MAX_FILE_PATH = 100

class Problem(models.Model):
    name              = models.CharField(max_length=MAX_PROBLEM_NAME)
    problem_statement = models.CharField(max_length=MAX_FILE_PATH) #filename
    solution          = models.CharField(max_length=MAX_FILE_PATH)

class TestCase(models.Model):
    problem         = models.ForeignKey(Problem)
    input_filename  = models.CharField(max_length=MAX_FILE_PATH)
    output_filename = models.CharField(max_length=MAX_FILE_PATH)

class Submission(models.Model):
    problem         = models.ForeignKey(Problem)
    source_code     = models.CharField(max_length=MAX_FILE_PATH)
    author          = models.ForeignKey(User)
    language        = models.CharField(max_length=MAX_LANG_ID)
    submittedAt     = models.DateTimeField()
    evaluated       = models.BooleanField()
    compiler_output = models.CharField(max_length=MAX_FILE_PATH) 
    overall_result  = models.CharField(max_length=MAX_TESTCASE_RESULT)

class TestRun(models.Model):
    submission = models.ForeignKey(Submission)
    result     = models.CharField(max_length=MAX_TESTCASE_RESULT)
    time       = models.DateTimeField()

class News(models.Model):
    title  = models.CharField(max_length=200)
    text   = models.CharField(max_length=2000)
#   author = 
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.text
