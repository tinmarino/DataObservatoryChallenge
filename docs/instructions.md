    Instrucciones
    1 Problema de razonamiento
    2 Funciones y Clases
    3 Manipulación de datos

Prueba técnica Back End
Equipo DO
2023-02-22
Instrucciones

A continuación, se presentan 3 problemas que deberás resolver en un plazo de 6 horas desde que recibas el correo con estas instrucciones. No está contemplado que la prueba la resuelvas completamente, por lo que te recomendamos que te enfoques en lo que son tus fortalezas. Esta no es una prueba de velocidad y es mejor entregar buenas respuestas antes que responder toda la prueba.

La primera pregunta es de razonamiento y buscamos ver qué buena idea se te puede ocurrir para resolver un problema que por medio de fuerza bruta, requeriría demasiado poder de cómputo, pero que una aproximación inteligente podría resolver rápida y eficientemente.

La segunda pregunta es sobre funciones y clases, utilizando Programación Orientada a Objetos (OOP). Aquí buscamos ver qué tan claros están los conceptos de programación y algo muy importante para nosotros es revisar el orden con el que trabajas y como documentas el código.

La tercera corresponde a la manipulación de datos y aquí queremos ver cómo solucionarías el tener que trabajar con datos que no están del todo bien estructurados para luego ordenarlos y formatearlos de manera apropiada para consumirlos con posterioridad (¡algo que en el DO hacemos mucho!).

En algunas preguntas es mandatorio utilizar Python, pero en otras no es necesario, aunque si muy deseable dado que es el lenguaje principal que utilizamos en los desarrollos Back End en el DO, dentro de las herramientas de AWS (funciones Lambda principalmente).

Es esperable (¡y queremos que así sea!) que revises y uses toda clase de material disponible (como por ejemplo, StackOverflow), pero también esperamos que resuelvas estos problemas de manera individual y sin ayuda directa de otras personas (por ejemplo, preguntar en foros o a un colega).

¡Esperamos que pases un buen rato resolviendo este test!
Entrega de Resultados

Para entregar tus resultados tienes dos opciones:

    Enviarnos un archivo zip con tus respuestas al correo de reclutamiento del DO, recruiting@dataobservatory.net, con el asunto “Prueba técnica” seguido por su nombre (por ejemplo: Prueba técnica Juan Pérez).
    Crear un repositorio público donde nos compartas tus respuestas (github, gitlab, bitbucket, etc) y enviarlo al correo electrónico mencionado en el punto anterior con las mismas instrucciones para el nombre del asunto.

Cualquiera de ellas es igual de válida, usa la que más te acomode (¡pero debes usar solo una!).

En tu entrega, ten presente los siguientes puntos:

    Incluir todo el material generado (archivos .py, .ipynb u otros).
    Dividir el material generado por pregunta, idealmente carpetas. Por ejemplo, pregunta_1 y dentro incluir los archivos necesarios para correr el código y obtener la respuesta a la pregunta.
    Incluir un archivo de configuración de ambiente en el caso de ser necesario. Por ejemplo, en el caso de usar Python, incluir un archivo requirements con las librerías necesarias.
    Finalmente, sé lo más claro posible con tu ćodigo y realiza comentarios que expliquen las partes claves del mismo. Como lo describimos anteriormente, nos interesa no sólo la solución a la que llegues, también queremos saber como es tu razonamiento para resolver estos problemas.

1 Problema de razonamiento

Para esta pregunta, no es mandatorio usar Python, pero como te explicamos anteriormente es bastante deseable. Aquí tampoco es necesario usar OOP, pero lo puedes usar si es lo que más te acomoda.

El Registro Civil tiene una base de datos con todos los automóviles del país. Dicha base de datos tiene muchas transacciones al día y se está tornando un proceso lento y engorroso. Una de esas transacciones es justamente obtener la llave primaria según una patente dada, que después se utiliza para consultar otras bases de datos. Afortunadamente, quien diseñó la base de datos era una persona visionaria y lo hizo de tal forma, que hay una relación lógica entre el ID del registro (la llave primaria) y la patente a consultar, por lo cual no es realmente necesario consultar la base de datos para obtener este ID (y viceversa).

Para ello, necesitamos que crees funciones que nos permitan:

    Ingresar una patente y que la función retorne el ID asociado.
    Ingresar el ID y que la función retorne la patente.

