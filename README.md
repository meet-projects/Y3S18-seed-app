# Seed app for Y2 projects

This is a complete seed app project with: Flask, SQLAlchemy, Bootstrap, jQuery
You will need to fork this repo and then start working on your own project.

### 1. Fork the repo

1. Select a person in your group responsible for git / github management
2. Click on the fork button on the top right corner of the page and fork it on your profile
3. git clone the new repo that was created on your profile

```
cd ~/Desktop/
git clone ...
cd Y2S17-seed-app/
source initialize.sh
```

### 2. Structure

* `model.py`: define your tables here
* `app.py`: define your routes here
* `templates/`: add your HTML templates here
* `static/`: add your static files in the corresponding folder (css, js, img)

### 3. Create the database and tables
Once you added your classes to `model.py` run the following command to create your database:

```
python create_db.py
```

### 2. Run the server locally

```
flask run
```