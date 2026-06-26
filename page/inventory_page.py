from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.titulo = (By.CLASS_NAME, "app_logo")
        self.productos = (By.CLASS_NAME, "inventory_item")
        self.menu = (By.ID, "react-burger-menu-btn")
        self.filtro = (By.CLASS_NAME, "product_sort_container")
        self.boton_agregar = (By.CLASS_NAME, "btn_inventory")
        self.contador_carrito = (By.CLASS_NAME, "shopping_cart_badge")
        self.nombres_productos = (By.CLASS_NAME, "inventory_item_name")
        self.nombres_carrito = (By.CSS_SELECTOR, "div.inventory_item_name")  # Locator específico para carrito
        self.carrito = (By.CLASS_NAME, "shopping_cart_link")

    def obtener_titulo(self):
        return self.driver.title

    def obtener_productos(self):
        return self.driver.find_elements(*self.productos)

    def menu_visible(self):
        return self.driver.find_element(*self.menu).is_displayed()

    def filtro_visible(self):
        return self.driver.find_element(*self.filtro).is_displayed()

    def agregar_producto_al_carrito(self):
        self.driver.find_elements(*self.boton_agregar)[0].click()

    def obtener_contador_carrito(self):
        return self.driver.find_element(*self.contador_carrito).text

    def obtener_nombre_primer_producto(self):
        productos = self.driver.find_elements(*self.nombres_productos)
        if productos:
            return productos[0].text
        return ""

    def obtener_nombre_primer_producto_carrito(self):
        productos = self.driver.find_elements(*self.nombres_carrito)
        if productos:
            return productos[0].text
        return ""

    def ir_al_carrito(self):
        self.driver.find_element(*self.carrito).click()

    def agregar_producto_por_nombre(self, nombre_producto_json):
        productos = self.driver.find_elements(*self.productos)

        for producto in productos:
            nombre = producto.find_element(*self.nombres_productos).text
            if nombre == nombre_producto_json:
                producto.find_element(*self.boton_agregar).click()
                break