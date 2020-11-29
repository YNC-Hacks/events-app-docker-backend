CREATE TABLE "users" (
  "user_email" text PRIMARY KEY,
  "name" text,
  "verified" boolean
);

CREATE TABLE "memberships" (
  "membership_id" int PRIMARY KEY,
  "user_email" text,
  "organization_id" int,
  "admin" boolean
);

CREATE TABLE "organization" (
  "organization_id" int PRIMARY KEY,
  "name" text
);

CREATE TABLE "attendance" (
  "user_email" text,
  "event_id" int,
  "registration_date" timestamp,
  "registration_time" timestamp
);

CREATE TABLE "events" (
  "event_id" int PRIMARY KEY,
  "organization_id" int,
  "event_date" DATE,
  "event_time" TIMESTAMP,
  "location" text,
  "capacity" int
);