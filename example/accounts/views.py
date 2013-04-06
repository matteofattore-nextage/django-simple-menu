from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    return render_to_response('index.html',
                              context_instance=RequestContext(request))

@login_required
def profile(request):
    return render_to_response('registration/profile.html',
                              context_instance=RequestContext(request))

def one(request):
    return render_to_response('registration/label.html', {'label':'one'},
                              context_instance=RequestContext(request))
def two(request):
    return render_to_response('registration/label.html', {'label':'two'},
                              context_instance=RequestContext(request))
def three(request):
    return render_to_response('registration/label.html', {'label':'three'},
                              context_instance=RequestContext(request))
def four(request):
    return render_to_response('registration/label.html', {'label':'four'},
                              context_instance=RequestContext(request))