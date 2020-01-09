# django_web

![Logo de django](https://gitlab.com/uploads/-/system/project/avatar/3692106/django.png "Django Logo")


## Resumen:
	Este repositorio sera el conjunto de los ejercicios django que me paresca que son ejercicios semi completos 
	que dan una idea de las cosas que se pueden hacer con **django** como framework para desarrollo de webs dinamicas.
	
## ¿Como se usa el repositorio?
	
	Como dije, va a haber varios ejercicios y lo mas probable es que utilice diferentes versiones de django y python
	por lo que en cada ejercicio van a estar presentes las versiones de python y de django utilizadas segun las librerias
	necesiten, ya que muchas librerias muchas veces no funcionan con las ultimas actualizaciones de python.
	
	Si utilizas anaconda es sencillo, creas un ambiente con conda con una version especifica de python y ya esta. 
	
## *Pasos*: 
-----------------------------------------------------------
1. Abris la terminal 

2. Buscas las versiones de python disponibles : *conda search python*

3. De la lista elegis una version y corres : conda install *python=numeroDeVersionQueQueres*

4. Despues, con esa version que elegiste creas el entorno
............................................................
* Otra forma mas resumida *
Abris el prompt de anaconda y creas el entorno con el comando

*conda create -n nombreDeEntorno python=numeroDeVersionQueQueres*
----------------------------------------------------------- 	

Lo mas seguro es que ponga un txt con los requerimientos de cada proyecto

-----------------------------------------------------------
## *Instalacion de django:*

Se instala usando pip => *pip install django=numeroDeVersion*
-----------------------------------------------------------

-----------------------------------------------------------
## *Instalacion de requirements.txt:*

*pip install -r requirements.txt* 
-----------------------------------------------------------

-----------------------------------------------------------
## *Instalacion de requirements.txt:*

Para correr el **localhost** y asi poder entender que hay en cada proyecto
Una vez instalado todo lo que tenias que instalar en las versiones adecuadas,
te paras en donde esta ubicado el archivo *manage.py* con el prompt con tu 
entorno activado y corres el comando:

*python manage.py runserver*

Y ahi esta, con eso podes ver lo que hay en cada proyecto, ya que la idea es
que son ejercicios por lo que no se van a subir a Host mas pro, no de prueba 
ni nada de eso.
-----------------------------------------------------------

En el caso que haya algun ejercicio que use bases de datos *postgresql* 
en ves de *sqlite* lo voy a especificar. Igual, es solo instalar postgres 
que ya de entrada te instala el pgAdmin que es donde se manipula toda la 
base de datos y se define el codigo **sql**. Y tenes que tener en cuenta 
que instalar postgre no basta tambien tenes que instalar *psycopg2*
que igual es sencillo, es solo instalar en el entorno que estes parado
*pip install psycopg2* y ya esta.


-----------------------------------------------------------
## Referencias de interes:

1. (*[ckEditor][1]*)

2. (*[Documentación de django][2]*)

3. (*[Documentación por version de Python][3]*)

4. (*[Crispy Forms][4]*)

5. **(Investigar esto)** (*[Sphinx: python documentation generator][5]*) 

6. **(Investigar esto)** (*[Heroku: Cloud Application Platform][6]*) 

7. (*[psycopg][7]*)
[1]: https://ckeditor.com
[2]: https://www.djangoproject.com
[3]: https://www.python.org/doc/versions/
[4]: https://django-crispy-forms.readthedocs.io/en/latest/
[5]: http://www.sphinx-doc.org/en/master/
[6]: https://www.heroku.com
[7]: http://initd.org/psycopg/docs/install.html