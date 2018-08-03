# Seed app for Y3 projects

This is a complete seed app project with: Flask, SQLAlchemy, Bootstrap, jQuery.
You will need to fork this repo and then start working on your own project.
//
### 1. Fork the repo

1. Select a person in your group responsible for git management
2. Click on the fork button on the top right corner of the page and fork it on your profile
3. Clone the new repo that was created on your profile

```
cd ~/Desktop/
git clone ...
cd Y3S18-seed-app/
source initialize.sh
```

### 2. Structure

- project
  - __init__.py: main app creation
  - models.py: define your tables here
  - views.py: general views and routes here
  - users.py: user blueprint, user-related/auth routes here
  - forms.py: define forms here
  - static: add static files in corresponding folder (css, js, img)
  - templates: add your HTML templates here
- instance
  - flask.cfg: define your db and secret key values here

### 3. Run the server locally

```
flask run
```
