import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

class usarunitTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_select (self):
        driver= self.driver
        driver.get("https://pruebas-quejas.ine.mx/")
        time.sleep(3)

        login = self.driver.find_element(By.XPATH,"//*[@id='root']/section/header/section/div/div/button[2]/span[2]").click()
        #time.sleep(2)                                 
      
        #dropdown.find_element(By.XPATH, "//option[. = 'Audi']").click()
        #time.sleep(3)
        usuario =driver.find_element(By.ID, 'normal_login_user').send_keys("hazael.gaytan")
        password =driver.find_element(By.ID, 'normal_login_password').send_keys("password")
        time.sleep(2)
        aceptarbtn = self.driver.find_element(By.XPATH,"//*[@id='normal_login']/div[3]/div/div/div/div/button").click()
        time.sleep(10)
        valofcentral = self.driver.find_element(By.XPATH,"//*[@id='root']/section/main/section/div[2]/div/div/div/div/div/div[5]/div/div/div").click()
        
        time.sleep(5)
        regqueja = self.driver.find_element(By.XPATH,"//*[@id='root']/section/header/section/section/ul/li[5]").click()
        time.sleep(7)        
        self.driver.find_element(By.CSS_SELECTOR, ".ant-picker").click()
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(4) > .ant-picker-cell:nth-child(3) > .ant-picker-cell-inner").click()

        time.sleep(4)
        hecho = self.driver.find_element(By.ID, 'formInfoGral_hechoDenunciado').send_keys("Se presenta queja del Partido Acción nacional vs el Partido Político MORENA, Claudia Sheinbaum Pardo, Marcelo Luis Ebrard Casaubón, Ricardo Monreal Ávila, Manuel Velasco Coello y José Gerardo Rodolfo Fernández Noroña, derivado de la pinta de bardas, diversos espectaculares y lonas con frases como ES CLAUDIA, TODOS CON MOREAL, AHORA ES ADÁN AUGUSTO, CON MARCELO SÍ, LA CORCHOLATA VERDE MANUEL VELASCO MÉXICO NOS UNE PROYECTO DE NACIÓN colocadas en distintos puntos del Estado de San Luis Potosí, lo que a dicho del quejoso constituye actos anticipados de precampaña y campaña")
        time.sleep(2)
        
        cerarsesion = self.driver.find_element(By.XPATH,"//*[@id='root']/section/header/section/div/div/button[2]").click()

    def tearDown(self):
        self.driver.close()
 
if __name__ == '__main__':
    unittest.main()

