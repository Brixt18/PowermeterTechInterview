# Tech Interview

Este proyecto es una API construida en [DJango](https://www.djangoproject.com/) para la entrevista ténica de Powermeter

## Endpoints
*  `GET /maximum-consumption/{id_light_meter}/` consumo máximo de un medidor de luz

* `GET /minimum-consumption/{id_light_meter}/` consumo mínimo de un medidor de luz

* `GET /total-consumption/{id_light_meter}/` consumo total de un medidor de luz

* `GET /average-consumption/{id_light_meter}/` consumo promedio de un medidor de luz

### Medidor de Luz

* `GET /light-meter/` lista con todos los medidores

* `POST /light-meter/` crear medidor
* * Parámetros: Enviar JSON: 
```Json
    {
        "name": "medidor x"
    }
```

* `DELETE /light-meter/{id}/` Eliminar medidor

* `PATCH /LIGHT-meter/{id}/` Actualizar datos de un medidor
* * los datos son filtrados, solo se actualizarán aquellos que sean válidos
* * Datos válidos:
```Json
    {
        "name": "medidor x actualizado"
    }
```

### Mediciones

* `GET /measure/` lista con todas las mediciones y sus medidores

* `POST /measure/` crear medición
* * Parámetros: Enviar JSON: 
```Json
    {
        "kwh": 3,
        "light_meter_id": 1
    }
```

* `DELETE /measure/{id}/` Eliminar medición

* `PATCH /measure/{id}/` Actualizar datos de una medición
* * los datos son filtrados, solo se actualizarán aquellos que sean válidos
* * Datos válidos:
```Json
    {
        "kwh": 3,
        "light_meter_id": 1
    }
```


En orden de mantener privacidad y no es relevante para probar este proyecto, no incluiré otros parámetros que me han sido asignados a seguir.

## Instalación

Clonar el proyecto como normalmente clonas un proyecto de github.

```
$ git clone https://github.com/Brixt18/PowermeterTechInterview
```
O descargando el archivo .zip del mismo.


## Requisitos
* [Python >= 3.7](https://www.python.org/downloads/release/python-370/)

## Dependencias
* Instalar usando pip
```
$ pip install -r requirements.txt
```
Incluye:
* [DJango](https://pypi.org/project/Django/)
* [DJango Rest Framework](https://www.django-rest-framework.org//)

## Cómo Usar

### Inicializar
Una vez instaladas todas las dependencias, ejecutar:
```
$ python manage.py runserver
```
Y la aplicación comenzará a ejectuar en entorno Local con el puerto 5000 (`localhost:8000`).

### En caso de errores:
En caso de no poder ejecutar la aplicación con el comando Python, intenté utilizar `$ python3 ...` o `$ python2 ..` etc, es decir: definir la versión. Esto suele suceder cuando hay varias versiones de python instaladas.