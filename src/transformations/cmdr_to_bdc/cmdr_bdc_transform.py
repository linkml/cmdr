"""Transformation script to convert CMDR schema to BDC schema"""
from linkml_map.datamodel.transformer_model import TransformationSpecification, ClassDerivation, SlotDerivation
from linkml_map.inference.schema_mapper import SchemaMapper
from linkml_runtime.utils.formatutils import camelcase, underscore
from linkml_runtime.dumpers import yaml_dumper
from linkml_runtime.utils.schemaview import SchemaView
from pathlib import Path


REPO_ROOT = Path.cwd().parent.parent.parent
print(REPO_ROOT)


def get_bdc_class_derivations(target_schemaview) -> dict:
    """
    Function to get BDC class definitions

    :param target_schemaview: SchemaView object
    :param subset_classes: List of classes to subset
    :return: Dictionary of class derivations incl slot derivations
    """
    # Example implementation to fetch class definitions
    # This should be replaced with the actual implementation
    class_derivations ={}
    subset_classes = target_schemaview.all_classes()
    for class_name in subset_classes:
        class_derivation = ClassDerivation(populated_from=class_name,
                                           name=camelcase(class_name))
        induced_slots = target_schemaview.class_induced_slots(class_name)
        for slot in induced_slots:
            print(slot.name)
            slot_derivation = SlotDerivation(populated_from=slot.name, name=underscore(slot.name))
            class_derivation.slot_derivations[underscore(slot.name)] = slot_derivation
        class_derivations[camelcase(class_name)] = class_derivation
    return class_derivations


def main():
    """Main function to convert CMDR schema to BDC schema."""
    schema_path = REPO_ROOT / "src" / "cmdr" / "schema" / "cmdr.yaml"  # Use quotes to denote string literals
    bdc_raw = REPO_ROOT / "src" / "cmdr" / "schema" / "bdc.yaml"
    cmdr_sv = SchemaView(schema_path)
    bdc_sv = SchemaView(bdc_raw)
    class_derivations = get_bdc_class_derivations(target_schemaview=bdc_sv)
    ts = TransformationSpecification(class_derivations=class_derivations)
    ts.title = "CMDR to BDC transformation"
    ts.id = "cmdr_to_bdc"

    yaml_dumper.dump(ts, "cmdr_to_bdc_transformation_spec.yaml")

    mapper = SchemaMapper()
    mapper.source_schemaview = cmdr_sv

    target_schema_obj = mapper.derive_schema(
        specification=ts, target_schema_id="cmdr-bdc-schema", target_schema_name="CMDR_BDC_schema"
    )

    # ugly bit of hacking to demonstrate end-to-end functionality
    target_schema_obj.types = cmdr_sv.all_types()

    yaml_dumper.dump(target_schema_obj, "cmdr_bdc_schema.yaml")

if __name__ == "__main__":
    """Entry point for the script."""
    main()
