from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True,verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = 'Категории'


class News(models.Model):
    title = models.CharField(max_length=255,blank=True,null=True,verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    photo = models.ImageField(upload_to='media',verbose_name='Фото')
    date_of_upload = models.DateTimeField(auto_now_add=True,verbose_name="Дата Публикации")
    likes = models.IntegerField(default=0)
    news_category = models.ForeignKey('Category',on_delete=models.CASCADE,related_name='category')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = 'Новости'
