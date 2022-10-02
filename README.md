<p align="center">
 <h1 style="text-align: center;">Lemon-CLI 🍋📀</a>
</p>

<h3 align="center">Lemon-CLI</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/Sas2k/Lemon-CLI.svg)](https://github.com/Sas2k/Lemon-CLI/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/Sas2k/Lemon.svg)](https://github.com/Sas2k/Lemon-CLI/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> Component Generator for <a href="https://github.com/Sas2k/Lemon">Lemon 🍋</a>
    <br> 
</p>

## 📝 Table of Contents

- [📝 Table of Contents](#-table-of-contents)
- [🧐 About <a name = "about"></a>](#-about-)
- [🏁 Getting Started <a name = "getting_started"></a>](#-getting-started-)
  - [Installing](#installing)
- [🎈 Usage <a name="usage"></a>](#-usage-)
  - [Components Implemented](#components-implemented)
- [⛏️ Built Using <a name = "built_using"></a>](#️-built-using-)
- [✍️ Authors <a name = "authors"></a>](#️-authors-)
- [🎉 Acknowledgements <a name = "acknowledgement"></a>](#-acknowledgements-)

## 🧐 About <a name = "about"></a>

This project is to make your lives easier with lemon, this is also my **Hacktoberfest** project.

Lemon 🍋 : https://github.com/Sas2k/Lemon

## 🏁 Getting Started <a name = "getting_started"></a>

### Installing

**With PIP**
```
pip install Lemon-CLI
```

## 🎈 Usage <a name="usage"></a>

generating a component

```
Lemon-CLI component <component>
```

will create

```
components/
  - <component>.py
```

### Components Implemented

> For the ones, that aren't implemented open an issue and describe it or implement it yourself and PR this.
> (Change the README and related stuff accordingly, Make sure to describe the PR changes well.)

- #### App
  
  A base app in Lemon.

```python
from Lemon.components import Component
from Lemon.Server import server

Root = Component("App")
App = server.Server(None)

class Index(Component):
    name = "Index"
    def item(props: dict):
        return "<h1>Hello World!</h1>"

Root.add(Index)

@App.route("/")
def index(request, response):
    response.text = Root.render("<Index/>")

App.run()
```

- #### Form
  
  A basic form.

```python
from Lemon.components import Component
from Lemon.ui.forms import FormControl

class Form(Component):
    name = "Form"

    def item(props: dict):
        return """
        <form>
            <div class="form-group">
                <Input type="text" id="TextInput" text="Text Input:" placeholder="placeholder"/>
                <Select id="SelectInput" text="Select Input:" options="Option 1,Option 2,Option 3"//>
                <Checkbox id="CheckboxInput" text="Checkbox Input"/>
                <Submit id="SubmitButton" text="Submit"/>
            </div>
        </form>
        """

components = [Form, FormControl().components]
```

- #### EmailPassword

  A form asking for Email and Password.

```python
from Lemon.components import Component
from Lemon.ui.forms import FormControl

class EmailPassword(Component):
    name = "EmailPassword"

    def item(props: dict):
        return """
        <div class="form-group">
            <form>
                <Input type="email" id="EmailInput" text="Email Input:" placeholder="placeholder"/>
                <Input type="password" id="PasswordInput" text="Password Input:" placeholder="placeholder"/>
                <Submit id="SubmitButton" text="Submit"/>
            </form>
        </div>
        """

components = [EmailPassword, FormControl().components]
```

- #### Page Heading

  A simple page heading.

```python
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
```

## ⛏️ Built Using <a name = "built_using"></a>

- [Python](https://www.python.org)
## ✍️ Authors <a name = "authors"></a>

- [@Sas2k](https://github.com/Sas2k) - Idea & Initial work

See also the list of [contributors](https://github.com/Sas2k/Lemon-CLI/contributors) who participated in this project.

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Hacktoberfest
