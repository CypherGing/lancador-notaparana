from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

entidade_cnpj = '23.951.256/0001-80'
def main():
    # Informar CPF e Senha
    cpf = str(input('Digite o seu CPF: '))
    senha = str(input('Digite a sua senha: '))
    
    # Abrir Nota Paraná
    driver = webdriver.Chrome()
    driver.get(r"https://notaparana.pr.gov.br/nfprweb/DoacaoDocumentoFiscalCadastrar")
    
    sleep(3)
    # Campos de Login

    campo_cpf = driver.find_element(By.XPATH, '//*[@id="attribute"]')
    campo_senha = driver.find_element(By.XPATH, '//*[@id="password"]')

    # Fazer o login
    campo_cpf.send_keys(cpf)
    sleep(1)
    campo_senha.send_keys(senha)
    sleep(1)
    driver.find_element(By.XPATH, '/html/body/div/div/div[1]/form/div[4]/input').click()
    sleep(30)
    entidade = driver.find_element(By.XPATH, '//*[@id="cnpjEntidade"]')
    sleep(1)
    entidade.send_keys(entidade_cnpj)
    campo_chave_de_acesso = driver.find_element(By.XPATH, '//*[@id="chaveAcesso"]')
    chave_copiada = campo_chave_de_acesso.get_attribute('value')
    sleep(1)
    while True:
        if len(chave_copiada) > 20:
            driver.find_element(By.XPATH, '//*[@id="btnDoarDocumento"]').click()
            sleep(5)



main()
print('FIM')




