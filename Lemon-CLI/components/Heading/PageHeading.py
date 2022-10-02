from Lemon.components import Component

class PageHeading(Component):
    name = "PageHeading"

    def item(props: dict):
        return f"""
        <div style="background-color: {props["color"]}" id="top" class="container-fluid">
            <h1 class="page-heading">{props["text"]}</h1>
        </div>
        """

components = [PageHeading]