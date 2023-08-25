# SCYTHE CONTROL #

import nmap
import xml.etree.ElementTree
import time

def nmap_scan(argument, scan_type_name):
    try:
        host_address = input("Digite um válido host de IP\n" + ': ')
        if host_address == '':
            host_address = "0.0.0.0"
        
        range = input("Digite um range válido de Porta/Portas | Examplo: 0-1030 \n" + ': ')
        if range == '':
            range = "0-1030"
        
        print('Starting Scan')
        nm.scan(host_address, range, arguments=argument)
        time.sleep(3)
        for host in nm.all_hosts():
            if nm[host].state() == "down":
                print("Porta inativa ou não existe")
            else:
                print("Tipo do scan: " + scan_type_name)
                print('Host: ' + f'{host} | {nm[host].hostname()}')
                print('State: ' + f'{nm[host].state()}')
                for proto in nm[host].all_protocols():
                    lport = nm[host][proto].keys()
                    for port in lport:
                        state = nm[host][proto][port]['state']
                        service_name = nm[host][proto][port]['name']
                        print("[+] " + f'Port : {port}\t\t' + f'State : {state}\t\t' + f'Service : {service_name}')

    except xml.etree.ElementTree.ParseError:
        print("Erro de permissão")

    except nmap.PortScannerError:
        print("Erro de permissão")

def fingerprint_scan(argument):
    try:
        host_address = input("Digite um IP válido | Recomendado: 0.0.0.0\n" + ': ')
        if host_address == '':
            host_address = "0.0.0.0"
        
        fiware_range = "1026, 1883, 4041, 8666, 9001, 27017"
        fiware_ports = ["1026", "1883", "4041", "8666", "9001", "27017"]
        fiware_status = []
        nm.scan(host_address, fiware_range, arguments=argument)
        time.sleep(3)
        for host in nm.all_hosts():
            if nm[host].state() == "down":
                print("IP inativo ou não existe")
            else:
                for proto in nm[host].all_protocols():
                    lport = nm[host][proto].keys()
                    for port in lport:
                        state = nm[host][proto][port]['state']
                        service_name = nm[host][proto][port]['name']
                        if not port in fiware_ports and state == "open":
                            fiware_status.append(1)
                        else:
                            fiware_status.append(0)
                if not 0 in fiware_status:
                    return f"Host: {host} | FIWARE Detected on server"
    
    except xml.etree.ElementTree.ParseError:
        print("Erro de permissão")
        
    except nmap.PortScannerError:
        print("Erro de permissão")

nm = nmap.PortScanner()

while True:
    try:
        type_scan = int(input("Selecione uma opção:\n[1] TCP SYN scan\n[2] TCP connect scan\n[3] UDP scan\n[4] Fingerprint Analysis\n: "))
        
        if type_scan == 1:
            try:
                nmap_scan('-sS', 'TCP SYN scan')
            except:
                print("Erro inesperado")
        
        elif type_scan == 2:
            try:
                nmap_scan('-sT', 'TCP connect scan')
            except:
                print("Erro inesperado")
        
        elif type_scan == 3:
            try:
                nmap_scan('-sU', 'UDP scan')
            except:
                print("Erro inesperado")
        
        elif type_scan == 4:
            result = fingerprint_scan("")
            if result:
                with open("report.txt", "a") as report_file:
                    report_file.write("Fingerprint Analysis Report:\n")
                    report_file.write(result)
                    report_file.write("\n\n")
                    print("Relatório gerado e salvo em 'report.txt'")
        
        else:
            print("Opção não existente | Tente rodar com: 1, 2, 3, 4 or 5")

    except ValueError:
        print("Erro de valor | Tente rodar com: 1, 2, 3, 4 or 5")
