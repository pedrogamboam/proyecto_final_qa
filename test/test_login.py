from page.login_page import LoginPage
from utils.logger import logger
import pytest

@pytest.mark.smoke
def test_login_ok(driver):
    logger.info("Inicializando driver test_login_ok")
    login_page = LoginPage(driver)

    logger.info("Ingreso de datos validos para ejecutar test")
    login_page.login("standard_user","secret_sauce")

    logger.info("Iniciando sesion")
    
    assert "/inventory.html" in driver.current_url, "No se redirigió al inventario"
    logger.info("Inicio correcto de sesion")


def test_login_invalid_password(driver):
    logger.info("Inicializando driver test_login_invalid_password")
    login_page = LoginPage(driver)

    logger.info("Ingreso de datos invalidos para ejecutar test")
    login_page.login("standard_user","123456") #se ingreso una contraseña invalida aleatorea

    error = login_page.get_error_message()


    assert "Epic sadface: Username and password do not match any user in this service" in error
    logger.info("Inicio de sesion rechazado")
    