from django.contrib import admin
from .models import (
    Languages,
    Institutions,
    Category,
    Certifications,
    Prerequisites,
    Topic,
    Course,
    CareerOpportunity
)

admin.site.register(Languages)
admin.site.register(Institutions)
admin.site.register(Certifications)
admin.site.register(Category)
admin.site.register(Prerequisites)
admin.site.register(Topic)
admin.site.register(Course)
@admin.register(CareerOpportunity)
class CareerOpportunityAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'posted_at', 'is_active')
    list_filter = ('is_active', 'company', 'location')
    search_fields = ('title', 'company', 'description')