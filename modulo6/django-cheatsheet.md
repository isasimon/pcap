### Crear proyecto

Activamos el entorno virtual donde tengamos instalado Django

	django-admin startproject mysite .
	
Crea una estructura del tipo 

	mysite
	├── manage.py
	└── mysite
	├── __init__.py
	├── settings.py
	├── urls.py
	└── wsgi.py

### Lanzar proyecto

	python manage.py runserver
	
Se publica en http://127.0.0:8000

### Crear apps

Una app es un paquete que contendrá *models, views, URLs templates* y otros ficheros en caso de necesitarlos
En este ejemplo crearemos unaapp para escribir y publicar posts en un blog

	cd mysite
	python manage.py startapp blog
	
Se crea una estructura del tipo

	mysite
	├── blog
	│ ├── __init__.py
	│ ├── admin.py
	│ ├── apps.py
	│ ├── migrations
	│ ├── models.py
	│ ├── tests.py
	│ └── views.py
	├── db.sqlite3
	├── manage.py
	└── mysite

En *app.py* tenemos la configuración específica de la app.
La carpeta *migrations* sincroniza los modelos y la base de datos.
*models.py* contiene los modelos.
Por defecto dentro del settings se configura una base de datos SQLite. La podemos editar, por ejemplo a MySql
	
	DATABASES = {
	    'default': {
		'ENGINE': 'django.db.backends.mysql',
		'HOST': 'localhost',
		'PORT': '3306',
		'USER': 'root',
		'PASSWORD': 'notSecureChangeMe',
		'NAME': 'blog'
	    }
	}
	
Conectamos la app al proyecto añadiendola al INSTALLED_APPS dentro de *settings.py*

	INSTALLED_APPS = [
		'blog.apps.BlogConfig', # < here
		'django.contrib.admin',
		'django.contrib.auth',
		'django.contrib.contenttypes',
		'django.contrib.sessions',
		'django.contrib.messages',
		'django.contrib.staticfiles',
	]
	
#### Configuración de las URLs

Añadimos los paths en *mysite/urls.py*

	from django.contrib import admin
	from django.urls import path
	import blog.views # < here
	urlpatterns = [
		path('', blog.views.home, name='home'), # < here
		path('admin/', admin.site.urls),
	]

path(url, view, path_name)

#### Creación de las views

Editamos *blog/view.py*

	from django.shortcuts import render
	def home(request): # < here
		return render(request, 'home.html')

Las views se encargan de recibir una request y devolver una response. En este caso devolveremos contenido HTML que se 
encuentra en el template *home.html*

#### Creación del template

Creamos un directorio para los templates en *mysite* y colocamos *home.html*

	mysite
	├── blog
	├── templates # < here
	│ └── home.html # < here
	├── db.sqlite3
	├── manage.py
	└── mysite

Añadimos la siguiente línea HTML

	<h1>Home</h1>
	
Indicamos en la variable DIRS del *settings.py* la ubicación de los templates

	TEMPLATES = [
		{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [os.path.join(BASE_DIR, 'templates')], # < here
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
				],
			},
		},
	]
	
DIRS contiene la lista de directorios donde buscar templates
APP_DIRS = True le indica al engine buscar templates también en aplicaciones instaladas, de esta forma podemos también
poner templates dentro de las carpetas de estas (ejemplo *mysite/blog/templates/blog*)

Si ahora abrimos http://127.0.0.1:8000 veremos el *Home*

### Templates

Los templates contienen el HTML y una sintaxis especial (con *tags* y *variables*) que describe la lógica de como se 
inserta el contenido. Los *tags* controlan la lógica y las *variables* son reemplazadas cuando se evalúa el template.

Ejemplo

	<div class="posts">
		{% for post in posts %}
			<div class="post">
			{{ post.title }}
			</div>
		{% endfor %}
	</div>
	
