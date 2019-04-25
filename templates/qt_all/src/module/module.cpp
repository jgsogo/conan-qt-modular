
#include "{{module.name}}/{{module.name}}.h"

#include <iostream>

{% for it in module.depends -%}
#include "{{it}}/{{it}}.h"
{% endfor %}

void {{module.name}}(const std::string& prefix) {
    std::cout << prefix << "{{module.name}}\n";
    {% for it in depends -%}
    {{it}}(prefix + "\t");
    {% endfor %}
}
