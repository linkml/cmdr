# Auto generated from cmdr.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-03-06T17:07:59
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
class InvestigationId(URIorCURIE):
    pass


class MaterialEntityId(URIorCURIE):
    pass


class ParticipationId(URIorCURIE):
    pass


class ProcessId(URIorCURIE):
    pass


class MaterialProcessingId(ProcessId):
    pass


class SpecimenCollectionProcessId(ProcessId):
    pass


class SubjectId(URIorCURIE):
    pass


@dataclass
class Container(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TEMP.Container
    class_class_curie: ClassVar[str] = "TEMP:Container"
    class_name: ClassVar[str] = "Container"
    class_model_uri: ClassVar[URIRef] = CMDR.Container

    materials: Optional[Union[Dict[Union[str, MaterialEntityId], Union[dict, "MaterialEntity"]], List[Union[dict, "MaterialEntity"]]]] = empty_dict()
    participations: Optional[Union[Dict[Union[str, ParticipationId], Union[dict, "Participation"]], List[Union[dict, "Participation"]]]] = empty_dict()
    processes: Optional[Union[List[Union[str, ProcessId]], Dict[Union[str, ProcessId], Union[dict, "Process"]]]] = empty_dict()
    investigations: Optional[Union[Dict[Union[str, InvestigationId], Union[dict, "Investigation"]], List[Union[dict, "Investigation"]]]] = empty_dict()
    subjects: Optional[Union[Dict[Union[str, SubjectId], Union[dict, "Subject"]], List[Union[dict, "Subject"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="materials", slot_type=MaterialEntity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="participations", slot_type=Participation, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="processes", slot_type=Process, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="investigations", slot_type=Investigation, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="subjects", slot_type=Subject, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class Investigation(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TEMP.Investigation
    class_class_curie: ClassVar[str] = "TEMP:Investigation"
    class_name: ClassVar[str] = "Investigation"
    class_model_uri: ClassVar[URIRef] = CMDR.Investigation

    id: Union[str, InvestigationId] = None
    name: Optional[str] = None
    part_of: Optional[Union[str, InvestigationId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InvestigationId):
            self.id = InvestigationId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.part_of is not None and not isinstance(self.part_of, InvestigationId):
            self.part_of = InvestigationId(self.part_of)

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
    used_in: Optional[Union[Union[str, InvestigationId], List[Union[str, InvestigationId]]]] = empty_list()
    source: Optional[Union[str, SubjectId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MaterialEntityId):
            self.id = MaterialEntityId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.used_in, list):
            self.used_in = [self.used_in] if self.used_in is not None else []
        self.used_in = [v if isinstance(v, InvestigationId) else InvestigationId(v) for v in self.used_in]

        if self.source is not None and not isinstance(self.source, SubjectId):
            self.source = SubjectId(self.source)

        super().__post_init__(**kwargs)


@dataclass
class Participation(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TEMP.Participation
    class_class_curie: ClassVar[str] = "TEMP:Participation"
    class_name: ClassVar[str] = "Participation"
    class_model_uri: ClassVar[URIRef] = CMDR.Participation

    id: Union[str, ParticipationId] = None
    includes: Optional[Union[str, SubjectId]] = None
    name: Optional[str] = None
    involved_in: Optional[Union[Union[str, InvestigationId], List[Union[str, InvestigationId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ParticipationId):
            self.id = ParticipationId(self.id)

        if self.includes is not None and not isinstance(self.includes, SubjectId):
            self.includes = SubjectId(self.includes)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.involved_in, list):
            self.involved_in = [self.involved_in] if self.involved_in is not None else []
        self.involved_in = [v if isinstance(v, InvestigationId) else InvestigationId(v) for v in self.involved_in]

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
    has_input: Optional[Union[Union[str, MaterialEntityId], List[Union[str, MaterialEntityId]]]] = empty_list()
    has_output: Optional[Union[Union[str, MaterialEntityId], List[Union[str, MaterialEntityId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MaterialProcessingId):
            self.id = MaterialProcessingId(self.id)

        if not isinstance(self.has_input, list):
            self.has_input = [self.has_input] if self.has_input is not None else []
        self.has_input = [v if isinstance(v, MaterialEntityId) else MaterialEntityId(v) for v in self.has_input]

        if not isinstance(self.has_output, list):
            self.has_output = [self.has_output] if self.has_output is not None else []
        self.has_output = [v if isinstance(v, MaterialEntityId) else MaterialEntityId(v) for v in self.has_output]

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


@dataclass
class Subject(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TEMP.Subject
    class_class_curie: ClassVar[str] = "TEMP:Subject"
    class_name: ClassVar[str] = "Subject"
    class_model_uri: ClassVar[URIRef] = CMDR.Subject

    id: Union[str, SubjectId] = None
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SubjectId):
            self.id = SubjectId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


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

slots.includes = Slot(uri=TEMP.includes, name="includes", curie=TEMP.curie('includes'),
                   model_uri=CMDR.includes, domain=None, range=Optional[str])

slots.investigations = Slot(uri=TEMP.investigations, name="investigations", curie=TEMP.curie('investigations'),
                   model_uri=CMDR.investigations, domain=None, range=Optional[str])

slots.involved_in = Slot(uri=TEMP.involved_in, name="involved_in", curie=TEMP.curie('involved_in'),
                   model_uri=CMDR.involved_in, domain=None, range=Optional[str])

slots.materials = Slot(uri=TEMP.materials, name="materials", curie=TEMP.curie('materials'),
                   model_uri=CMDR.materials, domain=None, range=Optional[str])

slots.name = Slot(uri=TEMP.name, name="name", curie=TEMP.curie('name'),
                   model_uri=CMDR.name, domain=None, range=Optional[str])

slots.part_of = Slot(uri=TEMP.part_of, name="part_of", curie=TEMP.curie('part_of'),
                   model_uri=CMDR.part_of, domain=None, range=Optional[str])

slots.participations = Slot(uri=TEMP.participations, name="participations", curie=TEMP.curie('participations'),
                   model_uri=CMDR.participations, domain=None, range=Optional[str])

slots.processes = Slot(uri=TEMP.processes, name="processes", curie=TEMP.curie('processes'),
                   model_uri=CMDR.processes, domain=None, range=Optional[str])

slots.source = Slot(uri=TEMP.source, name="source", curie=TEMP.curie('source'),
                   model_uri=CMDR.source, domain=None, range=Optional[str])

slots.subjects = Slot(uri=TEMP.subjects, name="subjects", curie=TEMP.curie('subjects'),
                   model_uri=CMDR.subjects, domain=None, range=Optional[str])

slots.used_in = Slot(uri=TEMP.used_in, name="used_in", curie=TEMP.curie('used_in'),
                   model_uri=CMDR.used_in, domain=None, range=Optional[str])

slots.Container_investigations = Slot(uri=TEMP.investigations, name="Container_investigations", curie=TEMP.curie('investigations'),
                   model_uri=CMDR.Container_investigations, domain=Container, range=Optional[Union[Dict[Union[str, InvestigationId], Union[dict, "Investigation"]], List[Union[dict, "Investigation"]]]])

slots.Container_materials = Slot(uri=TEMP.materials, name="Container_materials", curie=TEMP.curie('materials'),
                   model_uri=CMDR.Container_materials, domain=Container, range=Optional[Union[Dict[Union[str, MaterialEntityId], Union[dict, "MaterialEntity"]], List[Union[dict, "MaterialEntity"]]]])

slots.Container_participations = Slot(uri=TEMP.participations, name="Container_participations", curie=TEMP.curie('participations'),
                   model_uri=CMDR.Container_participations, domain=Container, range=Optional[Union[Dict[Union[str, ParticipationId], Union[dict, "Participation"]], List[Union[dict, "Participation"]]]])

slots.Container_processes = Slot(uri=TEMP.processes, name="Container_processes", curie=TEMP.curie('processes'),
                   model_uri=CMDR.Container_processes, domain=Container, range=Optional[Union[List[Union[str, ProcessId]], Dict[Union[str, ProcessId], Union[dict, "Process"]]]])

slots.Container_subjects = Slot(uri=TEMP.subjects, name="Container_subjects", curie=TEMP.curie('subjects'),
                   model_uri=CMDR.Container_subjects, domain=Container, range=Optional[Union[Dict[Union[str, SubjectId], Union[dict, "Subject"]], List[Union[dict, "Subject"]]]])

slots.Investigation_id = Slot(uri=TEMP.id, name="Investigation_id", curie=TEMP.curie('id'),
                   model_uri=CMDR.Investigation_id, domain=Investigation, range=Union[str, InvestigationId])

slots.Investigation_part_of = Slot(uri=TEMP.part_of, name="Investigation_part_of", curie=TEMP.curie('part_of'),
                   model_uri=CMDR.Investigation_part_of, domain=Investigation, range=Optional[Union[str, InvestigationId]])

slots.MaterialEntity_id = Slot(uri=TEMP.id, name="MaterialEntity_id", curie=TEMP.curie('id'),
                   model_uri=CMDR.MaterialEntity_id, domain=MaterialEntity, range=Union[str, MaterialEntityId])

slots.MaterialEntity_source = Slot(uri=TEMP.source, name="MaterialEntity_source", curie=TEMP.curie('source'),
                   model_uri=CMDR.MaterialEntity_source, domain=MaterialEntity, range=Optional[Union[str, SubjectId]])

slots.MaterialEntity_used_in = Slot(uri=TEMP.used_in, name="MaterialEntity_used_in", curie=TEMP.curie('used_in'),
                   model_uri=CMDR.MaterialEntity_used_in, domain=MaterialEntity, range=Optional[Union[Union[str, InvestigationId], List[Union[str, InvestigationId]]]])

slots.MaterialProcessing_has_input = Slot(uri=TEMP.has_input, name="MaterialProcessing_has_input", curie=TEMP.curie('has_input'),
                   model_uri=CMDR.MaterialProcessing_has_input, domain=MaterialProcessing, range=Optional[Union[Union[str, MaterialEntityId], List[Union[str, MaterialEntityId]]]])

slots.MaterialProcessing_has_output = Slot(uri=TEMP.has_output, name="MaterialProcessing_has_output", curie=TEMP.curie('has_output'),
                   model_uri=CMDR.MaterialProcessing_has_output, domain=MaterialProcessing, range=Optional[Union[Union[str, MaterialEntityId], List[Union[str, MaterialEntityId]]]])

slots.Participation_id = Slot(uri=TEMP.id, name="Participation_id", curie=TEMP.curie('id'),
                   model_uri=CMDR.Participation_id, domain=Participation, range=Union[str, ParticipationId])

slots.Participation_includes = Slot(uri=TEMP.includes, name="Participation_includes", curie=TEMP.curie('includes'),
                   model_uri=CMDR.Participation_includes, domain=Participation, range=Optional[Union[str, SubjectId]])

slots.Participation_involved_in = Slot(uri=TEMP.involved_in, name="Participation_involved_in", curie=TEMP.curie('involved_in'),
                   model_uri=CMDR.Participation_involved_in, domain=Participation, range=Optional[Union[Union[str, InvestigationId], List[Union[str, InvestigationId]]]])

slots.Process_id = Slot(uri=TEMP.id, name="Process_id", curie=TEMP.curie('id'),
                   model_uri=CMDR.Process_id, domain=Process, range=Union[str, ProcessId])

slots.SpecimenCollectionProcess_has_input = Slot(uri=TEMP.has_input, name="SpecimenCollectionProcess_has_input", curie=TEMP.curie('has_input'),
                   model_uri=CMDR.SpecimenCollectionProcess_has_input, domain=SpecimenCollectionProcess, range=Optional[Union[Union[str, MaterialEntityId], List[Union[str, MaterialEntityId]]]])

slots.SpecimenCollectionProcess_has_output = Slot(uri=TEMP.has_output, name="SpecimenCollectionProcess_has_output", curie=TEMP.curie('has_output'),
                   model_uri=CMDR.SpecimenCollectionProcess_has_output, domain=SpecimenCollectionProcess, range=Optional[Union[Union[str, MaterialEntityId], List[Union[str, MaterialEntityId]]]])

slots.Subject_id = Slot(uri=TEMP.id, name="Subject_id", curie=TEMP.curie('id'),
                   model_uri=CMDR.Subject_id, domain=Subject, range=Union[str, SubjectId])