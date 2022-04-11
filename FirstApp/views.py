# Coding by SunWoo(tjsntjsn20@gmail.com)

from django.http import HttpResponse
from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt

from .template import HTMLTemplate


topics = [
    dict(title='routing', body='Routing is ...'),
    dict(title='view', body='View is ...'),
    dict(title='model', body='Model is ...')
]

def index(request):
    global topics

    article = f"""
    <h2>Welcome!</h2>
    Hello, Django.
    """
    return HttpResponse(HTMLTemplate(article=article, topics=topics))


def read(request, id: str):
    global topics

    topic = topics[int(id)]
    article = f"""
    <h2>{topic["title"]}</h2>
    {topic["body"]}
    """
    return HttpResponse(HTMLTemplate(article=article, topics=topics, id=id))


@csrf_exempt
def create(request):
    global topics
    article = f"""
    <form action="/create/" method="post">
        <p><input type="text" name="title" placeholder="title"></p>
        <p><textarea name="body" placeholder="body"></textarea></p>
        <p><input type="submit"></p> 
    </form>
    """
    if request.POST == {}:
        return HttpResponse(HTMLTemplate(article=article, topics=topics))
    else:
        title = request.POST["title"]
        body = request.POST["body"]
        topics.append(dict(title=title, body=body))
        url = f"/read/{len(topics)-1}"
        return redirect(url)


@csrf_exempt
def delete(request):
    global topics
    id = request.POST["id"]
    del topics[int(id)]
    return redirect("/")


@csrf_exempt
def update(request, id):
    global topcis
    topic = topics[int(id)]
    title = topic["title"]
    body = topic["body"]

    article = f"""
    <form action="/update/{id}/" method="post">
        <p><input type="text" name="title" placeholder="title" value={title}></p>
        <p><textarea name="body" placeholder="body">{body}</textarea></p>
        <p><input type="submit"></p> 
    </form>
    """
    if request.POST == {}:
        return HttpResponse(HTMLTemplate(article=article, topics=topics, id=id))
    else:
        title = request.POST["title"]
        body = request.POST["body"]
        topics[int(id)] = dict(title=title, body=body)
        url = f"/read/{id}"
        return redirect(url)
