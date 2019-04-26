from conans import ConanFile

class Qt(ConanFile):
    name = "qt"
    version = "{{version}}"

    # settings = "os", "arch", "compiler", "build_type"

    options = {
        {% for module in modules -%}
        "{{module}}": [True, False],
        {% endfor -%}
    }
    default_options = {
        {% for module in modules -%}
            {% if module != "qtbase" -%}
            "{{module}}": False,
            {% else -%}
            "{{module}}": True,
            {% endif -%}
        {% endfor -%}
    }

    def requirements(self):
        {% for module in modules -%}
        if self.options.{{module}}:
            self.requires("{{module}}/{{version}}@{{user}}/{{channel}}")
        {% endfor %}

    def package_id(self):
        self.info.header_only()
