# Doctor Hunt Project - Java & Groovy API

This project integrates **Java** and **Groovy** to develop the **Doctor Hunt Project APIs**, a system where patients can make appointments with doctors, maintain medical records, and receive diagnosis offers. It includes features like user authentication, doctor management, and appointment scheduling.

The application is built using **Spring Boot** for the backend, with **PostgreSQL** as the database. The project uses **DTO (Data Transfer Objects)** for managing data flow between layers, ensuring smooth communication between components.

## Project Overview

This project includes:

- **Patient Appointment Management**: Patients can book appointments with doctors.
- **Medical Records Management**: Store and manage patient medical records for ongoing and historical reference.
- **Doctor Diagnosis Offers**: Doctors can create and manage diagnostic tests offered to patients.
- **User Authentication**: Secure login and registration for both patients and doctors.
- **Spring Boot Backend**: RESTful APIs using Spring Boot framework to handle business logic and database interaction.
- **PostgreSQL Database**: Reliable relational database to store patient, doctor, appointment, and medical record data.
- **Groovy Scripting**: Groovy is used to dynamically script and enhance functionality, allowing quick changes or new features to be implemented easily.

## Features

- **User Authentication**: Patients and doctors can register, log in, and authenticate via JWT (JSON Web Tokens).
- **Appointment Booking**: Patients can view available doctors and book appointments based on time slots.
- **Medical Records**: Patients' medical records are stored securely, allowing doctors to add or view historical information.
- **Diagnosis Test Offers**: Doctors can add available diagnostic tests to their profiles for patients to select.
- **Spring Boot & PostgreSQL**: The project uses Spring Boot to create robust backend APIs and PostgreSQL for data persistence.
- **DTO (Data Transfer Objects)**: DTOs are used to transfer data between layers efficiently, ensuring proper structuring of API responses.



## Installation

1. Install Python and Django
Ensure you have Python installed on your system. You can check the version with:
python --version
If Django is not installed, install it using:
pip install django

2. Create a Django Project
To start a new Django project, use the following command:
django-admin startproject projectname
Navigate into the project directory:
cd projectname

3. Install Django REST Framework (DRF)
Next, install Django REST Framework by running:
pip install djangorestframework

4. Add DRF to INSTALLED_APPS
Once DRF is installed, open the settings.py file inside your project folder and add 'rest_framework' to the INSTALLED_APPS list.
Example:
INSTALLED_APPS = [ 'rest_framework', ]

5. Install Django CORS Headers (Optional)
If you want to allow Cross-Origin Resource Sharing (CORS) for your API, install django-cors-headers:
pip install django-cors-headers
Then, add it to INSTALLED_APPS and MIDDLEWARE in settings.py.
Example:
INSTALLED_APPS = [ 'corsheaders', ]
MIDDLEWARE = [ 'corsheaders.middleware.CorsMiddleware', ]

6. Create an App in Your Project
Create an app for your API:
python manage.py startapp api

7. Define a Model (Optional)
In the api/models.py file, define your models. For example, to create an Item model:
class Item(models.Model):
name = models.CharField(max_length=100)
description = models.TextField()
def __str__(self):
return self.name

8. Migrate the Database
Run migrations to create the necessary database tables:
python manage.py makemigrations
python manage.py migrate

9. Create a Serializer for Your Model
In the api/serializers.py file, create a serializer for your model. Example:
class ItemSerializer(serializers.ModelSerializer):
class Meta:
model = Item
fields = '__all__'

10. Create Views Using DRF
In the api/views.py file, create views for your API using DRF's viewsets:
class ItemViewSet(viewsets.ModelViewSet):
queryset = Item.objects.all()
serializer_class = ItemSerializer

11. Set Up URLs
Create the URLs for your API in api/urls.py:
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'items', ItemViewSet)
urlpatterns = [ path('', include(router.urls)), ]
Then, include these URLs in the main urls.py of your project:
urlpatterns = [ path('admin/', admin.site.urls), path('api/', include('api.urls')), ]

12. Run the Server
Now, you can run the development server to test your setup:
python manage.py runserver
Your API will be accessible at http://127.0.0.1:8000/api/items/.

13. Requirements File
To generate a requirements.txt file with the installed packages, use:
pip freeze > requirements.txt
This will list all installed packages like djangorestframework and django in the requirements.txt file.

Example requirements.txt
Here’s an example of a requirements.txt file:
Django==4.1.0
djangorestframework==3.14.0
django-cors-headers==3.10.0
You can install the dependencies on another system using:
pip install -r requirements.txt
## Project Structure

