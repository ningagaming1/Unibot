# UniBot

UniBot is a modular Python-based student assistant designed to combine multiple independent utilities into a single application. Rather than building one large program, UniBot follows a modular architecture where every feature is developed as its own module and connected through a central router. This approach makes the project easier to maintain, debug, and expand while keeping the code organized and reusable.

## Features

* Secure user login system
* Modular router-based architecture
* Budget Tracker
* Todo Manager
* Contacts Manager
* Journal with multi-line writing
* Journal reader
* File Organizer
* Tic Tac Toe
* Flip a Coin
* Grades Analyzer
* Web Utilities
* LPU Utilities
* Administrator section with role-based access
* Multi-command support using the keyword `and`

## Project Architecture

UniBot follows a simple but scalable architecture.

```
main.py
    │
    ▼
Login System
    │
    ▼
Central Router
    │
    ├── Budget
    ├── Todo
    ├── Contacts
    ├── Journal
    ├── File Organizer
    ├── Tic Tac Toe
    ├── Flip a Coin
    ├── Grades
    ├── Web
    ├── LPU
    └── Chatbot
```

Every module exposes the same interface:

```python
handle(user_input, user_data)
```

The router's responsibility is only to determine which module should process the user's request. Each module contains its own functionality, making the project easy to extend without modifying the routing system.

## Journal Module

The Journal module currently supports:

* Creating journal entries
* Multi-line writing
* Automatic timestamp generation
* UTF-8 text storage
* Reading previous journal entries
* Selecting journals by index
* Input validation through exception handling

Each journal is stored as an individual text file while its location is recorded inside the user's data.

## User Data

All modules receive a shared `user_data` dictionary that stores information such as:

* User ID
* Username
* Password
* Budget
* Tasks
* Contacts
* Grades
* Journal entries

This allows every module to access only the information it requires while keeping the overall design consistent.

## Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
* Modular Programming
* File Handling
* NumPy
* Pandas

## Design Philosophy

The primary objective of UniBot is not simply to combine many small programs but to demonstrate clean software architecture. The project emphasizes readability, maintainability, scalability, and reusable code. Every feature is implemented as an independent module, making future expansion straightforward without turning the application into one large, difficult-to-maintain codebase.

## Project Status

**Current Progress:** ~85%

The core architecture and most planned modules are implemented. Future updates will focus on refining existing modules, improving usability, expanding administrator functionality, and adding new utilities while preserving the modular design.

## Future Goals

* Continue expanding student productivity tools
* Improve module interactions
* Add additional utility modules
* Enhance user experience
* Continue learning and applying new Python concepts as the project evolves

---

UniBot is an active learning and portfolio project created to demonstrate practical Python development, modular software design, and scalable application architecture.
