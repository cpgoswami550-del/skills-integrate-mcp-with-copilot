# Issues to create: Integrate Gymie features

The following issues are drafts for features to add to `skills-integrate-mcp-with-copilot`. You can create them manually, or run `scripts/create_issues.py` with a GitHub token to open them automatically.

Repository: cpgoswami550-del/skills-integrate-mcp-with-copilot

---

1) **Add persistent storage (SQLite) for activities**

- **Problem:** Current activities are in-memory and lost on restart.
- **Proposed:** Add SQLite + ORM models and migrations for activities and participants; swap in DB-backed CRUD for existing endpoints.
- **Acceptance criteria:**
  - `Activity` and `Participant` models with migrations exist.
  - `GET /activities`, `POST /activities/{name}/signup`, `DELETE /activities/{name}/unregister` use DB.
  - Tests for signup/unregister are added.
- **Files to modify:** `src/app.py`, add `src/models.py`, update `requirements.txt`.

---

2) **Add user authentication (email-based) and basic ACL**

- **Problem:** No authentication or roles; anyone can sign up students.
- **Proposed:** Implement simple auth (FastAPI OAuth2 password flow), add roles: `admin`, `teacher`, `student`. Protect admin endpoints.
- **Acceptance criteria:**
  - Login/register endpoints.
  - Admin-only endpoints protected.
  - Seed an admin user for local dev.
- **Files:** `src/auth.py`, update routes in `src/app.py`.

---

3) **User management UI & API**

- Add endpoints + minimal admin UI to list users, create/edit users and assign roles.
- **Acceptance criteria:** CRUD API for users and a new static admin page under `/static/admin_users.html`.

---

4) **Membership/Subscription support (plans & signup caps)**

- Introduce `Plan`/`Membership` concept and ability to attach plans to activities (e.g., paid clubs, priority signups).
- **Acceptance criteria:** Plan model, admin APIs for plans, activity->plan association.

---

5) **Billing & invoices (optional)**

- Implement invoices for paid activities, store payments, invoice numbers, and seed invoice settings.
- **Acceptance criteria:** Invoice model, payment endpoints (mock), invoice numbering configuration.

---

6) **Dashboard & reporting**

- Add a simple admin dashboard showing counts: total activities, registrations this month, full activities, upcoming schedules.
- **Acceptance:** New `/static/admin_dashboard.html` plus API endpoints to provide metrics.

---

7) **SMS/email notifications for signups**

- Integrate optional SMS/email notifications for signup confirmations and reminders (configurable).
- **Acceptance:** Configurable provider, mock provider for dev, endpoints to trigger notifications.

---

8) **Media (profile images) support**

- Allow users to upload profile images and serve via static path; integrate storage in `static/uploads`.
- **Acceptance:** Upload API, storage, and display in admin user list.

---

9) **Scheduler (cron) for reminders and cleanup**

- Add scheduled tasks (e.g., cleanup stale signups, send reminders) using APScheduler or FastAPI background tasks + cron setup doc.
- **Acceptance:** Scheduler service and docs to enable cron.

---

10) **Logging, error monitoring, and debug tooling**

- Add structured logging, Sentry integration optional, and a debug mode setting.
- **Acceptance:** Configurable logging and Sentry env var usage.

---

11) **Tests and seed data**

- Add unit tests for core signup flows and fixtures/seeds for demo data.
- **Acceptance:** `pytest` setup, `tests/` with signup/unregister tests, and a seed script.

---

12) **Docs & install guide update**

- Update `README.md` with new setup steps: DB migrations, env vars, running scheduler, and demo credentials.
- **Acceptance:** Clear run instructions and example `.env`.

---

To auto-create these issues via GitHub API, run `scripts/create_issues.py` (see `README` in `scripts/`).
