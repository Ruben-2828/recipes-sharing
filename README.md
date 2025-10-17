# Recipes Sharing web app

#### Tenderini Ruben - 879290

## Table of Contents

#### 1. [Objective](#objective)
#### 2. [Contents](#contents)
#### 3. [Tools](#tools)
#### 4. [Setup](#setup)
#### 5. [Codebase](#codebase)

## Objective
This project main goal is to create a Django-based web application that enables users to share, discover, and manage food recipes in a user-friendly environment.

## Contents

This web application is a recipe sharing platform that allows users to discover, create, and manage food recipes. The main features include:

1. **Recipe Discovery**
   - Browse a list of the latest recipes
   - View detailed recipe information including ingredients and preparation steps
   - See recipe duration and author information

2. **Recipe Management**
   - Create new recipes with title, duration, and detailed description
   - Add multiple ingredients with their quantities
   - Update existing recipes
   - Delete recipes (only for recipe authors)

3. **User Features**
   - User authentication system
   - Personal recipe management
   - Ability to edit and delete own recipes
   - View recipes created by other users

4. **Modern UI/UX**
   - Responsive design that works on all devices
   - Clean and intuitive interface
   - Easy navigation between recipes
   - Dynamic ingredient management when creating recipes

## Tools

1. **Python:** High-level multipurpouse programming language.

2. **Django:** Full-featured web framework that uses MTV architecture.

3. **PostgreSQL:** Powerful open-source relational database system for reliable data management and performance.

4. **Docker:** Tool that helps developers build, share, run, and verify applications using containerization.

5. **GitHub:** Version control platform for project management.

## Setup

1. **Install Docker:** To install docker, follow this guide from the official website: 
    [docker.com/get-started](https://www.docker.com/get-started/)

2. **Install Git:** To install git, use the official website download page: 
    [git-scm.com/downloads](https://git-scm.com/downloads)

3. **Clone repository:** Clone this repository using the following command: 
    ``` 
    git clone https://github.com/Ruben-2828/recipes-sharing.git 
    ```

4. **Set .env file:** Using the file ```.env.example```, create an actual ```.env``` file and set proper values for the environment variables.

5. **Run project:** Open a terminal and navigate to the project folder. Once here, simply run the following command:
    ``` 
    docker compose up -d 
    ```
    Make sure docker is running before executing the command above.

6. **Enter the website:** Oper your favourite browser and type:
    ``` 
    127.0.0.1:8000 
    ```

## Codebase
- `recipes_app/`: Main application for recipes management
- `users_app/`: User management application.
- `templates/`: Directory containing base HTML templates.
- `static/`: Directory for base static files (CSS, JavaScript, images).
- `recipes_project/`: Django project configuration directory. 
- `Dockerfile`: Configuration file for Docker container.
- `.dockerignore`: Specifies files to ignore in Docker builds.
- `requirements.txt`: Python package dependencies.
- `docker-compose.yaml`: Docker services configuration.
- `manage.py`: Django's command-line utility.
- `.gitignore`: Specifies files to ignore in Git.
- `.env.example`: Example of an environment variables file
