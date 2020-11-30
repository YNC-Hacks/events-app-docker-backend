ALTER TABLE "memberships" ADD FOREIGN KEY ("user_email") REFERENCES "users" ("user_email");

ALTER TABLE "memberships" ADD FOREIGN KEY ("organization_id") REFERENCES "organizations" ("organization_id");

ALTER TABLE "attendance" ADD FOREIGN KEY ("user_email") REFERENCES "users" ("user_email");

ALTER TABLE "attendance" ADD FOREIGN KEY ("event_id") REFERENCES "events" ("event_id");

ALTER TABLE "events" ADD FOREIGN KEY ("organization_id") REFERENCES "organizations" ("organization_id");
