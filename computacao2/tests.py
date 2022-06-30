from django.test import TestCase

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.opera.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep

# Create your tests here.
class PlayerFormTest(LiveServerTestCase):

  def testform(self):
    selenium = webdriver.Edge(r'C:\bin\msedgedriver.exe')
    #Choose your url to visit
    selenium.get('http://127.0.0.1:8000/clientecad')
    #find the elements you need to submit form
    player_nome = selenium.find_element_by_id('id_nome')
    player_endereco = selenium.find_element_by_id('id_endereco')
    player_numero = selenium.find_element_by_id('id_numero')
    player_bairro = selenium.find_element_by_id('id_bairro')
    player_cidade = selenium.find_element_by_id('id_cidade')

    submit = selenium.find_element_by_id('submit_button')

    #populate the form with data
    player_nome.send_keys('Teste')
    player_endereco.send_keys('Rua 7')
    player_numero.send_keys('370')
    player_bairro.send_keys('VNE')
    player_cidade.send_keys('Eldorado')

    #submit form
    submit.send_keys(Keys.RETURN)
