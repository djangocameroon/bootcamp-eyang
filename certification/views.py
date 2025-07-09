from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView, FormView, DetailView
from django.shortcuts import render,get_object_or_404
from .forms import (
    AddCertificationForm, CategoryForm,
    InstitutionsForm, PrerequisitesForm, LanguagesForm
)
from .models import Certifications

from datetime import datetime

from django.core.paginator import Paginator


def certification_list(request):
    certifications_list = Certifications.objects.all().order_by('name')
    paginator = Paginator(certifications_list, 8)  # 6 certifications par page

    page_number = request.GET.get('page')
    certifications = paginator.get_page(page_number)

    # Préparer les choix de difficulté pour le template
    difficulty_choices = dict(Certifications._meta.get_field('level_of_difficulty').choices)

    return render(request, 'certif.html', {
        'certifications': certifications,
        'difficulty_choices': difficulty_choices
    })


def certification_detail(request, pk):
    certification = get_object_or_404(Certifications, pk=pk)

    # Organiser les données pour le template
    context = {
        'certif': certification,
        'difficulty_levels': dict(Certifications._meta.get_field('level_of_difficulty').choices),
        'topics': certification.topic.all(),
        'categories': certification.category.all(),
        'languages': certification.languages.all(),
        'prerequisites': certification.prerequisites.all()
    }

    return render(request, 'certif_detail.html', context)

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

