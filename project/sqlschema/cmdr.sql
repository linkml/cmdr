

CREATE TABLE "Container" (
	materials TEXT, 
	participations TEXT, 
	processes TEXT, 
	investigations TEXT, 
	subjects TEXT, 
	PRIMARY KEY (materials, participations, processes, investigations, subjects)
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
	has_input TEXT, 
	has_output TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "SpecimenCollectionProcess" (
	id TEXT NOT NULL, 
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
	PRIMARY KEY (id), 
	FOREIGN KEY(source) REFERENCES "Subject" (id)
);

CREATE TABLE "Participation" (
	includes TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	involved_in TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(includes) REFERENCES "Subject" (id)
);
