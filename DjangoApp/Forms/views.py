from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.template import loader
from .models import Students, Groups, Fakulcies
from django.urls import reverse
from django.views import generic


def HelloWindow(request):
    return render(request, 'Forms/index.html')


class IndexViewGroups(generic.ListView):
    template_name = 'Forms/groups_list.html'
    context_object_name = 'groups_list'

    def get_queryset(self):
        return Groups.objects.order_by('group_num')


class DetailViewGroups(generic.DetailView):
    model = Groups
    template_name = 'Forms/group_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(DetailViewGroups, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['faks_list'] = Fakulcies.objects.all()
        return context


class ResultsViewGroups(generic.DetailView):
    model = Groups
    template_name = 'Forms/group_results.html'


def edit_group(request, group_id):
    group = get_object_or_404(Groups, pk=group_id)
    try:
        selected_num = str(request.POST['group_num'])
        selected_fakulcy = Fakulcies.objects.get(pk=request.POST['fak'])
    except (KeyError, group.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'Forms/group_detail.html', {
            'group': group,
            'error_message': "You didn't typo all of the fields.",
        })
    else:
        group.group_num = selected_num
        group.fakulcy_id = selected_fakulcy
        group.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('Forms:group_results', args=(group.id,)))


def add_group_form(request):
    faks_list = Fakulcies.objects.all()
    return render(request, 'Forms/add_group.html', {"faks_list" : faks_list})


def add_group(request):
    try:
        selected_num = str(request.POST['group_num'])
        selected_fakulcy = Fakulcies.objects.get(pk=request.POST['fak'])
    except (selected_num == 0 or selected_fakulcy == 0):
        # Redisplay the question voting form.
        return render(request, 'Forms/group_detail.html', {
            'error_message': "You didn't typo all of the fields.",
        })
    else:
        group=Groups.objects.create_group(selected_num, selected_fakulcy)
        group.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('Forms:group_results', args=(group.id,)))




class IndexView(generic.ListView):
    template_name = 'Forms/students_list.html'
    context_object_name = 'students_list'

    def get_queryset(self):
        return Students.objects.order_by('name')


class DetailView(generic.DetailView):
    model = Students
    template_name = 'Forms/detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(DetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['groups_list'] = Groups.objects.all()
        return context


class ResultsView(generic.DetailView):
    model = Students
    template_name = 'Forms/results.html'


def edit_student(request, student_id):
    student = get_object_or_404(Students, pk=student_id)
    try:
        selected_name = str(request.POST['student_name'])
        selected_surname = str(request.POST['student_surname'])
        selected_group = Groups.objects.get(pk=request.POST['group'])
    except (KeyError, student.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'Forms/detail.html', {
            'student': student,
            'error_message': "You didn't typo all of the fields.",
        })
    else:
        student.name = selected_name
        student.surname = selected_surname
        student.group = selected_group
        student.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('Forms:results', args=(student.id,)))


def add_student_form(request):
    groups_list = Groups.objects.all()
    return render(request, 'Forms/add_student.html', {"groups_list" : groups_list})


def add_student(request):
    try:
        selected_name = str(request.POST['student_name'])
        selected_surname = str(request.POST['student_surname'])
        selected_group = Groups.objects.get(pk=request.POST['group'])
    except (selected_name == 0 or selected_surname == 0 or selected_group == 0):
        # Redisplay the question voting form.
        return render(request, 'Forms/group_detail.html', {
            'error_message': "You didn't typo all of the fields.",
        })
    else:
        student=Students.objects.create_student(selected_name, selected_surname, selected_group)
        student.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('Forms:results', args=(student.id,)))



class IndexViewFakulcy(generic.ListView):
    template_name = 'Forms/fakulcies_list.html'
    context_object_name = 'fakulcies_list'

    def get_queryset(self):
        return Fakulcies.objects.order_by('fakulcy_name')


class DetailViewFakulcy(generic.DetailView):
    model = Fakulcies
    template_name = 'Forms/fakulcy_detail.html'

class ResultsViewFakulcy(generic.DetailView):
    model = Fakulcies
    template_name = 'Forms/fakulcies_results.html'


def edit_fakulcy(request, fakulcy_id):
    fakulcy = get_object_or_404(Fakulcies, pk=fakulcy_id)
    try:
        selected_name = str(request.POST['fakulcy_name'])
    except (KeyError, fakulcy.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'Forms/fakulcy_detail.html', {
            'fakulcy': fakulcy,
            'error_message': "You didn't typo all of the fields.",
        })
    else:
        fakulcy.name = selected_name
        fakulcy.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('Forms:fakulcy_results', args=(fakulcy.id,)))


def add_fakulcy_form(request):
    faks_list = Fakulcies.objects.all()
    return render(request, 'Forms/add_fakulcy.html')


def add_fakulcy(request):
    try:
        selected_name = str(request.POST['fakulcy_name'])
    except (selected_name == 0):
        # Redisplay the question voting form.
        return render(request, 'Forms/fakulcy_detail.html', {
            'error_message': "You didn't typo all of the fields.",
        })
    else:
        fakulcy=Fakulcies.objects.create_fakulcy(selected_name)
        fakulcy.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('Forms:fakulcy_results', args=(fakulcy.id,)))


def delete_student(request, id):
    try:
        student = Students.objects.get(id=id)
        student.delete()
        return render(request, 'Forms/index.html')
    except Students.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


def delete_group(request, id):
    try:
        group = Groups.objects.get(id=id)
        group.delete()
        return render(request, 'Forms/index.html')
    except Groups.DoesNotExist:
        return HttpResponseNotFound("<h2>Group not found</h2>")


def delete_fakulcy(request, id):
    try:
        fak = Fakulcies.objects.get(id=id)
        fak.delete()
        return render(request, 'Forms/index.html')
    except Fakulcies.DoesNotExist:
        return HttpResponseNotFound("<h2>Fakulcy not found</h2>")