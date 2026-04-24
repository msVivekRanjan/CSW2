from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from .models import Article, Comment
from .forms import ArticleShareForm, CommentForm


def article_list(request):
    articles_list = Article.objects.all()
    paginator = Paginator(articles_list, 5)
    page_number = request.GET.get('page')
    try:
        articles = paginator.page(page_number)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    return render(request, 'articleApp/article_list.html', {'articles': articles})


def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    comments = article.comments.all()
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            form = CommentForm()
    return render(request, 'articleApp/article_detail.html', {'article': article, 'comments': comments, 'form': form})


def article_share(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    sent = False
    if request.method == 'POST':
        form = ArticleShareForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = f"{cd['name']} recommends you read {article.title}"
            message = f"Read {article.title}\n\n{cd['name']} says: {cd['comments']}"
            send_mail(subject, message, cd['email'], [cd['to']])
            sent = True
    else:
        form = ArticleShareForm()
    return render(request, 'articleApp/article_share.html', {'article': article, 'form': form, 'sent': sent})