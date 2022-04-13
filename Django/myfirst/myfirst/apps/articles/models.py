import datetime
from django.db import models

from django.utils import timezone
from django.urls import reverse

class Article(models.Model):
    article_title = models.CharField('название статьи', max_length = 200)
    article_text = models.TextField('текст статьи')
    pub_date = models.DateTimeField('дата публикации')
    '''cat = models.ForeignKey('Comment', on_delete = models.CASCADE, null = True)'''
    def __atr__(self):
        return self.article_title

    def was_published_recenyly(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days = 7))



    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    author_name = models.CharField('имя автора', max_length = 50)
    comment_text = models.TextField('текст коментария', max_length = 200)

    def __atr__(self):
        return self.author_name

def get_absolute_url(self):
    return revers('comment', kwargs={'comment_id': self.pk})

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'
