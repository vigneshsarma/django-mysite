from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime,time

def current_time(request):
  now =time.ctime()
#  t=get_template('current_time.html')
#  resp=t.render(Context({'current_time':now}))
  return render_to_response('current_time.html',{'current_time':now})

def hours_ahead(request,offset):
  try:
    hours_offset = int(offset)
  except ValueError:
    raise Http404()
  next_time=datetime.datetime.now()+datetime.timedelta(hours=hours_offset)
#  assert False
#  html="<html><body>In %s hour(s), it will be %s.</body></html>"%(offset,dt)
  return render_to_response('hours_ahead.html',locals())

def hello(request):
  return HttpResponse("Helo World")