La salida de esto sería algo como

	<div class="posts">
		<div class="post">First blog post ...</div>
		<div class="post">Second ...</div>
		<div class="post">Third ...</div>
	</div>

**Tags syntax:** {% tag %}
**Variables syntax:** {{ variable }} # Accedemos a los atributos con **.**

Se pueden aplicar filtros a las variables usando un pipe **|**. Por ejemplo

	{{ post.title|truncatechars:10 }}
	
#### Herencia en los templates

Creamos un fichero *templates/base.html* con el siguiente contenido 


	<!doctype html>
	<html lang="en">
		<head>
			<meta charset="UTF-8">
			<title>Site</title>
		</head>
		<body>
			<ul class="menu">
			<li><a href="{% url 'home' %}">Home</a></li>
			</ul>
			{% block title %}{% endblock %}
			<p>{% block content %}Some default content{% endblock %}</p>
		</body>
	</html>


*base.html* será el template base a todos los posts del site
El tag **url** devuelve la view que machea con el view_name indicado. Así evitamos harcodear las URLs.
El tag **block** define un bloque que puede ser sobrescrito por otros templates.

Por ejemplo, sobrescribimos el título extediendo *base.html* desde *home.html*

	{% extends "base.html" %}
	{% block title %}<h1>Home</h1>{% endblock %}
	
### Statics files

#### Añadir CSS

Creamos el siguiente esquema de carpetas

	.
	├── blog
	├── db.sqlite3
	├── manage.py
	├── mysite
	├── static # < here
	│ └── css # < here
	│ └── base.css # < here
	└── templates
	
Añadimos código CSS en base.css

	.menu {
		list-style: none;
		padding-left: 0;
	}
	.menu > li {
		display: inline-block;
	}
	.menu > li > a {
		text-decoration: none;
		color: #000;
		margin: 0 0.3em;
	}
	.menu > li > a.active {
		padding-bottom: 0.3em;
		border-bottom: 2px solid #528DEA;
	}
	

Configuramos en *settings.py* anadiendo STATICSFILES_DIRS:

	STATIC_URL = '/static/'
	STATICFILES_DIRS = [ # < here
		os.path.join(BASE_DIR, 'static'),
	]

El módulo *django.contrib.staticfiles* se añade a INSTALLED_APPS y se pone DEBUG a True en *settings.py*

	DEBUG = True # < here
	INSTALLED_APPS = [
		'blog.apps.BlogConfig',
		'django.contrib.admin',
		'django.contrib.auth',
		'django.contrib.contenttypes',
		'django.contrib.sessions',
		'django.contrib.messages',
		'django.contrib.staticfiles', # < here
		'django.contrib.sites',
	]
	
ADVRTENCIA: esto solo en desarrollo

Añadimos el css en *template/base.html*

<!doctype html>
{% load static %} <!-- here -->
<html lang="en">
<head>
	<meta charset="UTF-8">
	<link rel="stylesheet"
		href="{% static 'css/base.css' %}"> <!-- here -->
	<title>Site</title>
</head>
<body>
...
</body>
</html>

### Models

#### Crear modelos

Los modelos describen la estructura y comportamiento de tus datos. Creamos la clase Post en *blogs/models.py*

	from django.db import models
	class Post(models.Model): # < here
		title = models.CharField(default='', max_length=255) # Campos de la BDD
		body = models.TextField(default='', blank=True)
		
		def __str__(self):
				return self.title
			
Registramos el modelo en *blog/admin.py*

	from django.contrib import admin
	from blog.models import Post # < here
	admin.site.register(Post) # < here
	
Aplicamos ahora los cambios en la base de datos usando el *manage.py*

	python manage.py makemigrations
	python manage.py migrate
	python manage.py createsuperuser
	
Entrando en http://127.0.0.1:8000/admin podemos ver el panel de administrador

#### Listar los posts

