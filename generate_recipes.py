import configparser
import os
from jinja2 import Template
import textwrap
from collections import namedtuple

module_type = namedtuple("module", ["name", "depends"])

me = os.path.dirname(__file__)

def render(template, output_filename, **kwargs):
    with open(template, 'r') as f:
        t = Template(f.read())
    content = t.render(**kwargs)

    with open(output_filename, "w") as f:
        f.write(content)


def generate_qt(modules, version, user, channel, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)    

    # Basic data
    data = {"modules": [module.name for module in modules],
            "version": version,
            "user": user,
            "channel": channel
            }

    # conanfile
    output_filename = os.path.join(output_dir, "conanfile.py")
    template = os.path.join(me, "templates", "qt_recipe.tmp.py")
    render(template, output_filename, **data)
    return "qt", output_filename


def generate_qt_module(module, version, user, channel, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Basic data
    data = {"module": module,
            "version": version,
            "user": user,
            "channel": channel
            }

    # conanfile
    output_filename = os.path.join(output_dir, "conanfile.py")
    template = os.path.join(me, "templates", "module_recipe.tmp.py")
    render(template, output_filename, **data)
    return module.name, output_filename
    

def generate_qt_all(modules, version, user, channel, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Basic data
    data = {"modules": [module.name for module in modules],
            "version": version,
            "user": user,
            "channel": channel
            }
    # conanfile
    conanfile_filename = os.path.join(output_dir, "conanfile.py")
    template = os.path.join(me, "templates", "qt_all", "conanfile.py")
    render(template, conanfile_filename, **data)

    # CMakeLists.txt
    output_filename = os.path.join(output_dir, "CMakeLists.txt")
    template = os.path.join(me, "templates", "qt_all", "CMakeLists.txt")
    render(template, output_filename, **data)

    # src/CMakeLists.txt
    project_folder = os.path.join(output_dir, "src")
    if not os.path.exists(project_folder):
        os.makedirs(project_folder)
    output_filename = os.path.join(project_folder, "CMakeLists.txt")
    template = os.path.join(me, "templates", "qt_all", "src", "CMakeLists.txt")
    render(template, output_filename, **data)

    # Iterate each module
    for module in modules:
        data.update({"module": module})

        # Create folder
        module_folder = os.path.join(output_dir, "src", module.name)
        if not os.path.exists(module_folder):
            os.makedirs(module_folder)

        # CMakeLists.txt
        output_filename = os.path.join(module_folder, "CMakeLists.txt")
        template = os.path.join(me, "templates", "qt_all", "src", "module", "CMakeLists.txt")
        render(template, output_filename, **data)

        # header file
        output_filename = os.path.join(module_folder, "{}.h".format(module.name))
        template = os.path.join(me, "templates", "qt_all", "src", "module", "module.h")
        render(template, output_filename, **data)
        
        # source file
        output_filename = os.path.join(module_folder, "{}.cpp".format(module.name))
        template = os.path.join(me, "templates", "qt_all", "src", "module", "module.cpp")
        render(template, output_filename, **data)
    return "qt_all", conanfile_filename


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
    modules_raw = _getsubmodules(qtmodules)
    modules = []
    for it, data in modules_raw.items():
        modules.append(module_type(it, data["depends"]))

    conanfiles = []
    output_path = os.path.join(me, "output")
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    version = "0.1"
    user = "issue"
    channel = "testing"

    print("Generate qt_all")
    id, r = generate_qt_all(modules, version, user, channel, os.path.join(output_path, "qt_all"))
    conanfiles.append((id, r))

    for it in modules:
        print("Generate {}".format(it.name))
        id, r = generate_qt_module(it, version, user, channel, os.path.join(output_path, it.name))
        conanfiles.append((id, r))

    print("Generate qt")
    id, r = generate_qt(modules, version, user, channel, os.path.join(output_path, "qt"))
    conanfiles.append((id, r))

    # Create jobs to run in Conan for all these recipes
    conan_export = os.path.join(me, "jobs.sh")
    with open(conan_export, "w") as f:
        for id, r in conanfiles:
            f.write("conan remove {}/{}@{}/{} -f\n".format(id, version, user, channel))
            f.write("conan create {} {}/{}\n".format(r, user, channel))


if __name__ == "__main__":
    main()