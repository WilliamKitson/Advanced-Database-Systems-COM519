# Advanced Database Systems COM519

Tkinter desktop application for managing a restaurant-style SQLite database. The app includes staff login, team management, menu management, nutrition lookup, menu item images, and XML backup export.

## Project Contents

| File | Purpose |
| --- | --- |
| `main.py` | Application entry point. Opens the Tkinter UI using the bundled database. |
| `presentation.py` | Main UI controller for login, actions, team, menu, nutrition, and backup screens. |
| `login_manager.py` | Authenticates staff users against the `Staff` table using SHA-256 password hashes. |
| `team_manager.py` | Reads, adds, edits, and deletes staff records and staff roles. |
| `menu_manager.py` | Reads, adds, and edits menu records and menu categories. |
| `nutrition_manager.py` | Reads ingredient, weight, and calorie data for menu items. |
| `roles_manager.py` | Reads available staff roles. |
| `image_writer.py` | Stores menu item images as BLOB data and loads them for display. |
| `backup_xml.py` | Exports database tables to an XML file. |
| `input_validator.py` | Validates password strength for staff edits. |
| `injection_detector.py` | Checks input for suspicious SQL-like substrings before database writes. |
| `4kitsw10_COM519_database` | Bundled SQLite database used by the application. |

## Requirements

- Python 3
- Tkinter
- SQLite support through Python's standard `sqlite3` module
- Pillow
- tkcalendar

Install the external Python packages with:

```bash
python3 -m pip install pillow tkcalendar
```

Tkinter and SQLite are normally included with standard Python installations. If Tkinter is missing, install a Python distribution that includes Tk support.

## Running the App

From the project root:

```bash
python3 main.py
```

The application opens a desktop window. The default admin login shown by the app is:

```text
Username: u
Password: p
```

## Main Workflows

After login, the actions screen provides:

- `Manage Team Members`: view staff, add staff, edit staff details, assign roles, update passwords, and delete staff.
- `Manage Menu`: view menu items, add menu items, edit menu item category/name/price/cook time, attach an image, and open nutrition details.
- `Backup to XML`: export core database tables to an XML file selected through a save dialog.

Most rows are opened by double-clicking them in the table view.

## Database

The app uses the SQLite database file `4kitsw10_COM519_database` directly. Keep this file in the project root unless you also update the database path in `main.py`.

The database contains these tables:

- `Staff`
- `Roles`
- `Staff_Roles`
- `Menu`
- `Categories`
- `Ingredients`
- `Menu_Ingredients`
- `Orders`

It also defines these views:

- `View_Team_Members`
- `Staff_Edit_Data`
- `Customer_Facing_Menu`
- `Menu_Item_Neutrition`

Triggers are used to create a staff-role row after a staff member is inserted, remove staff-role rows after staff deletion, and remove menu-ingredient rows after menu deletion.

## Notes

- Staff passwords are stored as SHA-256 hashes.
- New staff usernames are generated from forename and surname when added through the add screen.
- Editing an existing staff member requires a password with at least 10 characters, including lowercase letters, uppercase letters, and numbers.
- Menu item images are stored in the `Menu.Image` BLOB column.
- XML backups include `Staff`, `Roles`, `Staff_Roles`, `Menu`, `Categories`, `Ingredients`, and `Menu_Ingredients`.

