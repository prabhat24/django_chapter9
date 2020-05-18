<h3>objective chapter 3 Models and Databases</h3>
1. first tell Django about the database you intend to use (i.e. configure DATABASES in settings.py) <br>
2. First, create your new model(s) in your Django application’s models.py file. (categories and pages)  <br>
3. Update admin.py to include and register your new model(s). <br>
4. Perform the migration `$python manage.py makemigrations <app_name>`.<br>
5. Apply the changes `$ python manage.py migrate`. This will create the necessary infrastruc-
ture within the database for your new model(s).<br>
6. Create/edit your population script for your new model(s).<br>