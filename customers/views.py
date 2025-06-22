from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Customer
from .forms import CustomerForms
from django.urls import reverse
from django.db.models import Q


# Create your views here.

class CustomerListView(ListView):
    model = Customer
    context_object_name = 'customer_list'
    template_name = 'customer/customer_list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Força a paginação aparecer sempre
        context['is_paginated'] = True

        return context

    
    def get_queryset(self):
        name = self.request.GET.get('name')

        if name:
            object_list = self.model.objects.filter(
                Q(first_name__icontains=name) | Q(last_name__icontains=name))
        
        else:
            object_list = self.model.objects.all()
            
        return object_list


class CustomerCreateView(CreateView):
    template_name = 'customer/customer.html'
    form_class = CustomerForms

    def form_valid(self, form):
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('customer:customer-list')
    

class CustomerUpdateView(UpdateView):
    template_name = 'customer/customer.html'
    form_class = CustomerForms

    def form_valid(self, form):
        return super().form_valid(form)
    
    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Customer, id=id) 

    def get_success_url(self):
        return reverse('customer:customer-list')
    

class CustomerDeleteView(DeleteView):
    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Customer, id=id)
    
    def get_success_url(self):
        return reverse('customer:customer-list')
    
