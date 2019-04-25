import configparser
import os
from jinja2 import Template
import textwrap


me = os.path.dirname(__file__)

def render(template, output_filename, **kwargs):
    with open(template, 'r') as f:
        t = Template(f.read())
    content = t.render(**kwargs)

    with open(output_filename, "w") as f:
        f.write(content)


def render_recipe(name, version, depends, output_path):
    template = os.path.join(me, "templates", "module_recipe.tmp")
    with open(template, 'r') as f:
        t = Template(f.read())
    content = t.render(libname=name, version=version, depends=depends)

    output_filename = os.path.join(output_path, "{}.py".format(name.lower()))
    with open(output_filename, "w") as f:
        f.write(content)
    
    return output_filename


def generate_qt_all(modules, version, user, channel, output_dir):
    # Basic data
    data = {"modules": [module.name for module in modules],
            "version": version,
            "user": user,
            "channel": channel
            }
    # conanfile
    output_filename = os.path.join(output_dir, "conanfile.py")
    template = os.path.join(me, "templates", "qt_all", "conanfile.py")
    render(template, output_filename, **data)

    # CMakeLists.txt
    output_filename = os.path.join(output_dir, "CMakeLists.py")
    template = os.path.join(me, "templates", "qt_all", "CMakeLists.py")
    render(template, output_filename, **data)

    # src/CMakeLists.txt
    output_filename = os.path.join(output_dir, "src", "CMakeLists.py")
    template = os.path.join(me, "templates", "qt_all", "src", "CMakeLists.py")
    render(template, output_filename, **data)

    # Iterate each module
    for module in modules:
        data.update({"module": module})

        # Create folder
        module_folder = os.path.join(output_dir, "src", module.name)
        if not os.path.exists(module_folder):
            os.makedirs(module_folder)

        # CMakeLists.txt
        output_filename = os.path.join(module_folder, "CMakeLists.py")
        template = os.path.join(me, "templates", "qt_all", "src", "module", "CMakeLists.py")
        render(template, output_filename, **data)

        # header file
        output_filename = os.path.join(module_folder, "{}.h".format(module.name))
        template = os.path.join(me, "templates", "qt_all", "src", "module", "module.h")
        render(template, output_filename, **data)
        
        # source file
        output_filename = os.path.join(module_folder, "{}.cpp".format(module.name))
        template = os.path.join(me, "templates", "qt_all", "src", "module", "module.cpp")
        render(template, output_filename, **data)


def _getsubmodules(filepath):
    config = configparser.ConfigParser()
    config.read(filepath)
    res = {}
    assert config.sections()
    for s in config.sections():
        section = str(s)
        assert section.startswith("submodule ")
        assert section.count('"') == 2
        modulename = section[section.find('"') + 1: section.rfind('"')]
        status = str(config.get(section, "status"))
        if status != "obsolete" and status != "ignore":
            res[modulename] = {"branch": str(config.get(section, "branch")), "status": status,
                                "path": str(config.get(section, "path")), "depends": []}
            if config.has_option(section, "depends"):
                res[modulename]["depends"] = [str(i) for i in config.get(section, "depends").split()]
    return res

def main():
    qtmodules = os.path.join(os.path.dirname(__file__), "qtmodules.conf")
    modules = _getsubmodules(qtmodules)

    conanfiles = []
    output_path = os.path.join(me, "output")
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    for name, data in modules.items():
        print(name)
        conanfile = render_recipe(name, "0.1", depends=data["depends"], output_path=output_path)
        conanfiles.append(conanfile)

    conan_export = os.path.join(me, "jobs.sh")
    with open(conan_export, "w") as f:
        for it in conanfiles:
            f.write("conan export {} issue/testing\n".format(it))

if __name__ == "__main__":
    main()