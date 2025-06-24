from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView, FormView, DetailView
from django.shortcuts import render
from .forms import (
    AddCertificationForm, CategoryForm,
    InstitutionsForm, PrerequisitesForm, LanguagesForm
)
from .models import Certifications

from datetime import datetime




def certif(request):

    return render(request, 'certif.html')

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["certifications"] = Certifications.objects.all()
        return context


class AddCertificationView(FormView):
    template_name = 'add_certification.html'
    form_class = AddCertificationForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_form'] = CategoryForm()
        context['institutions_form'] = InstitutionsForm()
        context['prerequisites_form'] = PrerequisitesForm()
        context['languages_form'] = LanguagesForm()
        context['csrf_token'] = get_token(self.request)
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        """Override post to handle the form submission manually"""
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect(self.success_url)

        return self.render_to_response(self.get_context_data(form=form))


class AddRelatedView(View):
    """Handle AJAX requests for adding related models."""

    @method_decorator(require_POST)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, model_name, *args, **kwargs):
        if model_name == 'category':
            form = CategoryForm(request.POST)
        elif model_name == 'institution':
            form = InstitutionsForm(request.POST)
        elif model_name == 'prerequisites':
            form = PrerequisitesForm(request.POST)
        elif model_name == 'languages':
            form = LanguagesForm(request.POST)
        else:
            return JsonResponse({'error': 'Invalid model type'}, status=400)

        if form.is_valid():
            form.save()
            return redirect(reverse('add_certification'))
        else:
            return JsonResponse({'error': form.errors}, status=400)


class CertificationDetailView(DetailView):
    """Display details for a specific certification."""
    model = Certifications
    template_name = 'certification_detail.html'
    context_object_name = 'certification'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add any additional context data here if needed
        return context

