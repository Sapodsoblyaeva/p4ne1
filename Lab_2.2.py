import paramiko
from time import sleep
ssh_connection = paramiko.SSHClient()
ssh_connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_connection.connect(
    "10.31.70.209",
    username="mk",
    password="q1q1q1",
    look_for_keys=False,
    allow_agent=False
)
session = ssh_connection.invoke_shell()

session.send('\n\n\nterminal length 0\n\n')
sleep(2)
session.send('\n\n\nshow interface | i packets \n\n')
while True:
    sleep(1)
    s = session.recv(1024)
    if not s:
        break
    print(s.decode())
