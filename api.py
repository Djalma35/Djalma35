import requests
import os


def banner():
    print("""
███████╗██╗    ██╗███████╗███████╗████████╗               
██╔════╝██║    ██║██╔════╝██╔════╝╚══██╔══╝               
███████╗██║ █╗ ██║█████╗  █████╗     ██║                  
╚════██║██║███╗██║██╔══╝  ██╔══╝     ██║                  
███████║╚███╔███╔╝███████╗███████╗   ██║                  
╚══════╝ ╚══╝╚══╝ ╚══════╝╚══════╝   ╚═╝                  
                ██████╗  █████╗ ███╗   ██╗███████╗██╗     
                ██╔══██╗██╔══██╗████╗  ██║██╔════╝██║     
                ██████╔╝███████║██╔██╗ ██║█████╗  ██║     
                ██╔═══╝ ██╔══██║██║╚██╗██║██╔══╝  ██║     
                ██║     ██║  ██║██║ ╚████║███████╗███████╗
                ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝
    """)


def banner19():
    print("""\033[31m
███████╗██╗    ██╗███████╗███████╗████████╗               
██╔════╝██║    ██║██╔════╝██╔════╝╚══██╔══╝               
███████╗██║ █╗ ██║█████╗  █████╗     ██║                  
╚════██║██║███╗██║██╔══╝  ██╔══╝     ██║                  
███████║╚███╔███╔╝███████╗███████╗   ██║                  
╚══════╝ ╚══╝╚══╝ ╚══════╝╚══════╝   ╚═╝                  
                ██████╗  █████╗ ███╗   ██╗███████╗██╗     
                ██╔══██╗██╔══██╗████╗  ██║██╔════╝██║     
                ██████╔╝███████║██╔██╗ ██║█████╗  ██║     
                ██╔═══╝ ██╔══██║██║╚██╗██║██╔══╝  ██║     
                ██║     ██║  ██║██║ ╚████║███████╗███████╗
                ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝
    \033[0m""")


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def ip():
    banner()

    ip_input = input('Digite o IP para uma consulta: ')

    request = requests.get(
        'https://ipwhois.app/json/{}'.format(ip_input))

    ip_data = request.json()

    if 'message' not in ip_data:
        clear()
        banner()
        print("==> IP ENCONTRADO <==")

        print("IP: {}".format(ip_data['ip']))
        print("Tipo: {}".format(ip_data['type']))
        print("Continente: {}".format(ip_data['continent']))
        print("País: {}".format(ip_data['country']))
        print("Capital: {}".format(ip_data['country_capital']))
        print("Região: {}".format(ip_data['region']))
        print("Cidade: {}".format(ip_data['city']))
        print("Moeda: {}".format(ip_data['currency']))

    else:
        clear()
        print('{}: IP Invalido.'.format(ip_input))

    print('---------------------------------')
    option = int(
        input("""
Quer fazer uma nova consulta?

1. Sim
2. Sair
>>> """))
    if option == 1:
        clear()
        ip()

    elif option == 2:
        clear()
        banner()
        exit()

    else:
        clear()
        banner()
        print("Opção inválida.")


