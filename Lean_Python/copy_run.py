import netmiko
import re
import time
import datetime


# def cisco(ip, username, password):
device = {'device_type': 'cisco_nxos',#'cisco_ios_telnet'
          'host': '10.1.4.208',
          'username': 'admin',
          'password': 'NetMo@303'#,
          # 'secret': 'Nm@303'
          }

net_connet = netmiko.ConnectHandler(**device)

# net_connet.enable()

# #获取内存利用率
# mem = 'show processes memory'#'show system resources'
# show = net_connet.send_command(mem)
# number = re.findall(r'Processor Pool Total:\s+(\d+)\s+Used:\s+(\d+)\s+', show)
# percent = int((int(number[0][1]) / int(number[0][0]))*100)
# print(str(percent) + '%')





# 获取内存利用率
# show = net_connet.send_command('show processes memory')
# number = re.findall(r'System memory\s+:\s+(\d+)K\s+total,\s+(\d+)K\s+used', show)
# percent = int((int(number[0][1]) / int(number[0][0])) * 100)
# print(str(percent) + '%')


#查看CPU利用率
# cpu = 'show processes cpu'
# show_cpu = net_connet.send_command(cpu)
# return_cpu = show_cpu.split('\n')
# print(return_cpu[-19])
# cpu_num = re.findall(r'(\d)', return_cpu[-19])
# cpu_data = []
# for i in cpu_num:
#     cpu_data.append('×') if int(i) >= 7 else cpu_data.append('√')
# print(cpu_data)

# cpu_data = []
# for i in return_cpu:
#     print(i)
#     if 'five minutes' in i:
#         cpu_percent = re.findall(r'five minutes:\s+(\d+)%', i)
#         if int(cpu_percent[0]) < 70:
#             cpu_data.append('√')
#         else:
#             cpu_data.append('×')
# if '×' in cpu_data:
#     print('×')
# else:
#     print('√')


#查看接口是否有错误
# err_int = 'show interface status err-dis'
# show_err = net_connet.send_command(err_int)
# return_err = show_err.split('\n')
# print('√') if 'Port         Name               Status   Reason' == return_err[-3] else print('×')
# if show_err == '':
#     print('√')
# else:
#     print('×')



#查看power状态
# env_power = 'show environment status power'
# show_power = net_connet.send_command(env_power)
# return_power = show_power.split('\n')
# data_power = []
# for i in return_power:
#     if 'PWR-C49E-300AC' in i:
#         data_power.append('√') if 'good' in i else data_power.append('×')
# print('×') if '×' in data_power else print('√')


#查看fan状态
# env_fan = 'show environment status fan'
# show_fan = net_connet.send_command(env_fan)
# return_fan = show_fan.split('\n')
# data_fan = []
# for i in return_fan:
#     if 'Fan' in i:
#         if 'Good' in i:
#             data_fan.append('√')
#         else:
#             data_fan.append('×')
# if '×' in data_fan:
#     print('×')
# else:
#     print('√')



    # fan_data.append('√') if re.match(r'\w+-\d', i) is not None and 'ok' in i else fan_data.append('×')
# data.append('×') if '×' in fan_data else data.append('√')
# time.sleep(1)



#日志检查
# logging = 'show logging | in error'
# net_connet.enable()
# show_log = net_connet.send_command(logging)
# return_log = show_log.split('\n')
# for i in return_log:
#     if i == '':
#         print('√')
#     else:
#         print('×')




#备份配置的思科类型'device_type': 'cisco_ios_telnet'
# command_copy = 'copy run tftp:'
# result = net_connet.send_command_timing(command_copy)
# if 'Address or name of remote host' in result:
#     # print('1')
#     result += net_connet.send_command_timing('10.1.5.93')
# if 'filename' in result:
#     # print('2')
#     result += net_connet.send_command('\n')


#备份配置的思科类型'device_type': 'cisco_nxos'

# net_connet.send_command_timing('copy run tftp:')
# net_connet.send_command_timing('\n')
# net_connet.send_command_timing('management')
# net_connet.send_command_timing('10.1.5.93')

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




