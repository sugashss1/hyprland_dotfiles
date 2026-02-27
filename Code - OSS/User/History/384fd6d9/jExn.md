##Multi-Tenant Task & Project Management System

A role-based task and project management web application built with Flask, Google Firestore, and Firebase Authentication concepts.
The system supports CEOs, Managers, and Employees, providing Kanban task tracking, project management, and admin controls.

##Features
Authentication & Authorization

Secure login with hashed passwords

Session-based authentication

Role-based access control:

CEO

Manager

Employee (user)

Role Capabilities
Role	Capabilities
CEO	View all projects & tasks, create users, assign managers
Manager	Create projects & tasks, assign tasks to employees
Employee	View only assigned tasks

##Task Management

Kanban board with:

TODO

IN PROGRESS

DONE

Drag & drop task status updates

Role-filtered task visibility

Task visualization (status distribution)

##Project Management

Create, edit, delete projects

CEO assigns projects to managers

Managers manage their own projects

Project-task association

##Dashboard

User profile summary

Admin actions (Create User)

Task status visualization

Role-based UI rendering

##Tech Stack

Backend: Flask (Python)

Database: Google Firestore

Auth: Session-based (password hashing)

Frontend: Jinja2, HTML, CSS, JavaScript

Charts: Chart.js