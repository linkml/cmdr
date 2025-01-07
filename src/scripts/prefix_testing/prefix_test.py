from linkml.generators.yamlgen import YAMLGenerator
from linkml.generators.linkmlgen import LinkmlGenerator
from linkml_runtime.linkml_model import SchemaDefinition
from linkml_runtime.utils.schemaview import SchemaView


def save_schema(schema: SchemaDefinition, output_path: str) -> None:
    # Use YAMLGenerator to generate YAML output
    # lm_gen = YAMLGenerator(schema, format="yaml")
    # yaml_text = lm_gen.serialize()
    #
    # # Write the generated YAML to the specified output file
    # with open(output_path, "w", encoding="utf-8") as f:
    #     f.write(yaml_text)
    # print(f"Schema saved to: {output_path}")

    lm_gen = LinkmlGenerator(output_path)
    linkml_text = lm_gen.serialize()
    with open("remodel.yaml", "w", encoding="utf-8") as f:
        f.write(linkml_text)

def save_linkml_schema(schema: SchemaDefinition, output_path: str) -> None:
    # Create a LinkmlGenerator instance to generate the schema in LinkML YAML format
    sv = SchemaView(schema)
    print(sv.schema.prefixes)

    lml_gen = LinkmlGenerator(schema)
    linkml_text = lml_gen.serialize()

    # Write the generated LinkML YAML to the specified output file
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(linkml_text)
    print(f"LinkML schema saved to: {output_path}")

if __name__ == "__main__":
    output_file = "equipment_schema.yaml"

    schema = SchemaDefinition(
        name="EquipmentSchema",
        description="Schema for equipment data",
        id="equipment_schema",
        default_prefix="equipment_schema"
    )

    schema.default_range = "string"
    schema.prefixes = {
        "equipment_schema": "https://example.org/equipment_schema/",
        "linkml": "https://w3id.org/linkml/",
        "xsd": "http://www.w3.org/2001/XMLSchema#"
    }


    # save_schema(schema, output_file)
    # Call the function to generate and save the LinkML schema

    save_linkml_schema(schema, output_file)


    # sv = SchemaView("cmdr.yaml")
    # schemav = sv.schema
    # print(type(schemav))
    # print(schemav.prefixes)