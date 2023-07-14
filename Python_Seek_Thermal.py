import time
import cv2
import paramiko

username = 'youbot' # хост робота
password = '111111' # пароль
output_path = f'/home/{username}/catkin_ws/src/seek_thermal_s/build/examples/'
output_file = 'output.jpg'
command = './seek_viewer --colormap=2 --rotate=90'
hostname = '192.168.88.22'
port = 22

# Запуск тепловизора на роботе seektermal
def run_thermal_camera(ssh):
    ssh.send(command.encode('utf-8') + b'\n')
    time.sleep(2.2)
    exit_string = ssh.recv(10000).decode('utf-8')
    time.sleep(1)
    while 'Error: LIBUSB_ERROR_TIMEOUT' in exit_string or 'LIBUSB_ERROR_PIPE' in exit_string or \
            'No such file or directory' in exit_string:
        ssh.send(command.encode('utf-8') + b'\n')
        time.sleep(2.2)
        exit_string = ssh.recv(10000).decode('utf-8')

# Получение и вывод изображения с тепловизора
def sshpt(sftp_client):
    status = True
    while status:
        sftp_client.get(output_path + output_file, output_file)
        time.sleep(0.01)

        img = cv2.imread(output_file)
        if isinstance(img, type(None)) or not status:
            continue

        cv2.imshow('HeatMapp', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            status = False

def connect():
    with paramiko.SSHClient() as client:
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.load_system_host_keys()
        client.connect(hostname, port, username, password)
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        sftp_client = client.open_sftp()
        ssh = client.invoke_shell()
        ssh.send(b'sudo -s' + b'\n')
        time.sleep(1)
        ssh.send(b'111111' + b'\n')
        time.sleep(1)
        ssh.send(b'cd catkin_ws/src/seek_thermal_s/build/examples/' + b'\n')

        time.sleep(1)
        run_thermal_camera(ssh)
        time.sleep(1)

        sshpt(sftp_client)
        client.close()


connect()