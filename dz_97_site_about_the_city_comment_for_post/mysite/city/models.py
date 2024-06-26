from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=100, verbose_name="Назвагиестатьи")
    body = models.TextField(verbose_name="Текст статьи")
    image = models.ImageField(upload_to='city/images/', verbose_name="Фото")
    views = models.IntegerField(verbose_name="Количество просмотров")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, verbose_name="Пост", related_name="comments")
    comment = models.TextField(verbose_name="Комментарий")
    created = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return f"Комментарий от {self.user} к посту {self.post}"
