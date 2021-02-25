from selenium import webdriver #Importando webdriver
from selenium.webdriver.common.keys import Keys #Importando reconhecimendo de teclas
import time #Para setarmos um tempo de diferença entre cada ação, "humanizando" o bot.

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(executable_path=r'chromedriver.exe')

    def login(self):
        driver = self.driver #Passando a referência do Chrome via Selenium
        driver.get('https://www.instagram.com') #Utilizado para acessar algum site/link
        time.sleep(2)

        user_element = driver.find_element_by_xpath("//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)

        password_element = driver.find_element_by_xpath("//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        password_element.send_keys(Keys.RETURN)
        time.sleep(5)

    def followWithUsername(self, username):
        self.driver.get('https://www.instagram.com/' + username + '/')
        time.sleep(2)
        followButton = self.driver.find_element_by_css_selector('button')
        if (followButton.text == 'Seguir'):
            followButton.click()
            time.sleep(2)
        else:
            print("Você já está seguindo este usuário!!")

print('~~~ Bem vindo ao FollowInstagramBom!! ~~~')
username = input('Digite seu user: ')
password = input('Digite sua senha: ')
print('~~~ o Bot iniciará em instantes!! ~~~')

edBot = InstagramBot(username, password)
edBot.login()
edBot.followWithUsername('zacefron')
print('Zac Efron acaba de ser seguidor!!\n')
edBot.followWithUsername('tiagogreis')
print('Tiago Reis acaba de ser seguidor!!\n')
