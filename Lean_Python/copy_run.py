import netmiko
import re
import time


# def cisco(ip, username, password):
device = {'device_type': 'cisco_nxos', #'cisco_ios_telnet',#
          'host': '10.1.4.207',
          'username': 'admin',
          'password': 'NetMo@303'
          }

net_connet = netmiko.ConnectHandler(**device)

#备份配置的思科类型'device_type': 'cisco_ios_telnet'
# command_copy = 'copy run tftp:'
# result = net_connet.send_command_timing(command_copy)
# if 'Address or name of remote host' in result:
#     print('1')
#     result += net_connet.send_command_timing('10.1.5.93')
# if 'filename' in result:
#     print('2')
#     result += net_connet.send_command('\n')


#备份配置的思科类型'device_type': 'cisco_nxos'

net_connet.send_command_timing('copy run tftp:')
net_connet.send_command_timing('\n')
net_connet.send_command_timing('management')
net_connet.send_command_timing('10.1.5.93')

# print(net_connet.send_command('show ip int brief vrf all'))
# result = net_connet.send_command_timing(command_copy)
# if 'filename' in result:
#     print('1')
#     result += net_connet.send_command_timing('\n')
# if 'vrf' in result:
#     print('2')
#     result += net_connet.send_command_timing('management')
# if 'tftp server' in result:
#     print('3')
#     result += net_connet.send_command('10.1.5.93')




# guesser = netmiko.SSHDetect(**device)
# net_connet.send_config_set()
# print(net_connet.send_command('show ip int brief vrf all'))
net_connet.disconnect()
#