El dominio de las patentes corresponde a los siguientes: [AAAA000, AAAA001, ..., ZZZZ999], el ID es secuencial, comienza en 1, por lo que AAAA000 tiene ID=1, AAAA001 tiene ID=2, AAAB000 tiene el ID=1.001 y así sucesivamente. En el registro, no está incluida la letra Ñ.
BONUS

Si incluyes algo de testeo, para nosotros sería genial.
2 Funciones y Clases

Esta pregunta deberá ser resuelta utilzando Python y siguiendo lo máximo posible la guía de estilo de Google.

Usando la API de StarWars (https://swapi.dev/documentation), construir dos clases que permitan describir a personas y planetas.

    Url personas: https://swapi.dev/api/people
    Url planetas: https://swapi.dev/api/planets

Para las personas, los atributos principales son los siguientes:

    name (público).
    height (público).
    mass (privado).
    hair_color (privado).
    skin_color (privado).
    eye_color (privado).
    birth_year (privado).
    gender (público).
    homeworld (público).
    species (privado).
    vehicles (privado).
    starships (privado).
    url (público).

Para cada persona, se debe poder contar con una función que:

    Una función pública que permita calcular el IMC de cada persona: pesoaltura2

    (nos preocupa su salud).
    Una función pública que nos diga si la persona es humana o no.
    Una función pública que diga cuántos vehículos y naves tiene en total la persona.
    Una función pública que permita compararse con otra persona, y nos diga cuál de las dos tiene mayor edad. tip: no tienes por qué saberlo, pero la fecha está con el sufijo BBY que significa Before Battle of Yavin (ABF para After Battle of Yavin), para que lo que tengas en consideración.
    Una función pública que nos devuelva el planeta de origen (bomeworld) como un objeto.

En el caso de los planetas, los atributos principales son los siguientes:

    name (público).
    rotation_period (público).
    orbital_period (público).
    diameter (privado).
    climate (público).
    gravity (público).
    terrain (público).
    surface_water (privado). Este es el porcentaje de su superficie que está cubierta por agua (0 a 100).
    population (privado).

Para cada planeta, se debe contar con una función que:

    Una función pública que permita calcular la superficie en kilómetros cuadrados (km2

    ).
    Una función pública que permita calcular la densidad poblacional (número de habitantes por kilómetro cuadrado).
    Una función pública que permita calcular cuántos kilómetros cuadrados están cubiertos por agua.
    Una función pública que permita calcular cuánta agua está disponible por habitante (kilómetros cuadrados de agua superficial por persona).

BONUS

Si incluyes alguna funcionalidad que lea directamente la API y genere los objetos necesarios, estaríamos encantados.
3 Manipulación de datos

Para esta pregunta no es mandatorio usar Python tampoco, pero como en las preguntas anteriores, también es recomendable. Por muy fácil y directa que sea la respuesta a algunas preguntas, todo debe ser realizado mediante código y quedar explicitado en el mismo.

Descargando el archivo csv, necesitamos en primera instancia, limpiar los datos y luego, transformar el formato y separar valores repetidos.

En este caso los datos son provenientes de un barco que hizo un viaje por año en tres ocasiones diferentes. Este barco se detiene algunas veces durante su trayecto a realizar estaciones, donde se lanza un ancla con sensores hasta alcanzar el lecho marino. Cada cierto intervalo de tiempo y profundidad, se hacen mediciones de algunas variables de interés. Mientras se realiza una estación, se asume que el barco no se mueve y que el tiempo es el mismo para cada una de las mediciones a diferentes profundidades (es decir, la fecha y hora de la medición 1, es la misma que la de la medición 200 para una misma estación).

Las variables medidas en cada estación son:

    Profundidad de la medición
    Fluorescencia
    Oxígeno disuelto
    Temperatura
    Salinidad

Ahora que ya tienes un poco de contexto, necesitamos que hagas lo siguiente:
3.1 Consolidación

Este paso debe tomar una base de datos sin depurar y entregar una tabla limpia, con todas las observaciones teniendo información relevante con nombres de columna y tipos de datos acordes. Para ello, siga los siguientes pasos:

    Al cargar los datos, elimina cualquier fila o columna que esté completamente sin datos. Si tiene al menos un valor válido en la fila/columna, no la elimines en este paso y vuelve a evaluar al final del ejercicio.
    Revisa que cada tipo de dato esté cargado correctamente. Si es númerico, que sea de esa forma, si es fecha, que sea de tipo de fecha, etc.
    Es posible que algunas filas tengan información parcialmente completa (tendrán valores válidos en algunas columnas, y en otras valores inválidos). Si esto sucede, rellena datos faltantes con la información de las filas superiores cuando sea necesario. Tip: recuerda que para una misma estación se asume que el tiempo no varía.
    Estandariza los nombres de las variables (nombre de las columnas):
        Todo debe estar con minúsculas
        Reemplaza los espacios por underscores (_).
        Reemplaza caracteres latinos y otros símbolos que no sean alfanuméricos o _-.
    Revise valores fuera de rango, si es que exisitieran. De existir datos que considere anómalos coméntalos brevemente, pero no es necesario que realices ninguna manipulación al respecto.

3.2 Reformateo

Ahora que la base de datos está limpia y ordenada, necesitamos optimizar un poco el formato en el que se encuentra.

En estos momentos la base de datos es un único consolidado con mucha información repetida. Te vamos a pedir que separes las tablas de manera que la información que se repite (la que identifica el barco y la estación), esté separada de las variables medidas (las 5 mencionadas inicialmente).

    Genera una tabla con los valores únicos que identifican cada barco y viaje. Cada viaje debe tener un id único. Esta tabla se llamará viajes.
    Genera una tabla con las mediciones, que no contenga información relacionada a los viajes a excepción del id de viaje. Esta tabla se llamará mediciones.
    Es muy importante que en ambas tablas exista un id que pueda relacionar ambas tablas. Este id puede ser de cualquier tipo (números, letras, símbolos o cualquier combinación de estas). Es decir, de la tabla viajes se establezca una relación uno es a muchos a la tabla mediciones.
    Finalmente, como es posible que en el futuro los datos vengan con más variables, transforma la tabla mediciones a formato largo. En concreto, hasta ahora esta tabla debiera tener 4 columnas de variables, más la columna de profundidad y la de id de viaje. Necesitamos que la tabla final quede con 4: id, profundidad, variable, valor. Ahora los registros en vez de ir hacia el lado quedan hacia abajo, permitiendo que si nuevas variables son añadidas, no es necesario cambiar la estructura de la tabla. La siguiente tabla es un ejemplo gráfico de lo que se busca, que es pasar de la tabla de la izquierda a la de la derecha:

id 	profundidad 	var1 	var2 	var3 	var4
1 	1.2 	1.67 	5.30 	0.37 	21.69
1 	2.4 	0.35 	5.88 	0.24 	2.67
2 	3.6 	0.92 	3.21 	0.19 	41.94
2 	4.8 	1.50 	3.14 	0.04 	7.25
3 	6.0 	1.65 	6.05 	0.53 	33.09
3 	7.2 	1.95 	5.58 	0.96 	42.50
id 	profundidad 	variable 	valor
1 	1.2 	var1 	1.67
1 	2.4 	var1 	0.35
2 	3.6 	var1 	0.92
2 	4.8 	var1 	1.50
3 	6.0 	var1 	1.65
3 	7.2 	var1 	1.95
1 	1.2 	var2 	5.30
1 	2.4 	var2 	5.88
2 	3.6 	var2 	3.21
2 	4.8 	var2 	3.14
3 	6.0 	var2 	6.05
3 	7.2 	var2 	5.58
1 	1.2 	var3 	0.37
1 	2.4 	var3 	0.24
2 	3.6 	var3 	0.19
2 	4.8 	var3 	0.04
3 	6.0 	var3 	0.53
3 	7.2 	var3 	0.96
1 	1.2 	var4 	21.69
1 	2.4 	var4 	2.67
2 	3.6 	var4 	41.94
2 	4.8 	var4 	7.25
3 	6.0 	var4 	33.09
3 	7.2 	var4 	42.50
3.3 ¿Qué dicen los datos?

Necesitamos generar algunos resúmenes de información, específicamente:

    ¿Qué crucero es el que tiene más datos?
    ¿En que hora del día se realizan más muestreos considerando los 3 años?
    Agrupando las profundidades cada 10 metros (de 0 a 10, >10 a 20 y así). ¿Cuál es el valor promedio para cada variable para cada uno de los 3 años y para cada uno de estas nuevas agrupaciones de profundidad?

¡¡¡Mucho éxito!!!
