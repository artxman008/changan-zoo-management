# CHANGAN Zoo Management

An Odoo 17 custom module developed for the CHANGAN Odoo Developer Assignment.

This module provides a simple yet production-oriented Zoo Management System for managing zoo keepers, living zones, and animals while demonstrating Odoo development best practices.

---

# Objectives

This project demonstrates the following Odoo development concepts:

- Odoo ORM Relationships
- Many2one & One2many
- SQL Constraints
- Python Constraints
- Computed Fields
- Smart Buttons
- Search Views
- Filters & Group By
- Dynamic Actions
- Data Integrity
- Clean Module Architecture

---

# Features

## Zoo Keeper

- Create and manage zoo keepers
- Store keeper information
- Upload keeper photo
- Automatically calculate:
  - Assigned Living Zones
  - Total Animals

---

## Living Zone

- Create living zones
- Assign zoo keeper
- Configure capacity
- Unique zone code
- Smart Button to view related animals
- Automatic animal count

---

## Animal

- Create animal records
- Assign living zone
- Store species, gender, birth date and weight
- Search by:
  - Name
  - Species
  - Living Zone
- Filter:
  - Male
  - Female
  - Heavy Animals
- Group By:
  - Species
  - Living Zone

---

# Data Model

```text
Zoo Keeper (1)
      │
      │ One2many
      ▼
Living Zone (N)
      │
      │ One2many
      ▼
Animal (N)
```

---

# Business Rules

### Living Zone

- Zone code must be unique
- Capacity must be greater than zero
- Capacity cannot be lower than the current animal count

### Animal

- Weight must be greater than zero
- Birth date cannot be in the future
- Animals cannot exceed living zone capacity

### Referential Integrity

- Living Zone cannot be deleted while animals exist
- Zoo Keeper cannot be deleted while assigned to living zones

---

# Technical Highlights

- Odoo 17 Community Edition
- Python
- PostgreSQL
- Docker Compose
- Odoo ORM
- Smart Buttons
- Dynamic Domain
- Dynamic Context
- Search View
- SQL Constraints
- Python Constraints
- Computed Fields
- Access Control (ACL)

---

# Screenshots

## Zoo Keeper

> *(Insert Screenshot)*

---

## Living Zone

> *(Insert Screenshot)*

---

## Animal

> *(Insert Screenshot)*

---

## Smart Button

> *(Insert Screenshot)*

---

## Search View

> *(Insert Screenshot)*

---

# Project Structure

```text
changan-zoo-management
│
├── docker-compose.yml
├── README.md
├── custom_addons
│   └── zoo
│       ├── models
│       ├── security
│       ├── views
│       ├── __manifest__.py
│       └── __init__.py
│
└── .gitignore
```

---

# Installation

Clone repository

```bash
git clone https://github.com/<your-account>/changan-zoo-management.git
```

Go to project

```bash
cd changan-zoo-management
```

Run Docker

```bash
docker compose up -d
```

Open

```
http://localhost:8069
```

Install

```
CHANGAN Zoo Management
```

---