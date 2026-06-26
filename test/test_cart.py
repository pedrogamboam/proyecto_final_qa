import pytest
from page.login_page import LoginPage
from page.inventory_page import InventoryPage
from utils.logger import logger

@pytest.fixture
def driver_logged(driver):
    logger.info("Inicializando driver con datos validos para test_cart")
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    logger.info("Validacion correcta prueba driver_logged")
    return InventoryPage(driver)

def test_agregar_producto_al_carrito(driver_logged):
    logger.info("Iniciando test_agregar_producto_al_carrito")
    driver_logged.agregar_producto_al_carrito()
    logger.info("Producto agregado")
    contador = driver_logged.obtener_contador_carrito()
    assert contador == "1", "La cantidad de productos no se agregó correctamente"
    logger.info("Validacion correcta test_agregar_producto_al_carrito")

def test_nombre_primer_producto(driver_logged):
    logger.info("Iniciando test_nombre_primer_producto")
    nombre = driver_logged.obtener_nombre_primer_producto()
    logger.info("Ingresando Nombre del primer producto")
    assert nombre != "", "El nombre del primer producto no se obtuvo correctamente"
    logger.info("Validacion correcta test_nombre_primer_producto")

def test_ir_al_carrito(driver_logged):
    logger.info("Iniciando test_ir_al_carrito")
    driver_logged.ir_al_carrito()
    logger.info("Navegacion al carrito realizada")
    assert "/cart.html" in driver_logged.driver.current_url, "No se redirigió al carrito"
    # Línea anterior (causaba NoSuchElementException porque usaba el locator del inventario en el carrito):
    # cart_item = driver_logged.driver.find_element(*driver_logged.nombres_productos).text
    logger.info("Validacion correcta redireccion al carrito")

    nombre = driver_logged.obtener_nombre_primer_producto()
    logger.info("Obtenido Nombre de inventario")
    cart_item = driver_logged.obtener_nombre_primer_producto_carrito()
    logger.info("Obtenido Nombre de carrito")
    assert cart_item == nombre, "El producto agregado no coincide"
    logger.info("Validacion correcta test_carrito")
    