```
DOCTORHUNTDJANGO:.
├───.vscode
├───doctorhuntdjango
│   └───__pycache__
├───doctorhunt_app
│   ├───migrations
│   │   └───__pycache__
│   ├───models
│   │   └───__pycache__
│   ├───serializers
│   │   └───__pycache__
│   ├───static
│   │   ├───css
│   │   └───js
│   ├───templates
│   ├───tests
│   ├───urls
│   │   └───__pycache__
│   ├───utils
│   │   └───__pycache__
│   ├───views
│   │   └───__pycache__
│   └───__pycache__
└───env
    ├───Include
    ├───Lib
    │   └───site-packages
    │       ├───pip
    │       │   ├───_internal
    │       │   │   ├───cli
    │       │   │   │   └───__pycache__
    │       │   │   ├───commands
    │       │   │   │   └───__pycache__
    │       │   │   ├───distributions
    │       │   │   │   └───__pycache__
    │       │   │   ├───index
    │       │   │   │   └───__pycache__
    │       │   │   ├───locations
    │       │   │   │   └───__pycache__
    │       │   │   ├───metadata
    │       │   │   │   ├───importlib
    │       │   │   │   │   └───__pycache__
    │       │   │   │   └───__pycache__
    │       │   │   ├───models
    │       │   │   │   └───__pycache__
    │       │   │   ├───network
    │       │   │   │   └───__pycache__
    │       │   │   ├───operations
    │       │   │   │   ├───build
    │       │   │   │   │   └───__pycache__
    │       │   │   │   ├───install
    │       │   │   │   │   └───__pycache__
    │       │   │   │   └───__pycache__
    │       │   │   ├───req
    │       │   │   │   └───__pycache__
    │       │   │   ├───resolution
    │       │   │   │   ├───legacy
    │       │   │   │   │   └───__pycache__
    │       │   │   │   ├───resolvelib
    │       │   │   │   │   └───__pycache__
    │       │   │   │   └───__pycache__
    │       │   │   ├───utils
    │       │   │   │   └───__pycache__
    │       │   │   ├───vcs
    │       │   │   │   └───__pycache__
    │       │   │   └───__pycache__
    │       │   ├───_vendor
    │       │   │   ├───cachecontrol
    │       │   │   │   ├───caches
    │       │   │   │   │   └───__pycache__
    │       │   │   │   └───__pycache__
    │       │   │   ├───certifi
    │       │   │   │   └───__pycache__
    │       │   │   ├───distlib
    │       │   │   │   └───__pycache__
    │       │   │   ├───distro
    │       │   │   │   └───__pycache__
    │       │   │   ├───idna
    │       │   │   │   └───__pycache__
    │       │   │   ├───msgpack
    │       │   │   │   └───__pycache__
    │       │   │   ├───packaging
    │       │   │   │   └───__pycache__
    │       │   │   ├───pkg_resources
    │       │   │   │   └───__pycache__
    │       │   │   ├───platformdirs
    │       │   │   │   └───__pycache__
    │       │   │   ├───pygments
    │       │   │   │   ├───filters
    │       │   │   │   │   └───__pycache__
    │       │   │   │   ├───formatters
    │       │   │   │   │   └───__pycache__
    │       │   │   │   ├───lexers
    │       │   │   │   │   └───__pycache__
    │       │   │   │   ├───styles
    │       │   │   │   │   └───__pycache__
    │       │   │   │   └───__pycache__
    │       │   │   ├───pyproject_hooks
    │       │   │   │   ├───_in_process
    │       │   │   │   │   └───__pycache__
    │       │   │   │   └───__pycache__
    │       │   │   ├───requests
    │       │   │   │   └───__pycache__
    │       │   │   ├───resolvelib
    │       │   │   │   ├───compat
    │       │   │   │   │   └───__pycache__
    │       │   │   │   └───__pycache__
    │       │   │   ├───rich
    │       │   │   │   └───__pycache__
    │       │   │   ├───tomli
    │       │   │   │   └───__pycache__
    │       │   │   ├───truststore
    │       │   │   │   └───__pycache__
    │       │   │   ├───urllib3
    │       │   │   │   ├───contrib
    │       │   │   │   │   ├───_securetransport
    │       │   │   │   │   │   └───__pycache__
    │       │   │   │   │   └───__pycache__
    │       │   │   │   ├───packages
    │       │   │   │   │   ├───backports
    │       │   │   │   │   │   └───__pycache__
    │       │   │   │   │   └───__pycache__
    │       │   │   │   ├───util
    │       │   │   │   │   └───__pycache__
    │       │   │   │   └───__pycache__
    │       │   │   └───__pycache__
    │       │   └───__pycache__
    │       └───pip-24.3.1.dist-info
    └───Scripts


- **Main.java**: The entry point of the Java application.
- **Script.groovy**: A Groovy script for dynamic execution.
- **MainTest.java**: Java unit tests for the application.
- **ScriptTest.groovy**: Groovy unit tests for the Groovy scripts.

## How to Run

### Running the Java Application

To run the Java application:

```bash
mvn exec:java
```

Or, using Gradle:

```bash
gradle run
```

### Running the Groovy Script

If you want to run the Groovy script directly, execute:

```bash
groovy src/main/groovy/com/example/Script.groovy
```

Alternatively, if you want to run the Groovy code from within Java, you can use the GroovyShell class like this:

```java
import groovy.lang.GroovyShell;

public class Main {
    public static void main(String[] args) {
        GroovyShell shell = new GroovyShell();
        shell.evaluate(new File("src/main/groovy/com/example/Script.groovy"));
    }
}
```

## Testing

To run unit tests for Java:

```bash
mvn test
```

For Groovy tests:

```bash
groovy -cp src/test/groovy com.example.ScriptTest
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


