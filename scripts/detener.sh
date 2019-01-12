#!/bin/bash

kill -9 $(cat appid.pid) # Leemos el archivo appid.pi donde tenemos almacenado el pid con el que se ha iniciado gunicorn
                         # y matamos el proceso para parar su ejecución.