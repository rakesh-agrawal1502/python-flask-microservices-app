CREATE SCHEMA IF NOT EXISTS sample;

CREATE SEQUENCE sample.customers_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

CREATE SEQUENCE sample.invoices_invoice_number_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

CREATE TABLE sample.customers
(
    id integer NOT NULL DEFAULT nextval('sample.customers_id_seq'::regclass),
    name character varying COLLATE pg_catalog."default" NOT NULL,
    address character varying COLLATE pg_catalog."default",
    email character varying COLLATE pg_catalog."default" NOT NULL,
    created_on timestamp without time zone,
    updated_on timestamp without time zone,
    CONSTRAINT customers_pkey PRIMARY KEY (id)
);


CREATE TABLE sample.invoices
(
    invoice_number integer NOT NULL DEFAULT nextval('sample.invoices_invoice_number_seq'::regclass),
    customer_id integer,
    amount integer,
    CONSTRAINT invoices_pkey PRIMARY KEY (invoice_number),
    CONSTRAINT invoices_customer_id_fkey FOREIGN KEY (customer_id)
        REFERENCES sample.customers (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);