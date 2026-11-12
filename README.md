# Ally Hamad Mpati — Portfolio

This is a Django 5.2.6 portfolio website with a dark editorial design, responsive navigation, project filtering, services, contact form, image uploads and Django admin support.

## Project location

The Django project is inside the `core` folder. Run commands from there because `manage.py` is located there.

## Windows setup

```powershell
cd D:\portfolio_project\core
& "C:\Users\mpati\AppData\Local\Programs\Python\Python313\python.exe" -m pip install -r requirements.txt
& "C:\Users\mpati\AppData\Local\Programs\Python\Python313\python.exe" manage.py migrate
& "C:\Users\mpati\AppData\Local\Programs\Python\Python313\python.exe" manage.py runserver
```

If `python` alone says that Python was not found, keep using the full Python path above until the Windows PATH is fixed.

## Admin

Open `http://127.0.0.1:8000/admin/` after creating an admin account:

```powershell
& "C:\Users\mpati\AppData\Local\Programs\Python\Python313\python.exe" manage.py createsuperuser
```

## Important

The contact form currently contains placeholder email settings. Replace `noreply@example.com` and `your-email@example.com` in `main/views.py` when you are ready to configure real email delivery.
