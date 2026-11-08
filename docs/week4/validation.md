# TrimLine validation

| Rule | Layer | How I tested it | What happened |
| --- | --- | --- | --- |
| Name, email, service required | Browser | Clicked Get a ticket with empty name field | Browser blocked submission with a native popup |
| Name, email, service required; service must exist | Flask | curl with empty name, invalid email, service_id=999 | 400 Bad Request, all 3 field errors shown, nothing saved |
| Name must be 80 characters or fewer | Flask | curl with an 85-character name | 400 Bad Request |
| A ticket needs a real service | Database (FOREIGN KEY) | `INSERT INTO tickets (user_id, service_id) VALUES (1, 999);` | `ERROR: violates foreign key constraint "tickets_service_id_fkey"` |
| Ticket status must be one of 5 values | Database (CHECK) | `UPDATE tickets SET status = 'lost' WHERE id = 1;` | `ERROR: violates check constraint "ck_tickets_status"` |
| One account per email | Database (UNIQUE) | `INSERT INTO users (name, email) VALUES ('Copy', 'raven.cosning@g.msuiit.edu.ph');` | `ERROR: duplicate key value violates unique constraint "users_email_key"` |
| A service's avg_minutes must be positive | Database (CHECK) | `INSERT INTO services (name, avg_minutes) VALUES ('Test', 0);` | `ERROR: violates check constraint "ck_services_avg_minutes"` |
| A service with tickets cannot be deleted | Database (RESTRICT) | `DELETE FROM services WHERE id = 1;` | `ERROR: violates foreign key constraint "tickets_service_id_fkey" on table "tickets"` |

No SQL is built with f-strings anywhere in the codebase (`git grep` check printed nothing).