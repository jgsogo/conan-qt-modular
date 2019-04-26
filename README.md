# conan-qt-modular

Conan packages for a modular library (Qt). This is just a POC

## Usage

Generate all the recipes from templates and create them (use `jobs.sh` script):

```
python generate_recipes.py
./jobs.sh
```

Move to `examples` directory and work with Conan as usual:
 * `consume_intermediate` contains an example using the intermediate Qt libraries:
 
    ```txt
    [requires]
    qtwebglplugin/0.1@issue/testing
    qtsensors/0.1@issue/testing

    [generators]
    cmake

    ```
 * `consume_qt` contains an example where the libraries are consumed using the single `qt` package:
 
    ```txt
    [requires]
    qt/0.1@issue/testing

    [options]
    qt:qtwebglplugin=True
    qt:qtsensors=True

    [generators]
    cmake

    ```
