# Event Management System

## Requirements

- Projektauftrag
- User Stories
- Dokumentation
  - Komponentendiagramm
  - Projektbeschreibung
- Source Code
  - Code in Git
  - Entwicklung in Feature branch
  - Keine Redundanz im Code
  - Werte können als Parameter übergeben werden, nicht hardcodiert
  - Saubere Trennung zwischen Queries und Programmlogik
  - Exception handling
  - Schema validation
- Applikation
  - User Input über GUI/CLI
  - User Feedback, z. B. „Name darf nicht leer sein“
  - Transaktionshandling/Rollback bei fehlgeschlagenen Transaktionen
  - CRUD Operationen
  - Sinnvolle Daten in der Datenbank
  - Volltextsuche
  - Eingabevalidierung
  - Fehlerbehandlung, z. B. nochmals Eingabe verlangen
  - Minimum 3 Analysefunktionen
  - Reporting
- Schlusspräsentation

## Project Description

A web-based application that allows users to manage and participate in events. It includes features such as CRUD operations, full-text search, transaction handling, and data analysis.

### Backend

The backend infrastructure consists of a containerised `python-flask` image wich makes use of the python `MongoClient` for DB manipulation. The API-Endpoints documentation can be found [here](/documentation/api-endpoints.md).

### Frontend

The GUI interaction for this project will be provided by a web-based angular website. The mockup including documentation can be found [here](/documentation/mockup.md).

### Database

As for DB-technology I've decided to go with MongoDB as it is available under the `SSPL-Licence` and the most popular NoSQL-Database.

### Component Diagram

Outline of the system architecture including client, server and database.

![eventManager-Component-Diagram](/assets/component_diagram_eventManager.svg)

## User Stories

### Epic Backend

|ID|Title|Estimate|Priority|Requirements|DoD|Done|
|-|-|-|-|-|-|-|
|BE-01|Python VENV|1h|high|Create python project with virtual environment.|VENV created and used as interpreter. Dependencies listed in `requirements.txt`. Tested for successful local interaction with flask app.|y|
|BE-02|User Management|1h|high|Basic rudimentary usermanagement.|Implementation of user model. Implemented and tested endpoints `/register`, `/login` and `/delete` for user model.|y|
|BE-03|Event Management|2h|high|Basic event management.|Implementation of event model. Implemented and tested endpoints `/create`, `/participate`, `/cancle`, `/edit` and `/delete` for event model.|y|
|BE-04|Event Analysis|2h|medium|Global analysis and search functionality for events and users.|Implementation of meaningful analysis and search methods for events and user data.|y|

### Epic Frontend

|ID|Title|Estimate|Priority|Requirements|DoD|Done|
|-|-|-|-|-|-|-|
|FE-01|Angular Project init|1h|high|Generate Angular project and plan out frontend stucture.|Angular project initialised and file-folder structured implemented.|y|
|FE-02|Mockup Realisation|4h|high|Implement the basic look and feel of the Mockup.|Angular-Site resembles Mockup, including css, routing, pages and components.|n|
|FE-03|API-Frontend|2h|medium|Implement the backend API-endpoints and logic in to the frontend.|Backend logic and DB-Data implemented following the mockup functionality description.|y|

### Epic Deployment

|ID|Title|Estimate|Priority|Requirements|DoD|Done|
|-|-|-|-|-|-|-|
|DE-01|MongoDB Server Setup|1h|low|Set up MongoDB docker on Server.|MongoDB running and tested on Server.|n|
|DE-02|Backend Deployment|2h|low|Containerise and deploy backend.|Backend running and tested as docker container on server.|n|
|DE-03|Frontend Deployment|2h|low|Containerise and deploy frontend.|Frontend running and tested as docker container on server.|n|
|DE-04|Reverse Proxy|1h|low|Setup reverse proxy, configure DynDNS and register LetsEncrypt SSL/TLS certivicate.|Frontend and backend accessible using HTTPS.|n|

### Epic Documentation

|ID|Title|Estimate|Priority|Requirements|DoD|Done|
|-|-|-|-|-|-|-|
|DO-01|Documentation initialisation|1h|high|Basic structure of documentation should be created. Write down first thoughts for chapter content.|Basic Documentation structure|y|
|DO-02|User Stories|1h|high|Define general Epics. Plan first stories with relevant information. Don't employ waterfall principle.|Epics and first Stories for Project defined. Stories include timeestimate , priority, requirements and DoD.|y|
|DO-03|Component Diagram|1h|medium|Create a diagram displaying the aspired components and their interaction.|Informative Component Diagram with all relevant information and connections.|y|
|DO-04|Frontend Mockup|4h|medium|Create a Mockup of the GUI. Plan out the necessary pages for the project. Describe functionality and design choice.|Mockup with context for all necessary pages.|n|
|DO-05|API Documentation|4h|low|Write the documentation of the api endpoints with relevant parameters, errors, responses etc.|All API Endpoints documented following the Template|n|
|DO-06|Setup-Deployment Documentation|1h|medium|Write the documentation for the setup and deployment of the front- and backend.|Local setup and docker deployment documented step by step. Necessary commands, parameters, links and templates included.|n|
