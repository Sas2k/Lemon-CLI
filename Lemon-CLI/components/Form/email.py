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