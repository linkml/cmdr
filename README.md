# cmdr

Core Model for Data Research (Tentative)

_Currently most influenced by the Include schema, https://github.com/include-dcc/include_linkml_

recommended:

- `make test`
- `make test_transform`

## Website

* [https://linkml.github.io/cmdr](https://linkml.github.io/cmdr)

## Repository Structure

* [examples/](examples/) - example data
* [project/](project/) - project files (do not edit these)
* [src/](src/) - source files (edit these)
    * [cmdr](src/cmdr)
        * [schema](src/cmdr/schema) -- LinkML schema (edit this)
* [datamodel](src/cmdr/datamodel) -- Generated python datamodel
* [tests](tests/) - python tests

We've added
some [HTML visualizastions of data instances](https://htmlpreview.github.io/?https://github.com/linkml/cmdr/blob/master/examples/Container-material-entities.html)!

## Developer Documentation

<details>
Use the `make` command to generate project artefacts:

- `make all`: make everything
- `make deploy`: deploys site

</details>

## Credits

this project was made with [linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter)
