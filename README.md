# ID and Password Manager – Offline Credential Storage with Tkinter
* * *

## Description

This project is a Tkinter-based Email ID and Password Manager that lets users store, search, update, and delete their credentials locally.
All data is saved in a text file, with a GUI for easy interaction, password visibility toggle, and options to view or clear all records.
It works completely offline and includes customizable colors and an about section for project details.

### Features Of Application Are:-

#### 1. Save Credentials
User can input an email ID and password and save them into a file.
Validates inputs (shows error if empty).

#### 2. Search Credentials
Retrieves the password for a given email ID from the stored file.
Handles cases where ID is missing or password is empty.

#### 3. Update Credentials
Modify the password for an existing email ID.
Checks if the ID exists before updating.

#### 4. Delete Credentials
Removes a specific ID-password pair from storage.

#### 5. how All Credentials
Opens a new window showing all saved IDs and passwords.
Includes a scrollbar for large data.
Has options to clear the screen, change background color, or delete all data.

#### 6. Clear All Data
Deletes the IdDatabase.txt file entirely.

#### 7. Password Visibility Toggle
"Hide" (masked) or "Show" (plain text) password in the entry field using radio buttons.

#### 8. Customizable UI
Change label background colors using a color chooser.
Multiple menus: File, Edit, Setting, About.

#### 9. About Section
Shows project information (“About GUI”) and developer details (“About Me”).

#### 10. Error Handling
Different message boxes for empty inputs, missing IDs, and missing passwords.
* * *

##  What This Helps With:
1. This tool helps you securely organize and manage your email IDs and passwords in one place without relying on internet-based services.
2. It eliminates the need to remember multiple credentials, reduces the risk of losing them, and allows quick retrieval whenever needed.
3. The offline storage ensures your data stays on your device, giving you full control and privacy.
* * * 


## Technologies Used:
- Python – Core programming language for logic and functionality.
- Tkinter – Python’s standard GUI library for creating the application interface.
- File Handling – To store, retrieve, update, and delete credentials in a local text file.
- OS Module – For file operations and system-level interactions (if applicable in the code).
* * *

## Requirements :-
1. `Python = 3.12.3`
2. `Tkinter = 8.6.14`
* * *


## How To Run In Your Machine :-
_Save Python file and give it to a name_

_Save Ico file of Image With Same Name_

***Open Your Terminal/cmd and type***
``` python
python name_of_your_file.py
```
