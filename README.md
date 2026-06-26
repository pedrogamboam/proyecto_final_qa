\# Proyecto Final - QA Automation Testing

Pedro Gamboa

26 Junio 2026



\## Propósito

Este proyecto automatiza pruebas funcionales de la aplicación \[SauceDemo](https://www.saucedemo.com) utilizando \*\*Selenium WebDriver\*\* y \*\*Pytest\*\*.

El objetivo es validar el flujo de login, navegación de productos y proceso de compra, asegurando calidad y confiabilidad en la aplicación.



\## Tecnologías utilizadas

\- Python 3.13

\- Selenium WebDriver 4.43.0

\- Pytest 9.0.2

\- Pytest-HTML 4.2.0 (reportes)

\- Git y GitHub

\- Pytest Check 2.8.0

\- Behave 1.3.3



\## Instalación

1\. Clonar el repositorio:

&#x20;  ```bash

&#x20;  https://github.com/pedrogamboam/proyecto-final-automation-testing-pedro-gamboa



\## Estructura del proyecto



proyecto\_final\_qa/

data/            	Datos externos para pruebas

features/        	Escenarios BDD

logs/            	Archivos de ejecución

page/            	Page Objects

reports/         	Reportes HTML y capturas

test/            	Casos de prueba con Pytest

utils/           	Funciones auxiliares

conftest.py      	Configuración global de Pytest

pytest.ini       	Configuración de ejecución

requirements.txt

README.md



\## Ejecución de pruebas



Desde consola

Ejecutar los tests manualmente con el siguiente comando:

py -m pytest 



Desde GitHub Actions

Cada push a la rama main, GitHub Actions ejecutará automáticamente el workflow definido en .github/workflows/tests.yml.



