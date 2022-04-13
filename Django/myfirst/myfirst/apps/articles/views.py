from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse

from .models import Article
from .models import Comment

def index(request):
    latest_articles_list = Article.objects.order_by('-pub_date')[:5]
    return render(request, 'articles/list.html', {'latest_articles_list': latest_articles_list})

def detail(request, article_id):
    try:
        a = Article.objects.get( id = article_id )
    except:
        raise Http404("Статья не найдена")

    latest_comment_list = a.comment_set.order_by('-id')[:10]

    return render(request, 'articles/detail.html', {'article': a, 'latest_comment_list': latest_comment_list})

def leave_comment(request, article_id):

    try:
        a = Article.objects.get( id = article_id )
    except:
        raise Http404("Статья не найдена")
    a.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'])

    return HttpResponseRedirect( reverse('articles:detail', args = (a.id,)) )




'''def comment_delete(request, article_id):

    selected_comment = get_object_or_404(Comment, id=id)
    selected_comment.delete()

    return HttpResponseRedirect( reverse('articles:detail', args = (a.id,)) )'''




def comment_delete(request, id):
    comment = Comment.objects.get( id = id )
    if comment.user == request.user:
        comment.is_removed = True
        comment.save()

    return HttpResponseRedirect( reverse('articles:detail', args = (a.id,)) )
