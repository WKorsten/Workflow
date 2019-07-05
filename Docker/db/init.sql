CREATE DATABASE gnomad;
use gnomad;

CREATE TABLE variants (
  variant VARCHAR(1000) UNIQUE,
  gene VARCHAR(20),
  uniprot VARCHAR(20),
  AF FLOAT
);