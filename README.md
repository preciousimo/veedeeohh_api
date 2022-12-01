# Veedeeohh API

## Installation

1. Clone the repo
```bash
git clone https://github.com/preciousimo/veedeeohh_api.git
```

2. Move into the directory where we have the project files
```bash
cd veedeeohh_api
```

3. Create a virtual environment :
```bash
virtualenv envname
```

4. Activate the virtual environment :
```bash
envname\Scripts\activate
```

5. Install the requirements :
```bash
pip install -r requirements.txt
```

6. Migrate Database
```bash
python manage.py migrate
```

7. Create Super User
```bash
python manage.py createsuperuser
```

8. To run the App, we use :
```bash
python manage.py runserver
```
⚠ Then, the development server will be started at http://127.0.0.1:8000/


## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## Contact

Precious Imoniakemu - [@preciousimo2](https://twitter.com/preciousimo2) - preciousimoniakemu@gmail.com

Project Link: [https://github.com/preciousimo/veedeeohh_api](https://github.com/preciousimo/veedeeohh_api)


## Acknowledgements
* [Django Docs](https://docs.djangoproject.com/en/4.1/)
* [DRF Docs](https://www.django-rest-framework.org/)
