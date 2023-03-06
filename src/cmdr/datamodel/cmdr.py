# Auto generated from cmdr.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-03-06T15:50:57
# Schema: cmdr
#
# id: https://w3id.org/linkml/cmdr
# description: Core Model for Data Research (Tentative)
# license: MIT

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
OBI = CurieNamespace('OBI', 'http://purl.obolibrary.org/obo/OBI_')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
TEMP = CurieNamespace('TEMP', 'https://example.org/TEMP/')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
CMDR = CurieNamespace('cmdr', 'https://w3id.org/linkml/cmdr/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = CMDR


# Types

# Class references
class MaterialEntityId(URIorCURIE):
    pass


class ProcessId(URIorCURIE):
    pass


class MaterialProcessingId(ProcessId):
    pass


class SpecimenCollectionProcessId(ProcessId):
    pass


@dataclass
class Container(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TEMP.Container
    class_class_curie: ClassVar[str] = "TEMP:Container"
    class_name: ClassVar[str] = "Container"
    class_model_uri: ClassVar[URIRef] = CMDR.Container

    processes: Optional[Union[List[Union[str, ProcessId]], Dict[Union[str, ProcessId], Union[dict, "Process"]]]] = empty_dict()
    materials: Optional[Union[Dict[Union[str, MaterialEntityId], Union[dict, "MaterialEntity"]], List[Union[dict, "MaterialEntity"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="processes", slot_type=Process, key_name="id", keyed=True)

        self._normalize_inlined_as_dict(slot_name="materials", slot_type=MaterialEntity, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class MaterialEntity(YAMLRoot):
    """
    Physical entity that is an input our output of a process
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TEMP.MaterialEntity
    class_class_curie: ClassVar[str] = "TEMP:MaterialEntity"
    class_name: ClassVar[str] = "MaterialEntity"
    class_model_uri: ClassVar[URIRef] = CMDR.MaterialEntity

    id: Union[str, MaterialEntityId] = None
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MaterialEntityId):
            self.id = MaterialEntityId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass
class Process(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TEMP.Process
    class_class_curie: ClassVar[str] = "TEMP:Process"
    class_name: ClassVar[str] = "Process"
    class_model_uri: ClassVar[URIRef] = CMDR.Process

    id: Union[str, ProcessId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProcessId):
            self.id = ProcessId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class MaterialProcessing(Process):
    """
    A planned process which results in physical changes in a specified input material
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0000094"]
    class_class_curie: ClassVar[str] = "OBI:0000094"
    class_name: ClassVar[str] = "MaterialProcessing"
    class_model_uri: ClassVar[URIRef] = CMDR.MaterialProcessing

    id: Union[str, MaterialProcessingId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MaterialProcessingId):
            self.id = MaterialProcessingId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class SpecimenCollectionProcess(Process):
    """
    A planned process with the objective of collecting a specimen
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0000659"]
    class_class_curie: ClassVar[str] = "OBI:0000659"
    class_name: ClassVar[str] = "SpecimenCollectionProcess"
    class_model_uri: ClassVar[URIRef] = CMDR.SpecimenCollectionProcess

    id: Union[str, SpecimenCollectionProcessId] = None
    has_input: Optional[Union[Union[str, MaterialEntityId], List[Union[str, MaterialEntityId]]]] = empty_list()
    has_output: Optional[Union[Union[str, MaterialEntityId], List[Union[str, MaterialEntityId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SpecimenCollectionProcessId):
            self.id = SpecimenCollectionProcessId(self.id)

        if not isinstance(self.has_input, list):
            self.has_input = [self.has_input] if self.has_input is not None else []
        self.has_input = [v if isinstance(v, MaterialEntityId) else MaterialEntityId(v) for v in self.has_input]

        if not isinstance(self.has_output, list):
            self.has_output = [self.has_output] if self.has_output is not None else []
        self.has_output = [v if isinstance(v, MaterialEntityId) else MaterialEntityId(v) for v in self.has_output]

        super().__post_init__(**kwargs)


class Subject(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TEMP.Subject
    class_class_curie: ClassVar[str] = "TEMP:Subject"
    class_name: ClassVar[str] = "Subject"
    class_model_uri: ClassVar[URIRef] = CMDR.Subject


# Enumerations


# Slots
class slots:
    pass

slots.has_input = Slot(uri=TEMP.has_input, name="has_input", curie=TEMP.curie('has_input'),
                   model_uri=CMDR.has_input, domain=None, range=Optional[str])

slots.has_output = Slot(uri=TEMP.has_output, name="has_output", curie=TEMP.curie('has_output'),
                   model_uri=CMDR.has_output, domain=None, range=Optional[str])

slots.id = Slot(uri=TEMP.id, name="id", curie=TEMP.curie('id'),
                   model_uri=CMDR.id, domain=None, range=Optional[str])

slots.materials = Slot(uri=TEMP.materials, name="materials", curie=TEMP.curie('materials'),
                   model_uri=CMDR.materials, domain=None, range=Optional[str])

slots.name = Slot(uri=TEMP.name, name="name", curie=TEMP.curie('name'),
                   model_uri=CMDR.name, domain=None, range=Optional[str])

slots.processes = Slot(uri=TEMP.processes, name="processes", curie=TEMP.curie('processes'),
                   model_uri=CMDR.processes, domain=None, range=Optional[str])

slots.Container_materials = Slot(uri=TEMP.materials, name="Container_materials", curie=TEMP.curie('materials'),
                   model_uri=CMDR.Container_materials, domain=Container, range=Optional[Union[Dict[Union[str, MaterialEntityId], Union[dict, "MaterialEntity"]], List[Union[dict, "MaterialEntity"]]]])

slots.Container_processes = Slot(uri=TEMP.processes, name="Container_processes", curie=TEMP.curie('processes'),
                   model_uri=CMDR.Container_processes, domain=Container, range=Optional[Union[List[Union[str, ProcessId]], Dict[Union[str, ProcessId], Union[dict, "Process"]]]])

slots.MaterialEntity_id = Slot(uri=TEMP.id, name="MaterialEntity_id", curie=TEMP.curie('id'),
                   model_uri=CMDR.MaterialEntity_id, domain=MaterialEntity, range=Union[str, MaterialEntityId])

slots.Process_id = Slot(uri=TEMP.id, name="Process_id", curie=TEMP.curie('id'),
                   model_uri=CMDR.Process_id, domain=Process, range=Union[str, ProcessId])

slots.SpecimenCollectionProcess_has_input = Slot(uri=TEMP.has_input, name="SpecimenCollectionProcess_has_input", curie=TEMP.curie('has_input'),
                   model_uri=CMDR.SpecimenCollectionProcess_has_input, domain=SpecimenCollectionProcess, range=Optional[Union[Union[str, MaterialEntityId], List[Union[str, MaterialEntityId]]]])

slots.SpecimenCollectionProcess_has_output = Slot(uri=TEMP.has_output, name="SpecimenCollectionProcess_has_output", curie=TEMP.curie('has_output'),
                   model_uri=CMDR.SpecimenCollectionProcess_has_output, domain=SpecimenCollectionProcess, range=Optional[Union[Union[str, MaterialEntityId], List[Union[str, MaterialEntityId]]]])