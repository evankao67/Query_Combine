--
-- Greenplum Database database dump
--

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: macc_all_brand_line_id_info; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE macc_all_brand_line_id_info (
    lineid character varying,
    name character varying,
    phone character varying,
    email character varying,
    status character varying,
    gender character varying,
    birthday character varying,
    updated_at timestamp without time zone,
    created_at timestamp without time zone,
    customer_id character varying
);


ALTER TABLE public.macc_all_brand_line_id_info OWNER TO postgres;

--
-- Name: macc_clid_decode_result; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE macc_clid_decode_result (
    clid character varying,
    memberid character varying,
    created_time timestamp without time zone
);


ALTER TABLE public.macc_clid_decode_result OWNER TO postgres;

--
-- Name: macc_clid_retuid_mapping_table; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE macc_clid_retuid_mapping_table (
    clid character varying,
    retuid character varying,
    created_time timestamp without time zone,
    updated_time timestamp without time zone
) ;


ALTER TABLE public.macc_clid_retuid_mapping_table OWNER TO postgres;

--
-- Name: macc_query_by_member_id_tags; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE macc_query_by_member_id_tags (
    member_id character varying,
    line_uid character varying,
    tags character varying,
    created_time timestamp without time zone
);


ALTER TABLE public.macc_query_by_member_id_tags OWNER TO postgres;

--
-- Name: macc_retuid_memberid_lineuid_map; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE macc_retuid_memberid_lineuid_map (
    retuid character varying,
    member_id character varying,
    line_uid character varying,
    tags character varying,
    created_time timestamp without time zone,
    updated_time timestamp without time zone
);


ALTER TABLE public.macc_retuid_memberid_lineuid_map OWNER TO postgres;

--
-- Greenplum Database database dump complete
--



