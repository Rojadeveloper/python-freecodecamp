# Proyecto 4 - Hash Table

Este es mi cuarto proyecto de Python realizado como parte del curso de FreeCodeCamp.

## Descripción

El programa implementa una tabla hash desde cero utilizando una clase de Python.

La tabla hash permite almacenar, buscar y eliminar pares clave-valor mediante una función hash que calcula la suma de los puntos de código Unicode de cada carácter de una cadena.

También permite manejar colisiones cuando diferentes claves producen el mismo valor hash.

## Funciones

La clase `HashTable` contiene los siguientes métodos:

- `hash()` → Calcula el valor hash de una cadena.
- `add()` → Agrega un par clave-valor a la tabla hash.
- `remove()` → Elimina una clave y su valor correspondiente.
- `lookup()` → Busca una clave y devuelve su valor.

## Ejemplo

El programa puede almacenar pares clave-valor como:

```python
ht = HashTable()

ht.add('golf', 'sport')
ht.add('dear', 'friend')
ht.add('read', 'book')

print(ht.collection)
```

Resultado:

```python
{
    424: {'golf': 'sport'},
    412: {
        'dear': 'friend',
        'read': 'book'
    }
}
```

También puede manejar colisiones. Por ejemplo, las claves `fcc` y `cfc` producen el mismo valor hash:

```python
ht.add('fcc', 'coding')
ht.add('cfc', 'chemical')

print(ht.collection[300])
```

Resultado:

```python
{
    'fcc': 'coding',
    'cfc': 'chemical'
}
```

## Lo que practiqué

En este proyecto practiqué algunos conceptos de Python, como:

- Programación orientada a objetos (POO).
- Clases y métodos.
- Diccionarios.
- Funciones hash.
- Puntos de código Unicode con `ord()`.
- Diccionarios anidados.
- Manejo de colisiones.
- Condicionales.
- Eliminación y búsqueda de elementos.

También aprendí cómo funciona una tabla hash y cómo manejar diferentes claves que producen el mismo valor hash.

## Curso

Proyecto realizado mientras estoy aprendiendo Python con FreeCodeCamp.
