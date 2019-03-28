CREATE SCHEMA IF NOT EXISTS kudosbot;

-- Create read-write role and grant rights
DO $$
  BEGIN
    CREATE ROLE r_kudosbot_rw NOSUPERUSER INHERIT NOCREATEDB NOCREATEROLE NOREPLICATION;
    EXCEPTION
    WHEN OTHERS THEN
      RAISE NOTICE 'not creating role r_kudosbot_rw -- it already exists';
  END
  $$;

GRANT USAGE ON SCHEMA kudosbot TO r_kudosbot_rw;
GRANT ALL ON ALL TABLES IN SCHEMA kudosbot TO r_kudosbot_rw;
ALTER DEFAULT PRIVILEGES IN SCHEMA kudosbot GRANT ALL ON TABLES TO r_kudosbot_rw;

-- Create read-write group role and grant rights
DO $$
  BEGIN
    CREATE ROLE g_kudosbot_rw NOSUPERUSER INHERIT NOCREATEDB NOCREATEROLE NOREPLICATION;
    EXCEPTION
    WHEN OTHERS THEN
      RAISE NOTICE 'not creating group role g_kudosbot_rw -- it already exists';
  END
  $$;

GRANT r_kudosbot_rw TO g_kudosbot_rw;

-- Create read-write user and make it valid forever
DO $$
  BEGIN
    CREATE ROLE kudosbot_rw WITH LOGIN;
    EXCEPTION
    WHEN OTHERS THEN
      RAISE NOTICE 'not creating user kudosbot_rw -- it already exists';
  END
  $$;

ALTER ROLE kudosbot_rw VALID UNTIL 'infinity';
GRANT g_kudosbot_rw TO kudosbot_rw;

ALTER ROLE kudosbot_rw SET search_path to kudosbot;


create table kudosbot.user_kudos
(
  user_id varchar(12) not null,
  event_ts varchar,
  channel varchar,
  text varchar,
  client_msg_id varchar,
  creation_ts timestamp
);