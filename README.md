# PortScanner ( SCYTHE CONTROL  - Caio Vinícius -  Luana Bannwart - Henrique Koji - João Cristovão - Guilherme Cavalheiro  (RM99747 , RM97738 , RM98476 , RM97924 , RM98305 )
- Luana Bannwart 
- Henrique Koji
- João Cristovão 
- Guilherme Cavalheiro
- Caio Vinícius


> Descrição:
O Scythe Control é um script Python que permite realizar varreduras de rede utilizando a biblioteca nmap e gerar relatórios em um arquivo de texto. Ele oferece diferentes opções de varredura e análise de portas e serviços.



> Funcionalidades: 

- Varredura TCP SYN: Esta opção realiza uma varredura de portas usando o método TCP SYN.
- Varredura TCP Connect: Realiza uma varredura de portas usando o método TCP Connect.
- Varredura UDP: Executa uma varredura de portas UDP.
- Análise de Impressão Digital: Analisa a presença do serviço "FIWARE" nas portas especificadas.



  
> Requisitos
- Python 3.9.2 ou superior instalado.
- Biblioteca python-nmap instalada. Instale usando o comando: pip install python-nmap.



> Sistema Operacional
O script foi testado e desenvolvido no sistema operacional Windows.




> Uso:
Execute o script em seu ambiente Python.
Escolha uma opção de varredura no menu.
Siga as instruções para inserir o IP de destino e as portas.
O script exibirá informações sobre as portas e serviços encontrados.
Para a opção "Análise de Impressão Digital", o script verifica a presença do "FIWARE" nas portas definidas.
Se o "FIWARE" for detectado, um relatório será gerado e salvo em report.txt.
Notas
Certifique-se de ter permissões para realizar varreduras em redes e sistemas.
O arquivo de relatório é gerado na pasta do script.
O script pode ser interrompido pressionando Ctrl+C.

