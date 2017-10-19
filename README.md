# zabbixusbmon
Python Script to use a USB arcade controller to send data to a zabbix server.

While looking for a cheap solution to monitor several circuits for closed or open status I came across a USB arcade controller that had 12 buttons.  With a little help from the evdev and pyzabbix python modules this script sends data to a Zabbix server for logging.  In theory this could be used with door and window sensors although I haven't tested it yet. 

Requirements
   * USB Arcade Controller Board: https://www.amazon.com/gp/product/B01C5J5AJO
   * zabbix server to log data and send alerts.
   * Computer with Python3 and configured zabbix-agent, I used a raspberry pi 
   * evdev and pyzabbix python modules.






   


