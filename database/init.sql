CREATE TABLE "users" (
  "user_email" text PRIMARY KEY,
  "name" text,
  "verified" boolean,
  "hash" text
);

CREATE TABLE "memberships" (
  "membership_id" int PRIMARY KEY,
  "user_email" text,
  "organization_id" int,
  "admin" boolean
);

CREATE TABLE "organizations" (
  "organization_id" int PRIMARY KEY,
  "name" text
);

CREATE TABLE "attendance" (
  "attendance_id" int PRIMARY KEY,
  "user_email" text,
  "event_id" int,
  "registration_date" DATE,
  "registration_time" TIME
);

CREATE TABLE "events" (
  "event_id" int PRIMARY KEY,
  "organization_id" int,
  "event_date" DATE,
  "event_time" TIME,
  "location" text,
  "capacity" int
);