Editamos el fichero *blog.view.py* para obtener los posts del modelo y devolverlos al template

	from django.shortcuts import render
	from .models import Post # < here
	def home(request):
		posts = Post.objects.all() # < here
		return render(request, 'home.html',
									{'section': 'home',
									'posts': posts, # < here
									})
									
Desde los modelos se crea una API para interaccionar con la base de datos. Post.objects.all() devuelvve un *QuerySet* con todos los Posts. Pasamos el *QuerySet* al template mediante { 'posts': posts }

Editamos *templates/home.html* para introducir esta información

{% extends "base.html" %}
		{% block content %} <!-- here -->
			{% for post in posts %}
					{{ post.pk }} : {{ post }} <br>
		{% endfor %}
{% endblock %}

#### Crear un detail page en el blog

Metemos el siguiente fragmento de código en *blog/models.py*

	from django.db import models
	from django.urls import reverse # < here
	from django.utils.text import slugify # < here
	class Post(models.Model):
		title = models.CharField(default='', max_length=255)
		body = models.TextField(default='', blank=True)
		slug = models.SlugField(default='', blank=True, max_length=255) # < here
		def __str__(self):
			return self.title
		def save(self, *args, **kwargs): # < here
			self.slug = slugify(self.title)
			super().save(*args, **kwargs)
		def get_absolute_url(self): # < here
			return reverse('blog:detail', args=[str(self.slug)])
			
*Slug* es una forma legible para una URL. Ejemplo

	www.noticias.ltda/?p=8679
	www.noticias.ltda/esto-es-un-slug
	
Sobrescribimos el método *save* para aplicarle lógica antes de guardar.
El método get_absolute_url devuelve la URL canónica

Lanzamos las migraciones en el prompt

	python manage.py makemigrations
	python manage.py migrate
	
Creamos el fichero *blog/urls.py*

	from django.urls import path
	from . import views
	app_name = 'blog'
	urlpatterns = [
		path('<slug:slug>/', views.detail, name='detail'),
	]
	
app_name nos indica un namespace para las URLs de este fichero. Ahora podemos referenciar a la 
página de detail usando blog:detail (namespace:path)

Usamos <slug:slug> para machear los valores de la URL (se pueden usar diferentes tipos como por ejemplo <int:id>)

Añadimos ahora las URLs a mysite/urls.py

	from django.contrib import admin
	from django.urls import path, include # < here
	import blog.views
	urlpatterns = [
		path('', blog.views.home, name='home'),
		path('blog/', include('blog.urls')), # < here
		path('admin/', admin.site.urls),
	]

Usando include hacemos que todas las URLs dentro de blog vengan precedidas por blog/

Ahora añadimos la nueva funcionalidad *detail* en *blog/views.py*

	from django.shortcuts import render, get_object_or_404 # <  here
	from .models import Post
	def home(request):
		posts = Post.objects.all()
		return render(request, 'home.html',
									{'section': 'home',
									'posts': posts,
									})
	def detail(request, slug=None): # < here
		post = get_object_or_404(Post, slug=slug)
		return render(request, 'blog/detail.html',
									{'section': 'blog_detail',
									'post': post,
									})
									
Creamos el template de detail en *detail.html* con este contenido

	{% extends "base.html" %}
	{% block title %}{{ post }}{% endblock %}
	{% block content %}
		<p>{{ post.body }}</p>
	{% endblock %}

Y editamos el *home.html*

	{% extends "base.html" %}
	{% block content %}
		{% for post in posts %}
			<a href="{{ post.get_absolute_url }}"> <!-- here -->
				{{ post.pk }} : {{ post }}
			</a>
			<br>
		{% endfor %}
	{% endblock %}

### Ejercicio

Crea una web que pulsando un link te diga si hoy llueve o no.

Para hacer la llamada a la API del tiempo usaremos el módulo *requests*:
	https://requests.readthedocs.io/en/latest/
	
PLUS: cambia el link por un button













































