def ip2():
    banner()

    ip_input = input('Digite o IP para uma consulta: ')

    request = requests.get(
        'https://ipapi.co/{}/json'.format(ip_input))

    ip_data = request.json()

    if 'error' not in ip_data:
        clear()
        banner()
        print("==> IP ENCONTRADO <==")

        print("IP: {}".format(ip_data['ip']))
        print("Versão: {}".format(ip_data['version']))
        print("Cidade: {}".format(ip_data['city']))
        print("Região: {}".format(ip_data['region']))
        print("Código da Região: {}".format(ip_data['region_code']))
        print("Código do País: {}".format(ip_data['country_code']))
        print("Nome do País: {}".format(ip_data['country_name']))
        print("Capital do País: {}".format(ip_data['country_capital']))
        print("Código do Continente: {}".format(ip_data['continent_code']))
        print("Código postal: {}".format(ip_data['postal']))
        print("Latitude: {}".format(ip_data['latitude']))
        print("Longitude: {}".format(ip_data['postal']))
        print("Fuso horário: {}".format(ip_data['timezone']))
        print("Código de Chamada do País: {}".format(
            ip_data['country_calling_code']))
        print("Moeda: {}".format(ip_data['currency']))
        print("Nome da moeda: {}".format(ip_data['currency_name']))
        print("Área do País: {}".format(ip_data['country_area']))
        print("População do País: {}".format(ip_data['country_population']))
        print("ASN: {}".format(ip_data['asn']))
        print("ORG: {}".format(ip_data['org']))

    else:
        clear()
        print('{}: IP Invalido.'.format(ip_input))

    print('---------------------------------')
    option = int(
        input("""
Quer fazer uma nova consulta?

1. Sim
2. Sair
>>> """))
    if option == 1:
        clear()
        ip2()

    elif option == 2:
        clear()
        banner()
        exit()

    else:
        clear()
        banner()
        print("Opção inválida.")


def cep():
    banner()

    cep_input = input('Digite o CEP para a consulta: ')

    request = requests.get(
        'https://brasilapi.com.br/api/cep/v1/{}'.format(cep_input))

    address_data = request.json()

    if 'errors' not in address_data:
        clear()
        banner()
        print("==> CEP ENCONTRADO <==")

        print("CEP: {}".format(address_data['cep']))
        print("Estado: {}".format(address_data['state']))
        print("Cidade: {}".format(address_data['city']))
        print("Vizinhança: {}".format(address_data['neighborhood']))
        print("Rua: {}".format(address_data['street']))

    else:
        clear()
        print('{}: CEP inválido.'.format(cep_input))

    print('---------------------------------')
    option = int(
        input("""
Deseja realizar uma nova consulta ?

1. Sim
2. Sair
>>> """))
    if option == 1:
        clear()
        cep()

    elif option == 2:
        clear()
        banner()
        exit()

    else:
        clear()
        banner()
        print("Opção inválida.")

def cep2():
    banner()

    cep_input = input('Digite o CEP para a consulta: ')

    request = requests.get(
        'https://ws.apicep.com/cep.json?code={}'.format(cep_input))

    address_data = request.json()

    if 'message' not in address_data:
        clear()
        banner()
        print("==> CEP ENCONTRADO <==")

        print("CEP: {}".format(cep_input))
        print("Estado: {}".format(address_data['state']))
        print("Cidade: {}".format(address_data['city']))
        print("Distrito: {}".format(address_data['district']))
        print("Endereço: {}".format(address_data['address']))

    else:
        clear()
        print('{}: CEP inválido.'.format(cep_input))

    print('---------------------------------')
    option = int(
        input("""
Deseja realizar uma nova consulta ?

1. Sim
2. Sair
>>> """))
    if option == 1:
        clear()
        cep2()

    elif option == 2:
        clear()
        banner()
        exit()

    else:
        clear()
        banner()
        print("Opção inválida.")

def cnpj():
    banner()

    cpf_input = input('Digite o CPF para a consulta: ')

    request = requests.get(
        'https://tudosobretodos.info/$cpf'.format(cpf_input))

    cpf_data = request.json()

    if 'message' not in cpf_data:
        clear()
        banner()
        print("==> CPF ENCONTRADO <==")

        print("Sexo: {}".format(cpf_data['CPF']))
        print("Nascimento: {}".format(cpf_data['nome']))
        print("CPF: {}".format(cpf_data['cep']))
        print("Telefone: {}".format(cpf_data['telefone']))
        print("E-mail: {}".format(CPF_data['email']))
        print("Endereço: {}".format(cpf_data['situacao']))

    else:
        clear()
        print('{}: CPF inválido.'.format(cpf_input))

    print('---------------------------------')
    option = int(
        input("""
Deseja realizar uma nova consulta ?

1. Sim
2. Sair
>>> """))
    if option == 1:
        clear()
        cnpj()

    elif option == 2:
        clear()
        banner()
        exit()

    else:
        clear()
        banner()
        print("Opção inválida.")


