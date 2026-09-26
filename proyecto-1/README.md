# Proyecto 1 - User Settings

Este es mi primer proyecto de Python realizado como parte del curso de FreeCodeCamp.

## Descripción

El programa permite administrar diferentes configuraciones de usuario utilizando un diccionario.

Se pueden agregar, actualizar, eliminar y mostrar las configuraciones.

## Funciones

- `add_setting()` → Agrega una nueva configuración.
- `update_setting()` → Actualiza una configuración existente.
- `delete_setting()` → Elimina una configuración.
- `view_settings()` → Muestra las configuraciones actuales.

## Ejemplo

El programa puede trabajar con configuraciones como:

    test_settings = {
        "theme": "dark",
        "notifications": "enabled",
        "volume": "high"
    }

    print(view_settings(test_settings))

Resultado:

    Current User Settings:
    Theme: dark
    Notifications: enabled
    Volume: high

## Lo que practiqué

En este proyecto practiqué algunos conceptos básicos de Python, como:

- Funciones
- Diccionarios
- Tuplas
- Condicionales
- Bucles
- F-strings
- Métodos para trabajar con strings
- `update()` y `pop()`

También practiqué cómo dividir el programa en diferentes funciones para que cada una se encargue de una tarea.

## Curso

Proyecto realizado mientras estoy aprendiendo Python con FreeCodeCamp.
