# CMDR

CMDR (pronunciation: “com-mo-dore” or sometimes “com-man-der”), the Core Model for Data Research, is a LinkML schema/data model for the collection of biological sample data, and its analysis.

The purpose of this schema is to act as a *base* schema for other LinkML schemas/data models to bootstrap for their specific use case.

## Project Setup

1. Clone *cmdr* project repository

```
$ git clone https://github.com/linkml/cmdr.git
```

2. Create virtual environment and install project dependencies
```
$ make install
```

3. Create downstream schema artifacts, run unit tests, and also validate examples/instance data against schema
```
$ make test
```

4. LinkML transformer mapping between source and target schemas on a class
```
$ make test_transform
```

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