def banks():
    banner()

    bank_input = input('Digite o Código bancário para a consulta: ')

    request = requests.get(
        'https://brasilapi.com.br/api/banks/v1/{}'.format(bank_input))

    bank_data = request.json()

    if 'message' not in bank_data:
        clear()
        banner()
        print("==> BANCO ENCONTRADO <==")

        print("Código bancário: {}".format(bank_data['code']))
        print("Nome: {}".format(bank_data['name']))
        print("Nome completo: {}".format(bank_data['fullName']))
        print("ISPB: {}".format(bank_data['ispb']))

    else:
        clear()
        print('{}: Código bancário inválido.'.format(bank_input))

    print('---------------------------------')
    option = int(
        input("""
Deseja realizar uma nova consulta ?

1. Sim
2. Sair
>>> """))
    if option == 1:
        clear()
        banks()

    elif option == 2:
        clear()
        banner()
        exit()

    else:
        clear()
        banner()
        print("Opção inválida.")


def covid19():

    banner19()

    covid19_input = input('Digite a UF para a consulta: ')

    request = requests.get(
        'https://covid19-brazil-api.now.sh/api/report/v1/brazil/uf/{}'.format(covid19_input))

    covid19_data = request.json()

    if 'error' not in covid19_data:
        clear()
        banner19()
        print("==> UF ENCONTRADA <==")

        print("Estado: {}".format(covid19_data['state']))
        print("UF: {}".format(covid19_data['uf']))
        print("Casos: {}".format(covid19_data['cases']))
        print("Mortes: {}".format(covid19_data['deaths']))
        print("Suspeitos: {}".format(covid19_data['suspects']))
        print("Recusados: {}".format(covid19_data['refuses']))

    else:
        clear()
        print('{}: UF inválida.'.format(covid19_input))

    print('---------------------------------')
    option = int(
        input("""
Deseja realizar uma nova consulta ?

1. Sim
2. Sair
>>> """))
    if option == 1:
        clear()
        covid19()

    elif option == 2:
        clear()
        banner19()
        exit()

    else:
        clear()
        banner19()
        print("Opção inválida.")


def whois():
    banner()

    ip_input = input('Digite o IP para uma consulta: ')

    request = requests.get(
        'http://ip-api.com/json/{}'.format(ip_input))

    ip_data = request.json()

    if 'message' not in ip_data:
        clear()
        banner()
        print("==> IP ENCONTRADO <==")

        print("IP: {}".format(ip_data['query']))
        print("País: {}".format(ip_data['country']))
        print("Código do país: {}".format(ip_data['countryCode']))
        print("Região: {}".format(ip_data['region']))
        print("Nome da Região: {}".format(ip_data['regionName']))
        print("Cidade: {}".format(ip_data['city']))
        print("Código postal: {}".format(ip_data['zip']))
        print("Lat: {}".format(ip_data['lat']))
        print("Lon: {}".format(ip_data['lon']))
        print("Fuso horário: {}".format(ip_data['timezone']))
        print("ISP: {}".format(ip_data['isp']))
        print("Org: {}".format(ip_data['org']))
        print("ASN: {}".format(ip_data['as']))

    else:
        clear()
        print('{}: IP Invalido.'.format(ip_input))

    print('---------------------------------')
    option = int(
        input("""
Quer fazer uma nova consulta?

1. Sim
2. Sair
>>> """))
    if option == 1:
        clear()
        whois()

    elif option == 2:
        clear()
        banner()
        exit()

    else:
        clear()
        banner()
        print("Opção inválida.")
