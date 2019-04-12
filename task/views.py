from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .forms import *
from django.core import serializers
from django.http import JsonResponse
from django.http.response import HttpResponseForbidden
from django.db.models import Q


class UserListView(generic.ListView):  # List of Users
    model = User
    template_name = 'list_of_users.html'
    paginate_by = 3
    # def get(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     data = serializers.serialize("json", queryset)
    #     return JsonResponse(data, status=200, safe=False) #get  Json

    def get_queryset(self):  # Search users
        query = self.request.GET.get('q')
        if query:
            return User.objects.filter(Q(username__icontains=query) | Q(email__icontains=query))
        else:
            return User.objects.all()

    def get_context_data(self, **kwargs):  # for query paginator
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context


class GroupListView(generic.ListView):
    model = Group
    template_name = 'list_of_groups.html'
    paginate_by = 3

    def get_queryset(self):  # Search groups
        query = self.request.GET.get('q')
        if query:
            return Group.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        else:
            return Group.objects.all()

    def get_context_data(self, **kwargs):  # for paginator
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context
    # def get(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     data = serializers.serialize("json", queryset)
    #     print(JsonResponse(list(data), status=200, safe=False))
    #     return JsonResponse(list(data), status=200, safe=False)


class UserCreate(generic.CreateView):
    model = User
    template_name = 'manipulate/user_form.html'
    fields = '__all__'
    success_url = reverse_lazy('user_list')


class UserEdit(generic.UpdateView):
    model = User
    form_class = UserModelEditForm
    template_name = 'manipulate/user_form.html'
    success_url = reverse_lazy('user_list')


class UserDelete(generic.DeleteView):
    model = User
    template_name = 'manipulate/user_confirm_delete.html'
    success_url = reverse_lazy('user_list')


class GroupCreate(generic.CreateView):
    model = Group
    fields = '__all__'
    template_name = 'manipulate/group_form.html'
    success_url = reverse_lazy('group_list')


class GroupEdit(generic.UpdateView):
    model = Group
    template_name = 'manipulate/group_form.html'
    fields = '__all__'
    success_url = reverse_lazy('group_list')


class GroupDelete(generic.DeleteView):
    model = Group
    template_name = 'manipulate/group_confirm_delete.html'
    success_url = reverse_lazy('group_list')

    def delete(self, request, *args, **kwargs):
        try:
            return super(GroupDelete, self).delete(
                request, *args, **kwargs
            )
        except models.ProtectedError as e:
            # Return the appropriate response
            return HttpResponseForbidden(
                "This group is tied to 1 or more users"
            )
