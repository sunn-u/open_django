# Coding by SunWoo(tjsntjsn20@gmail.com)

from typing import List, Dict


def HTMLTemplate(article: str, topics: List, id=None):
    # only for localhost:port/read/{id} page.
    if id != None:
        contextUI = f"""
        <li>
            <form action="/delete/" method="post">
                <input type="hidden" name="id" value={id}>
                <input type="submit" value="delete">
            </form>
        </li>
        <li>
            <form action="/update/{id}/" method="post">
                <input type="submit" value="update">
            </form>
        </li>
        """
    else:
        contextUI = ""
    
    # make list of topics.
    defaultList = ""
    for key, value in enumerate(topics):
        defaultList += f"""
        <li>
            <a href="/read/{key}/">{value["title"]}</a>
        </li>
        """

    # common page.
    return f"""
    <html>
    <body>
        <h1><a href="/">MyFirstDjango</a></h1>
        <ol>
            {defaultList}
        </ol>
        {article}
        <ul>
            <li>
                <form action="/create/" method="post">
                    <input type="submit" value="create">
                </form>
            </li>
            {contextUI}
        </ul>
    </body>
    </html>
    """
