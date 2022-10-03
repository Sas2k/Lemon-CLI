from Lemon.components import Component

class Footer(Component):
    name = "Footer"

    def item(props: dict):
        _subitems = []

        # user defines order of subitems
        for key in props.keys():
            if key == "footerAuthor":
                _subitems.append(f"Author: {props['footerAuthor']}" if "footerAuthor" in props else "")
            elif key == "footerEmail":
                _subitems.append(f"<a href='mailto:{props['footerEmail']}'>{props['footerEmail']}</a>")
            elif key == "footerCopyright":
                _subitems.append(f"&copy; {props['footerCopyright']}")

        return f"""
        <footer style="background-color: {props["backgroundColor"]}">
            <p>
                {_subitems.join(" | " or props["footerDelimiter"])}
            </p>
        </footer>
        """