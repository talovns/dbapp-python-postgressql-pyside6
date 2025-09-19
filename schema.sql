-- (опционально) своя схема
-- CREATE SCHEMA IF NOT EXISTS finance;
-- SET search_path = finance, public;

-- ENUM'ы
CREATE TYPE expense_category AS ENUM ('Food','Transport','Entertainment','Health','Education','Utilities','Other');
CREATE TYPE payment_method   AS ENUM ('Cash','Card','Online');

CREATE TABLE app_user (
  user_id    BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  username   TEXT NOT NULL UNIQUE,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE merchant (
  merchant_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  name        TEXT NOT NULL UNIQUE,
  city        TEXT,
  created_at  TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE expense (
  expense_id  BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  user_id     BIGINT NOT NULL REFERENCES app_user(user_id) ON DELETE CASCADE,
  merchant_id BIGINT REFERENCES merchant(merchant_id) ON DELETE SET NULL,
  category    expense_category NOT NULL,
  method      payment_method   NOT NULL,
  amount      NUMERIC(10,2)    NOT NULL CHECK (amount > 0),
  spent_at    DATE             NOT NULL,
  note        TEXT,
  created_at  TIMESTAMPTZ      NOT NULL DEFAULT now()
);

INSERT INTO app_user (username) VALUES ('demo') ON CONFLICT (username) DO NOTHING;

