This is a small project created for getting acquanted with Django and it's basic features.
While doing it I've learned about:
- Django template language;
- Some basic html knowledge (creating forms, sending user data);
- Fundamentals of working with sqlite database through Django models;
- Dynamic form editing in Django;
- Django admin panel.

The main idea of this project is creating a small site (in this case it's a booking club) that collects some user data.
Because dynamic form editing is used, there is also a chance to create additional fields to collect more data from user.
It can be achieved through admin panel by creating new form.
For that you need to go to http://127.0.0.1:8000/admin/, choose FormField and type in the name for new field. 

If the database is empty - you need to create a superuser with a command './manage.py createsuperuser'. 
After that create a Model with the name "participant" and add fields - name, age and favorite_book or some others.
