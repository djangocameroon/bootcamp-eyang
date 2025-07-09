from django.contrib import admin
from .models import (
    Languages,
    Institutions,
    Category,
    Certifications,
    Prerequisites,
    Topic,
    Course,
)

admin.site.register(Languages)
admin.site.register(Institutions)
admin.site.register(Certifications)
admin.site.register(Category)
admin.site.register(Prerequisites)
admin.site.register(Topic)
admin.site.register(Course)
