from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from todo.models import List, Task


def index(request):
    latest_list = List.objects.all().order_by('-list_name')[:5]
    context = {'latest_list': latest_list}
    return render(request, 'todo/index.html', context)

def detail(request, list_id):
    question = get_object_or_404(List, pk=list_id)
    return render(request, 'todo/detail.html', {'question': question})

def add(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, list_id):
	p = get_object_or_404(List, pk=list_id)
	try:
		selected_task = p.task_set.get(pk=request.POST['task'])
	except (KeyError, Task.DoesNotExist):
		return render(request, 'todo/detail.html',{
			'question': p,
			'error_message': "You didn't choose a task to delete",
		})
	else:
		selected_task.delete()
		return HttpResponseRedirect(reverse('todo:detail', args=(p.id,)))

