

CREATE TABLE "Container" (
	materials TEXT, 
	participations TEXT, 
	material_processings TEXT, 
	specimen_collection_processes TEXT, 
	investigations TEXT, 
	subjects TEXT, 
	PRIMARY KEY (materials, participations, material_processings, specimen_collection_processes, investigations, subjects)
);

CREATE TABLE "Investigation" (
	id TEXT NOT NULL, 
	name TEXT, 
	part_of TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(part_of) REFERENCES "Investigation" (id)
);

CREATE TABLE "MaterialProcessing" (
	id TEXT NOT NULL, 
	name TEXT, 
	has_input TEXT, 
	has_output TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Quantity" (
	has_raw_value TEXT, 
	has_numeric_value FLOAT, 
	has_unit TEXT, 
	comparator TEXT, 
	PRIMARY KEY (has_raw_value, has_numeric_value, has_unit, comparator)
);

CREATE TABLE "SpecimenCollectionProcess" (
	id TEXT NOT NULL, 
	name TEXT, 
	has_input TEXT, 
	has_output TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Subject" (
	id TEXT NOT NULL, 
	name TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "MaterialEntity" (
	id TEXT NOT NULL, 
	name TEXT, 
	used_in TEXT, 
	source TEXT, 
	volume TEXT, 
	concentration TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(source) REFERENCES "Subject" (id)
);

CREATE TABLE "Participation" (
	id TEXT NOT NULL, 
	name TEXT, 
	involved_in TEXT, 
	includes TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(includes) REFERENCES "Subject" (id)
);
