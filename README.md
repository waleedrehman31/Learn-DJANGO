# Learning DJANGO Python

- I am Learning DJANGO for webdevelopment. From free code camp and this is project i learn DJANGO.

## Important Cammand

### For Virtual Enviroment

- **For installing virtual enviroment.**

  > `pip3 install virtualenvwrapper-win`

- **For making virtual enviroment.**

  > `virtualenv projectName`

- **For making virtual enviroment with specific version of python.**

  > `virtualenv projectName -p python3`

- **To Start Vitual Enviroment.**

  - For MacOS

    > `Source bin/activate`

  - For Windows
    > `.\Scripts\activate`

- Deactivate virtual Enviroment
  > `deactivate`

### DJANGO PROJECT

- **Install DJANGO**.

  - for latest version

    > `pip install django ` OR ` pip3 install django`

  - for specific version
    > `pip install django=version ` OR ` pip3 install django=version`

- **Create DJANGO Project**
  > `django-admin startproject name-of-project`
- **Create DJANGO App**

  > `django-admin startproject name-of-app`

- **Start DJANGO Server**

  > `python manage.py runserver`

- **Migration**

  > `python manage.py makemigrations`

  > `python manage.py migrate`

- **Enter Pthon Shell**

  - Get in shell

    > `python manage.py shell`

  - Import Model in Shell
    > `from model_name.models import Model_Class_Name`
  - See all Object in class
    > `Model_Class_Name.objects.all()`
  - See all Object in class
    > `Model_Class_Name.objects.create(title='titles')`

## Notes

If `blank = False` means field is required on costumer view and if `null = False` means database needs some data.
blank deals with userside.
null deals with database i.e sqlite.
