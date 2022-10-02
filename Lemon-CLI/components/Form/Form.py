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