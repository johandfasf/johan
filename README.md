# practica de creacion y sincronizacion de repositorios de git y github

## detaos del alumno

-Johan Martinez Estrella 
-2630378
-creacion y sincronizacion de respositorios con git y github

## Objetivo de la práctica

Aprender a crear un repositorio local utilizando Git, agregar archivos, realizar cambios mediante commits y vincular el repositorio local con GitHub para sincronizar información entre ambos.

## Descripción del procedimiento realizado

Durante la práctica se creó un repositorio local utilizando PowerShell y Git. 
Primero se creó una carpeta para el proyecto y se ingresó a ella mediante la terminal.

Después se inicializó el repositorio con Git, se creó el archivo README.md y se agregó al área de preparación. Posteriormente se realizó un commit para guardar los cambios.

Finalmente, el repositorio local se vinculó con un repositorio creado previamente en GitHub y se enviaron los archivos mediante git push.

## Comandos de Git utilizados

| Comando | Función |
|---|---|
| git init | Inicializa un nuevo repositorio Git en la carpeta actual. |
| git status | Muestra el estado actual del repositorio y los cambios realizados. |
| git add | Agrega archivos al área de preparación (staging). |
| git add -A | Agrega todos los archivos nuevos, modificados o eliminados al área de preparación. |
| git commit -m "mensaje" | Guarda los cambios preparados en el historial del repositorio. |
| git branch -M main | Cambia el nombre de la rama actual a main. |
| git remote add origin URL | Vincula el repositorio local con un repositorio remoto. |
| git remote -v | Muestra los repositorios remotos configurados. |
| git push -u origin main | Envía los cambios del repositorio local a GitHub. |
| git pull origin main | Descarga los cambios de GitHub y los integra en el repositorio local. |
| git clone URL | Crea una copia local de un repositorio existente en GitHub. |

## Creación del repositorio local

Para crear el repositorio local se utilizó PowerShell.

Primero se creó una carpeta para el proyecto:

powershell
mkdir practica-git-johan-martinez

desdes de inicializo el repositorio de git

``git init``

**Con este comando se creó la estructura necesaria para que Git pudiera controlar las versiones de los archivos del proyecto.
Posteriormente se creó el archivo README.md**

## vinculacion del repositorio local con Github

Primero se creó un repositorio en GitHub.
Después se vinculó el repositorio local con el repositorio remoto utilizando:

``git remote add origin URL_DEL_REPOSITORIO``

## Sincronización Local → GitHub
La sincronización de Local → GitHub permite enviar los cambios realizados en la computadora al repositorio remoto.
El procedimiento básico es:

* *git add -A
* *git commit -m "Descripción de los cambios"
* *git push

git add prepara los archivos, git commit guarda los cambios en el historial y git push envía esos cambios a GitHub.

## Sincronización GitHub → Local

La sincronización GitHub → Local permite descargar los cambios que existen en el repositorio remoto y que todavía no están en el repositorio local.

``git pull origin main``

Este comando descarga los cambios de GitHub y los integra en la copia local del proyecto.

## Descripción de los archivos contenidos en el repositorio

README.md

Contiene la información de la práctica, el objetivo, el procedimiento, los comandos utilizados y la conclusión.

## Conclusión 
Con esta práctica aprendí los conceptos básicos de Git y GitHub y comprendí la diferencia entre un repositorio local y uno remoto. También aprendí a crear un repositorio, agregar archivos, guardar cambios mediante commits y sincronizar la información con GitHub,
Además, comprendí que Git permite llevar un control de las diferentes versiones de un proyecto, mientras que GitHub permite almacenar y compartir el repositorio de manera remota. Los comandos git add, git commit, git push y git pull son fundamentales para trabajar y mantener sincronizado un proyecto.
