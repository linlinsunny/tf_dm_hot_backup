hardware setup

(YAMAHA TF,DM)

main mixer ipaddress:192.168.1.5

sync minxer ipaddress:192.168.1.6

software (tested in orangepi r1 lts)

sudo apt update

sudo apt install python3 python3-pip -y

chmod +x final.py

sudo nano /etc/systemd/system/final.service



[Unit]
Description=Final Python Script
After=network.target

[Service]
ExecStart=/usr/bin/python3 /home/orangepi/final.py
Restart=always
User=orangepi

WorkingDirectory=/home/orangepi
Environment=PYTHONUNBUFFERED=1

[Install]
WantedBy=multi-user.target



sudo systemctl daemon-reload

sudo systemctl enable final.service

sudo systemctl start final.service


check 


sudo systemctl status final.service


log


journalctl -u final.service -f
