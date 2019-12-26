# DJANGO VEHICLE APPLICATION
The instructions below assume that you have a django project already set up; and a python virtual environment already installed and activated. 

## styles
All ahlev-django applications are using styles from [mdbootstrap.com](https://mdbootstrap.com), so please make sure you install [ahlev-django-css-js](https://github.com/ohahlev/ahlev-django-css-js.git) first.

## install from this repository
### clone
```
git clone https://github.com/ohahlev/ahlev-django-vehicle.git
```

### go to directory ahlev-django-vehicle
```
cd ahlev-django-vehicle
```

### create installer package
```
python3 setup.py sdist
```

### go to project directory
```
pip install dist/ahlev-django-vehicle-0.0.1.tar.gz
```

## project configuration
### update settings.py as the following
```
INSTALLED_APPS = [
    'vehicle', # add this line
    ...
]
```

### add these lines to the end of settings.py if they don't exist yet
```
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]
#STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
MEDIA_URL = '/medias/'
```

## screenshots
### frontend: partial tag
![](screenshot/vehicle_frontend.png)

### backend: home page
![](screenshot/vehicle_backend1.png)

### backend: list all tags
![](screenshot/vehicle_backend2.png)

### backend: edit a tag
![](screenshot/vehicle_backend3.png)
