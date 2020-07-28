from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Topic
from .forms import TopicForm

def index(request):
    """Home for Learning Log"""
    return render(request, 'learning_logs/index.html')

# Create your views here.

def topics(request,):
    """ Show topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    "show topic and it's entries"
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, "entries": entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """ add a new topic"""
    if request.method != 'POST':
        #no data submitted, create a blank form
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)
