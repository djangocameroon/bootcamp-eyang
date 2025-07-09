from django.db import models

from django.db import models


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
            ("3", "extreme"),
            ("4", "impossible"),
        ),
    )
    category = models.ManyToManyField("Category")
    topic = models.ManyToManyField("Topic")
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    duration_of_validity = models.CharField(null=True, max_length=50)
    institution = models.ForeignKey("Institutions", on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to="certification")
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

    def get_difficulty_badge_type(self):
        """Retourne le type de badge DaisyUI en fonction de la difficulté"""
        types = {
            '0': 'Easy',
            '1': 'Medium',
            '2': 'Hard',
            '3': 'Very_hard',
            '4': 'Impossible',
        }
        return types.get(self.level_of_difficulty, 'Impossible')

    def get_short_description(self):
        """Retourne une description tronquée pour les cartes"""
        return self.description[:100] + '...' if self.description else "Aucune description disponible"

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('certification_detail', kwargs={'pk': self.pk})

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


class Topic(models.Model):
    name = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = "topic"
        verbose_name_plural = "Topics"

    def __str__(self):
        return self.name

class Course(models.Model):
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
    topic = models.ManyToManyField("Topic")
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    duration_of_validity = models.CharField(null=True, max_length=50)
    institution = models.ForeignKey("Institutions", on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to="certification")
    exam_site = models.CharField(max_length=100)
    prerequisites = models.ManyToManyField("Prerequisites")
    link = models.URLField()
    discounts = models.CharField(null=True, max_length=50)
    languages = models.ManyToManyField("Languages")
    duration=models.IntegerField(null=True)
    class Meta:
        db_table = "courses"
        verbose_name_plural = "Courses"
        unique_together = ("name", "institution")

    def __str__(self):
        return f"{self.name} - {self.institution.name}"
