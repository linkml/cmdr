## Add your own custom Makefile targets here

RUN = poetry run

examples/transformations/include/%.yaml: src/data/examples/%.yaml
	$(RUN) linkml-tr map-data  $< \
		--schema src/cmdr/schema/cmdr.yaml \
		--source-type Container \
		--transformer-specification src/transformations/cmdr_to_include/cmdr_to_include.yaml \
		--output $@

# to be replaced with a iterative rule
test_transform: examples/transformations/include/Container-material-entities.yaml