from page.login_page import LoginPage
from utils.data_reader import read_user_csv
import pytest
from utils.logger import logger

@pytest.mark.parametrize("user",read_user_csv())
def test_login(driver,user):
    logger.info("Iniciando test_login_cvs")
    login_page = LoginPage(driver)

    logger.info("Ejecutando login con credenciales de users.csv")
    login_page.login(user["username"],user["password"])

    if user["valid"]=="true":
        logger.info("Caso esperado: login correcto")
        assert "/inventory.html" in driver.current_url, "No se redirigió al inventario"
        logger.info("Inicio correcto de sesion")
    else:
        logger.info("Caso esperado: login invalido")
        error = login_page.get_error_message()
        assert "Epic sadface" in error
        logger.info("Inicio de sesion rechazado")