-- Table: public.stock

-- DROP TABLE IF EXISTS public.stock;

CREATE TABLE IF NOT EXISTS public.stock
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    point_of_sale character varying(50) COLLATE pg_catalog."default" NOT NULL,
    product character varying(50) COLLATE pg_catalog."default" NOT NULL,
    date date NOT NULL,
    stock integer NOT NULL,
    CONSTRAINT stock_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.stock
    OWNER to postgres;