"""
Lemon-CLI: __main__.py
by Sasen Perera 2022
"""

import argparse
import os

file_directory = os.path.dirname(__file__)

components_list = {
    'app': open(file_directory + '/components/BaseApp.py', 'r').read(),
    'form': open(file_directory + '/components/Form/Form.py', 'r').read(),
    'email-password-input': open(file_directory + '/components/Form/email.py', 'r').read(),
    'page-heading': open(file_directory + '/components/Heading/PageHeading.py', 'r').read()
}

def main():
    parser = argparse.ArgumentParser(description="Lemon-CLI: __main__.py")
    subparser = parser.add_subparsers()

    parser.add_argument('-v', '--version', action='version', version='1.0.0')

    component = subparser.add_parser("component", help="Create a new component")
    component.add_argument("component", help="Component to generate.")

    args = parser.parse_args()

    if args.component:
        component_name = args.component.lower()
        if component_name in components_list:
            component_code = components_list[component_name]
            
            if os.path.exists("Components"):
                pass
            else:
                os.mkdir("Components")

            with open(f"Components/{component_name}.py", "w+") as file:
                file.write(component_code)
                print(f"Created component: {component_name}")
        else:
            print(f"Component not found: {component_name}")

if __name__ == "__main__":
    main()