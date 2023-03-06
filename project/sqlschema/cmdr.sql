

CREATE TABLE "Database" (
	subjects TEXT, 
	PRIMARY KEY (subjects)
);

CREATE TABLE "Diagnosis" (
	is_about TEXT, 
	source TEXT, 
	PRIMARY KEY (is_about, source)
);

CREATE TABLE "Document" (
	is_about TEXT, 
	PRIMARY KEY (is_about)
);

CREATE TABLE "Process" (
	has_input TEXT, 
	has_output TEXT, 
	PRIMARY KEY (has_input, has_output)
);

CREATE TABLE "Sampling" (
	has_input TEXT, 
	has_output TEXT, 
	PRIMARY KEY (has_input, has_output)
);

CREATE TABLE "Specimen" (
	has_source TEXT, 
	has_parent_specimen TEXT, 
	PRIMARY KEY (has_source, has_parent_specimen)
);

CREATE TABLE "Subject" (
	taxon TEXT, 
	birth_date TEXT, 
	PRIMARY KEY (taxon, birth_date)
);
