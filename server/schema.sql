-- claude-sleuth-db :: D1 Schema
-- Run this against your D1 database before deploying the worker.
-- Usage: wrangler d1 execute sleuth-db --file=schema.sql

CREATE TABLE IF NOT EXISTS investigations (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  description TEXT DEFAULT '',
  status TEXT DEFAULT 'active' CHECK(status IN ('active', 'paused', 'closed', 'archived')),
  created_utc TEXT NOT NULL,
  modified_utc TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS entities (
  id TEXT NOT NULL,
  investigation_id TEXT NOT NULL,
  type TEXT NOT NULL,
  name TEXT NOT NULL,
  aliases TEXT DEFAULT '[]',
  identifiers TEXT DEFAULT '{}',
  attributes TEXT DEFAULT '{}',
  source TEXT DEFAULT '',
  source_grade TEXT DEFAULT '',
  evidence_refs TEXT DEFAULT '[]',
  notes TEXT DEFAULT '',
  created_utc TEXT NOT NULL,
  modified_utc TEXT NOT NULL,
  PRIMARY KEY (id, investigation_id),
  FOREIGN KEY (investigation_id) REFERENCES investigations(id)
);

CREATE TABLE IF NOT EXISTS relationships (
  id TEXT NOT NULL,
  investigation_id TEXT NOT NULL,
  source_entity TEXT NOT NULL,
  target_entity TEXT NOT NULL,
  type TEXT NOT NULL,
  direction TEXT DEFAULT 'directed' CHECK(direction IN ('directed', 'undirected')),
  weight REAL DEFAULT 1.0,
  confidence REAL DEFAULT 0.0,
  start_date TEXT,
  end_date TEXT,
  source_intel TEXT DEFAULT '',
  source_grade TEXT DEFAULT '',
  evidence_refs TEXT DEFAULT '[]',
  notes TEXT DEFAULT '',
  created_utc TEXT NOT NULL,
  PRIMARY KEY (id, investigation_id),
  FOREIGN KEY (investigation_id) REFERENCES investigations(id)
);

CREATE TABLE IF NOT EXISTS source_grades (
  id TEXT NOT NULL,
  investigation_id TEXT NOT NULL,
  source_name TEXT NOT NULL,
  claim TEXT NOT NULL,
  reliability TEXT NOT NULL CHECK(reliability IN ('A', 'B', 'C', 'D', 'E', 'F')),
  credibility TEXT NOT NULL CHECK(credibility IN ('1', '2', '3', '4', '5', '6')),
  combined_grade TEXT NOT NULL,
  justification TEXT DEFAULT '',
  action_recommendation TEXT DEFAULT '',
  linked_evidence TEXT DEFAULT '[]',
  graded_utc TEXT NOT NULL,
  PRIMARY KEY (id, investigation_id),
  FOREIGN KEY (investigation_id) REFERENCES investigations(id)
);

CREATE TABLE IF NOT EXISTS timeline_events (
  id TEXT NOT NULL,
  investigation_id TEXT NOT NULL,
  original_datetime TEXT NOT NULL,
  utc_datetime TEXT NOT NULL,
  description TEXT NOT NULL,
  source TEXT DEFAULT '',
  source_reliability TEXT DEFAULT '',
  info_credibility TEXT DEFAULT '',
  entities_involved TEXT DEFAULT '[]',
  location TEXT DEFAULT '',
  category TEXT DEFAULT 'other',
  evidence_ref TEXT DEFAULT '',
  notes TEXT DEFAULT '',
  created_utc TEXT NOT NULL,
  PRIMARY KEY (id, investigation_id),
  FOREIGN KEY (investigation_id) REFERENCES investigations(id)
);

CREATE TABLE IF NOT EXISTS locations (
  id TEXT NOT NULL,
  investigation_id TEXT NOT NULL,
  entity_ref TEXT DEFAULT '',
  label TEXT NOT NULL,
  latitude REAL NOT NULL,
  longitude REAL NOT NULL,
  altitude_m REAL,
  accuracy_m REAL,
  source TEXT DEFAULT '',
  source_grade TEXT DEFAULT '',
  address TEXT DEFAULT '{}',
  observed_utc TEXT,
  collected_utc TEXT,
  temporal_confidence TEXT DEFAULT 'approximate',
  evidence_ref TEXT DEFAULT '',
  notes TEXT DEFAULT '',
  created_utc TEXT NOT NULL,
  modified_utc TEXT NOT NULL,
  PRIMARY KEY (id, investigation_id),
  FOREIGN KEY (investigation_id) REFERENCES investigations(id)
);

CREATE TABLE IF NOT EXISTS evidence_register (
  id TEXT NOT NULL,
  investigation_id TEXT NOT NULL,
  url TEXT DEFAULT '',
  description TEXT DEFAULT '',
  sha256 TEXT DEFAULT '',
  capture_utc TEXT,
  analyst_id TEXT DEFAULT 'claude-sleuth',
  storage_location TEXT DEFAULT '',
  artefact_type TEXT DEFAULT '',
  notes TEXT DEFAULT '',
  created_utc TEXT NOT NULL,
  PRIMARY KEY (id, investigation_id),
  FOREIGN KEY (investigation_id) REFERENCES investigations(id)
);

CREATE TABLE IF NOT EXISTS progress (
  investigation_id TEXT PRIMARY KEY,
  current_index INTEGER DEFAULT 0,
  completed TEXT DEFAULT '[]',
  modified_utc TEXT NOT NULL,
  FOREIGN KEY (investigation_id) REFERENCES investigations(id)
);

CREATE TABLE IF NOT EXISTS notebook (
  investigation_id TEXT PRIMARY KEY,
  content TEXT DEFAULT '',
  modified_utc TEXT NOT NULL,
  FOREIGN KEY (investigation_id) REFERENCES investigations(id)
);
