# Auto generated from cmdr.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-03-06T15:00:38
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
from linkml_runtime.linkml_model.types import String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
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



class Condition(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TEMP.Condition
    class_class_curie: ClassVar[str] = "TEMP:Condition"
    class_name: ClassVar[str] = "Condition"
    class_model_uri: ClassVar[URIRef] = CMDR.Condition


@dataclass
class Database(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TEMP.Database
    class_class_curie: ClassVar[str] = "TEMP:Database"
    class_name: ClassVar[str] = "Database"
    class_model_uri: ClassVar[URIRef] = CMDR.Database

    conditions: Optional[Union[Union[dict, Condition], List[Union[dict, Condition]]]] = empty_list()
    diagnoses: Optional[Union[Union[dict, "Diagnosis"], List[Union[dict, "Diagnosis"]]]] = empty_list()
    documents: Optional[Union[Union[dict, "Document"], List[Union[dict, "Document"]]]] = empty_list()
    observations: Optional[Union[Union[dict, "Observation"], List[Union[dict, "Observation"]]]] = empty_list()
    subjects: Optional[Union[Union[dict, "Subject"], List[Union[dict, "Subject"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.conditions, list):
            self.conditions = [self.conditions] if self.conditions is not None else []
        self.conditions = [v if isinstance(v, Condition) else Condition(**as_dict(v)) for v in self.conditions]

        if not isinstance(self.diagnoses, list):
            self.diagnoses = [self.diagnoses] if self.diagnoses is not None else []
        self.diagnoses = [v if isinstance(v, Diagnosis) else Diagnosis(**as_dict(v)) for v in self.diagnoses]

        if not isinstance(self.documents, list):
            self.documents = [self.documents] if self.documents is not None else []
        self.documents = [v if isinstance(v, Document) else Document(**as_dict(v)) for v in self.documents]

        if not isinstance(self.observations, list):
            self.observations = [self.observations] if self.observations is not None else []
        self.observations = [v if isinstance(v, Observation) else Observation(**as_dict(v)) for v in self.observations]

        if not isinstance(self.subjects, list):
            self.subjects = [self.subjects] if self.subjects is not None else []
        self.subjects = [v if isinstance(v, Subject) else Subject(**as_dict(v)) for v in self.subjects]

        super().__post_init__(**kwargs)


@dataclass
class Document(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TEMP.Document
    class_class_curie: ClassVar[str] = "TEMP:Document"
    class_name: ClassVar[str] = "Document"
    class_model_uri: ClassVar[URIRef] = CMDR.Document

    is_about: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.is_about is not None and not isinstance(self.is_about, str):
            self.is_about = str(self.is_about)

        super().__post_init__(**kwargs)


class Event(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TEMP.Event
    class_class_curie: ClassVar[str] = "TEMP:Event"
    class_name: ClassVar[str] = "Event"
    class_model_uri: ClassVar[URIRef] = CMDR.Event


class Information(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TEMP.Information
    class_class_curie: ClassVar[str] = "TEMP:Information"
    class_name: ClassVar[str] = "Information"
    class_model_uri: ClassVar[URIRef] = CMDR.Information


@dataclass
class Diagnosis(Information):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TEMP.Diagnosis
    class_class_curie: ClassVar[str] = "TEMP:Diagnosis"
    class_name: ClassVar[str] = "Diagnosis"
    class_model_uri: ClassVar[URIRef] = CMDR.Diagnosis

    is_about: Optional[Union[dict, Condition]] = None
    source: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.is_about is not None and not isinstance(self.is_about, Condition):
            self.is_about = Condition()

        if self.source is not None and not isinstance(self.source, str):
            self.source = str(self.source)

        super().__post_init__(**kwargs)


class MaterialEntity(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TEMP.MaterialEntity
    class_class_curie: ClassVar[str] = "TEMP:MaterialEntity"
    class_name: ClassVar[str] = "MaterialEntity"
    class_model_uri: ClassVar[URIRef] = CMDR.MaterialEntity


class Measurment(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TEMP.Measurment
    class_class_curie: ClassVar[str] = "TEMP:Measurment"
    class_name: ClassVar[str] = "Measurment"
    class_model_uri: ClassVar[URIRef] = CMDR.Measurment


class Observation(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TEMP.Observation
    class_class_curie: ClassVar[str] = "TEMP:Observation"
    class_name: ClassVar[str] = "Observation"
    class_model_uri: ClassVar[URIRef] = CMDR.Observation


@dataclass
class Process(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TEMP.Process
    class_class_curie: ClassVar[str] = "TEMP:Process"
    class_name: ClassVar[str] = "Process"
    class_model_uri: ClassVar[URIRef] = CMDR.Process

    has_input: Optional[str] = None
    has_output: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_input is not None and not isinstance(self.has_input, str):
            self.has_input = str(self.has_input)

        if self.has_output is not None and not isinstance(self.has_output, str):
            self.has_output = str(self.has_output)

        super().__post_init__(**kwargs)


class ResearchProject(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TEMP.ResearchProject
    class_class_curie: ClassVar[str] = "TEMP:ResearchProject"
    class_name: ClassVar[str] = "ResearchProject"
    class_model_uri: ClassVar[URIRef] = CMDR.ResearchProject


class ResearchSubject(YAMLRoot):
    """
    A Subject that has participated in at least on Study
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TEMP.ResearchSubject
    class_class_curie: ClassVar[str] = "TEMP:ResearchSubject"
    class_name: ClassVar[str] = "ResearchSubject"
    class_model_uri: ClassVar[URIRef] = CMDR.ResearchSubject


@dataclass
class Sampling(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TEMP.Sampling
    class_class_curie: ClassVar[str] = "TEMP:Sampling"
    class_name: ClassVar[str] = "Sampling"
    class_model_uri: ClassVar[URIRef] = CMDR.Sampling

    has_input: Optional[str] = None
    has_output: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_input is not None and not isinstance(self.has_input, str):
            self.has_input = str(self.has_input)

        if self.has_output is not None and not isinstance(self.has_output, str):
            self.has_output = str(self.has_output)

        super().__post_init__(**kwargs)


class Site(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TEMP.Site
    class_class_curie: ClassVar[str] = "TEMP:Site"
    class_name: ClassVar[str] = "Site"
    class_model_uri: ClassVar[URIRef] = CMDR.Site


@dataclass
class Specimen(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TEMP.Specimen
    class_class_curie: ClassVar[str] = "TEMP:Specimen"
    class_name: ClassVar[str] = "Specimen"
    class_model_uri: ClassVar[URIRef] = CMDR.Specimen

    has_parent_specimen: Optional[Union[dict, "Specimen"]] = None
    has_source: Optional[Union[dict, ResearchSubject]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_parent_specimen is not None and not isinstance(self.has_parent_specimen, Specimen):
            self.has_parent_specimen = Specimen(**as_dict(self.has_parent_specimen))

        if self.has_source is not None and not isinstance(self.has_source, ResearchSubject):
            self.has_source = ResearchSubject()

        super().__post_init__(**kwargs)


class Study(YAMLRoot):
    """
    the root class of the data model
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TEMP.Study
    class_class_curie: ClassVar[str] = "TEMP:Study"
    class_name: ClassVar[str] = "Study"
    class_model_uri: ClassVar[URIRef] = CMDR.Study


@dataclass
class Subject(MaterialEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TEMP.Subject
    class_class_curie: ClassVar[str] = "TEMP:Subject"
    class_name: ClassVar[str] = "Subject"
    class_model_uri: ClassVar[URIRef] = CMDR.Subject

    birth_date: Optional[str] = None
    taxon: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.birth_date is not None and not isinstance(self.birth_date, str):
            self.birth_date = str(self.birth_date)

        if self.taxon is not None and not isinstance(self.taxon, str):
            self.taxon = str(self.taxon)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.birth_date = Slot(uri=TEMP.birth_date, name="birth_date", curie=TEMP.curie('birth_date'),
                   model_uri=CMDR.birth_date, domain=None, range=Optional[str])

slots.conditions = Slot(uri=TEMP.conditions, name="conditions", curie=TEMP.curie('conditions'),
                   model_uri=CMDR.conditions, domain=None, range=Optional[str])

slots.diagnoses = Slot(uri=TEMP.diagnoses, name="diagnoses", curie=TEMP.curie('diagnoses'),
                   model_uri=CMDR.diagnoses, domain=None, range=Optional[str])

slots.documents = Slot(uri=TEMP.documents, name="documents", curie=TEMP.curie('documents'),
                   model_uri=CMDR.documents, domain=None, range=Optional[str])

slots.has_input = Slot(uri=TEMP.has_input, name="has_input", curie=TEMP.curie('has_input'),
                   model_uri=CMDR.has_input, domain=None, range=Optional[str])

slots.has_output = Slot(uri=TEMP.has_output, name="has_output", curie=TEMP.curie('has_output'),
                   model_uri=CMDR.has_output, domain=None, range=Optional[str])

slots.has_parent_specimen = Slot(uri=TEMP.has_parent_specimen, name="has_parent_specimen", curie=TEMP.curie('has_parent_specimen'),
                   model_uri=CMDR.has_parent_specimen, domain=None, range=Optional[str])

slots.has_source = Slot(uri=TEMP.has_source, name="has_source", curie=TEMP.curie('has_source'),
                   model_uri=CMDR.has_source, domain=None, range=Optional[str])

slots.is_about = Slot(uri=TEMP.is_about, name="is_about", curie=TEMP.curie('is_about'),
                   model_uri=CMDR.is_about, domain=None, range=Optional[str])

slots.observations = Slot(uri=TEMP.observations, name="observations", curie=TEMP.curie('observations'),
                   model_uri=CMDR.observations, domain=None, range=Optional[str])

slots.source = Slot(uri=TEMP.source, name="source", curie=TEMP.curie('source'),
                   model_uri=CMDR.source, domain=None, range=Optional[str])

slots.subjects = Slot(uri=TEMP.subjects, name="subjects", curie=TEMP.curie('subjects'),
                   model_uri=CMDR.subjects, domain=None, range=Optional[str])

slots.taxon = Slot(uri=TEMP.taxon, name="taxon", curie=TEMP.curie('taxon'),
                   model_uri=CMDR.taxon, domain=None, range=Optional[str])

slots.Database_conditions = Slot(uri=TEMP.conditions, name="Database_conditions", curie=TEMP.curie('conditions'),
                   model_uri=CMDR.Database_conditions, domain=Database, range=Optional[Union[Union[dict, Condition], List[Union[dict, Condition]]]])

slots.Database_diagnoses = Slot(uri=TEMP.diagnoses, name="Database_diagnoses", curie=TEMP.curie('diagnoses'),
                   model_uri=CMDR.Database_diagnoses, domain=Database, range=Optional[Union[Union[dict, "Diagnosis"], List[Union[dict, "Diagnosis"]]]])

slots.Database_documents = Slot(uri=TEMP.documents, name="Database_documents", curie=TEMP.curie('documents'),
                   model_uri=CMDR.Database_documents, domain=Database, range=Optional[Union[Union[dict, "Document"], List[Union[dict, "Document"]]]])

slots.Database_observations = Slot(uri=TEMP.observations, name="Database_observations", curie=TEMP.curie('observations'),
                   model_uri=CMDR.Database_observations, domain=Database, range=Optional[Union[Union[dict, "Observation"], List[Union[dict, "Observation"]]]])

slots.Database_subjects = Slot(uri=TEMP.subjects, name="Database_subjects", curie=TEMP.curie('subjects'),
                   model_uri=CMDR.Database_subjects, domain=Database, range=Optional[Union[Union[dict, "Subject"], List[Union[dict, "Subject"]]]])

slots.Diagnosis_is_about = Slot(uri=TEMP.is_about, name="Diagnosis_is_about", curie=TEMP.curie('is_about'),
                   model_uri=CMDR.Diagnosis_is_about, domain=Diagnosis, range=Optional[Union[dict, Condition]])

slots.Diagnosis_source = Slot(uri=TEMP.source, name="Diagnosis_source", curie=TEMP.curie('source'),
                   model_uri=CMDR.Diagnosis_source, domain=Diagnosis, range=Optional[str])

slots.Document_is_about = Slot(uri=TEMP.is_about, name="Document_is_about", curie=TEMP.curie('is_about'),
                   model_uri=CMDR.Document_is_about, domain=Document, range=Optional[str])

slots.Process_has_input = Slot(uri=TEMP.has_input, name="Process_has_input", curie=TEMP.curie('has_input'),
                   model_uri=CMDR.Process_has_input, domain=Process, range=Optional[str])

slots.Process_has_output = Slot(uri=TEMP.has_output, name="Process_has_output", curie=TEMP.curie('has_output'),
                   model_uri=CMDR.Process_has_output, domain=Process, range=Optional[str])

slots.Sampling_has_input = Slot(uri=TEMP.has_input, name="Sampling_has_input", curie=TEMP.curie('has_input'),
                   model_uri=CMDR.Sampling_has_input, domain=Sampling, range=Optional[str])

slots.Sampling_has_output = Slot(uri=TEMP.has_output, name="Sampling_has_output", curie=TEMP.curie('has_output'),
                   model_uri=CMDR.Sampling_has_output, domain=Sampling, range=Optional[str])

slots.Specimen_has_parent_specimen = Slot(uri=TEMP.has_parent_specimen, name="Specimen_has_parent_specimen", curie=TEMP.curie('has_parent_specimen'),
                   model_uri=CMDR.Specimen_has_parent_specimen, domain=Specimen, range=Optional[Union[dict, "Specimen"]])

slots.Specimen_has_source = Slot(uri=TEMP.has_source, name="Specimen_has_source", curie=TEMP.curie('has_source'),
                   model_uri=CMDR.Specimen_has_source, domain=Specimen, range=Optional[Union[dict, ResearchSubject]])

slots.Subject_birth_date = Slot(uri=TEMP.birth_date, name="Subject_birth_date", curie=TEMP.curie('birth_date'),
                   model_uri=CMDR.Subject_birth_date, domain=Subject, range=Optional[str])

slots.Subject_taxon = Slot(uri=TEMP.taxon, name="Subject_taxon", curie=TEMP.curie('taxon'),
                   model_uri=CMDR.Subject_taxon, domain=Subject, range=Optional[str])