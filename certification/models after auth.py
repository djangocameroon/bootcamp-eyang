from django.db import models
from django.contrib.auth.models import User




class Certifications(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)
    level_of_difficulty = models.CharField(
        max_length=20,
        default="0",
        choices=(
            ("0", "easy"),
            ("1", "medium"),
            ("2", "hard"),
            ("3", "very hard"),
            ("4", "impossible"),
        ),
    )
    category = models.ManyToManyField("Category")
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    duration_of_validity = models.CharField(null=True, max_length=50)
    institution = models.ForeignKey("Institutions", on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to="media/certification")
    exam_site = models.CharField(max_length=100)
    prerequisites = models.ManyToManyField("Prerequisites")
    link = models.URLField()
    discounts = models.CharField(null=True, max_length=50)
    languages = models.ManyToManyField("Languages")
    class Meta:
        db_table = "certifications"
        verbose_name_plural = "Certifications"
        unique_together = ("name", "institution")

    def __str__(self):
        return f"{self.name} - {self.institution.name}"


class Institutions(models.Model):
    name = models.CharField(max_length=50)
    accepted_zones = models.CharField(max_length=250)
    about = models.TextField(null=True)

    class Meta:
        db_table = "institutions"
        verbose_name_plural = "Institutions"

    def __str__(self):
        return self.name


class Prerequisites(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        db_table = "prerequisites"
        verbose_name_plural = "Prerequisites"

    def __str__(self):
        return self.title


class Languages(models.Model):
    code = models.CharField(max_length=6)
    name = models.CharField(max_length=20)

    class Meta:
        db_table = "languages"
        verbose_name_plural = "Languages"
        unique_together = ("code", "name")

    def __str__(self):
        return f"{self.name} - {self.code}"


class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = "category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Global_user(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name= models.CharField(max_length=20, null=True)
    last_name= models.CharField(max_length=20, null=True)
    contact= models.CharField(max_length=13, null=True)
    address = models.CharField(max_length=50, null=True)
    status= models.CharField(
        max_length=20,
        default="0",
        choices=(
            ("0", "College student"),
            ("1", "University student"),
            ("2", "Teacher"),
            ("3", "Employer"),
            ("4", "Entrepreneur"),
        ),
    )
    career = models.CharField(max_length=20)
    def __str__(self):
        return self.user.username
