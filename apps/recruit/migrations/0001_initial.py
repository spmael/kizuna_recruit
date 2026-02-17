from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CV",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("full_name", models.CharField(max_length=80)),
                ("phone_number", models.CharField(max_length=24)),
                ("email", models.EmailField(blank=True, max_length=254)),
                ("city", models.CharField(max_length=60)),
                ("address_line", models.CharField(blank=True, max_length=120)),
                ("photo", models.ImageField(upload_to="cv_photos/")),
                (
                    "availability",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("immediate", "Immédiate"),
                            ("2_weeks", "Dans 2 semaines"),
                            ("1_month", "Dans 1 mois"),
                            ("discuss", "À discuter"),
                        ],
                        max_length=20,
                    ),
                ),
                ("target_job_title", models.CharField(blank=True, max_length=60)),
                ("target_sector", models.CharField(blank=True, max_length=40)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={"ordering": ["-created_at"]},
        ),
        migrations.CreateModel(
            name="Education",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "level",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("primary", "Primaire"),
                            ("middle", "Collège (BEPC)"),
                            ("high", "Lycée (Probatoire / BAC)"),
                            ("university", "Université"),
                            ("vocational", "Formation professionnelle"),
                            ("other", "Autre"),
                        ],
                        max_length=20,
                    ),
                ),
                ("start_year", models.PositiveIntegerField(blank=True, null=True)),
                ("end_year", models.PositiveIntegerField(blank=True, null=True)),
                ("is_current", models.BooleanField(default=False)),
                (
                    "cv",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="educations", to="recruit.cv"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="WorkExperience",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("employer_name", models.CharField(blank=True, max_length=80)),
                ("city", models.CharField(blank=True, max_length=60)),
                ("start_month", models.PositiveSmallIntegerField(blank=True, null=True)),
                ("start_year", models.PositiveIntegerField(blank=True, null=True)),
                ("end_month", models.PositiveSmallIntegerField(blank=True, null=True)),
                ("end_year", models.PositiveIntegerField(blank=True, null=True)),
                ("is_current", models.BooleanField(default=False)),
                (
                    "cv",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="work_experiences", to="recruit.cv"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Skill",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=60)),
                (
                    "cv",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="skills", to="recruit.cv"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CVTranslation",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "language",
                    models.CharField(
                        choices=[("fr", "Français"), ("en", "English")],
                        default="fr",
                        max_length=2,
                    ),
                ),
                ("headline", models.CharField(blank=True, max_length=80)),
                ("summary", models.TextField(blank=True, max_length=400)),
                (
                    "cv",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="translations", to="recruit.cv"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EducationTranslation",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("language", models.CharField(choices=[("fr", "Français"), ("en", "English")], max_length=2)),
                ("school_name", models.CharField(max_length=100)),
                ("field_of_study", models.CharField(blank=True, max_length=80)),
                (
                    "education",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="translations", to="recruit.education"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="WorkExperienceTranslation",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("language", models.CharField(choices=[("fr", "Français"), ("en", "English")], max_length=2)),
                ("job_title", models.CharField(max_length=60)),
                ("description", models.TextField(blank=True, max_length=300)),
                (
                    "work_experience",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="translations",
                        to="recruit.workexperience",
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="cvtranslation",
            constraint=models.UniqueConstraint(fields=("cv", "language"), name="uniq_cv_language"),
        ),
        migrations.AddConstraint(
            model_name="educationtranslation",
            constraint=models.UniqueConstraint(fields=("education", "language"), name="uniq_education_language"),
        ),
        migrations.AddConstraint(
            model_name="workexperiencetranslation",
            constraint=models.UniqueConstraint(
                fields=("work_experience", "language"),
                name="uniq_work_experience_language",
            ),
        ),
    ]
