from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from page.inventory_page import InventoryPage
from page.login_page import LoginPage
from utils.logger import logger


def test_inventory_title(driver_logged):
    logger.info("Iniciando test_inventory_title")
    inventory_page = InventoryPage(driver_logged)

    titulo = inventory_page.obtener_titulo()
    logger.info("Obtenido titulo")
    assert titulo == "Swag Labs", "El titulo de la pagina es incorrecto"
    logger.info("Validacion correcta de prueba test_inventory_title")

def test_productos_visibles(driver_logged):
    logger.info("Iniciando test_productos_visibles")
    inventory_page = InventoryPage(driver_logged)

    productos = inventory_page.obtener_productos()
    logger.info("Contaje productos visibles")
    assert len(productos) > 0
    logger.info("Validacion correcta de prueba test_productos_visibles")

def test_ui_elements(driver_logged):
    logger.info("Iniciando test_ui_elements")
    inventory_page = InventoryPage(driver_logged)
    
    assert inventory_page.menu_visible(), "El menu no esta presente en la pagina"
    logger.info("Validacion correcta de prueba menu_visible")

    assert inventory_page.filtro_visible(), "El filtro no esta presente en la pagina"
    logger.info("Validacion correcta de prueba filtro_visible")