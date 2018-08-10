from django.db import models

SELECT_LABEL=(
    ('OBJ1', '選択肢1'),
    ('OBJ2', '選択肢2'),
    ('OBJ3', '選択肢3'),
        )

# Create your models here.
class Article(models.Model):
    subject = models.CharField(
            "タイトル",
            max_length=90,
    )
    data_str = models.CharField(
            "データ(文字型)",
            max_length=10000,
            null=True,
            )
    data_date = models.DateField(
            "データ(日時)",
            null=True,
            )
    data_datetime = models.DateTimeField(
            "データ(日時)",
            null=True,
            )
    data_bool = models.BooleanField(
            "データ(チェックボックス)",
            default=False,
            )
    data_choice = models.CharField(
            "データ(セレクトボックス)",
            max_length=10,
            choices=SELECT_LABEL,
            blank=True,
            null=True
            )

