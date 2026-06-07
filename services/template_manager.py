import json

class TemplateManager:

    TEMPLATE_FILE = "templates/templates.json"

    def load_templates(self):
        try:
            with open(self.TEMPLATE_FILE, "r") as file:
                return json.load(file)
        except:
            return {}

    def get_template(self, name):
        templates = self.load_templates()
        return templates.get(name)

    def personalize(self, template, data):
        for key, value in data.items():
            template = template.replace(
                f"{{{key}}}",
                str(value)
            )
        return template