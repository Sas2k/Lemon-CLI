from Lemon.components import Component

class Article(Component):
    name = "Article"

    def item(props: dict):
        return f"""
        <article style="background-color: {props["backgroundColor"]}" class="container-fluid">
            <h2 class="article-heading">{props["articleHeading"]}</h2>
            <span class="article-author"><i>Author: {props["articleAuthor"]}</i></span>
            <p class="article-body">{props["articleBody"]}</p>
        </article>
        """

components = [Article]