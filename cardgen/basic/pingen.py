from datetime import datetime
import random


def genMtnEpin(msg:str, amount:int) -> list:
    msg_list = msg.split(' ')
    sale_list = [msg_list[item+1] for item in range(0, len(msg_list)) if msg_list[item] =='Sale:']
    serial_list = [msg_list[item+1] for item in range(0, len(msg_list)) if msg_list[item] =='Serial:']
    


    compiled_data = []
    for item in sale_list:
        compiled_data += [ {
            'pin': item,
            'serial': serial_list[sale_list.index(item)],
            'code': '*131*PIN#'
        }]
    return compiled_data


def genGloEpin(msg:str, amount:int) -> list:
    msg_list = msg.split(' ')
    pin_list = [msg_list[item+1] for item in range(0, len(msg_list)) if msg_list[item] == 'Pin']
    serial_list = [msg_list[item].split(':')[1] for item in range(0, len(msg_list)) if msg_list[item].startswith('Serial')]
    compiled_data = []
    for item in pin_list:
        compiled_data += [{
            'pin': item,
            'serial': serial_list[pin_list.index(item)],
            'code': '*203*3*PIN#'
        }]
    
    return compiled_data
    

def genAirtelEpin(msg:str, amount:int) -> str:
    pass

def gen9mobileEpin(msg:str, amount:int) -> str:
    pass





def genref() -> str:
    date = str(datetime.now()).split(' ')[0].split('-')[0]+str(datetime.now()).split(' ')[0].split('-')[1]+str(datetime.now()).split(' ')[0].split('-')[2]
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = [1,2,3,4,5,6,7,8,9,0]
    for _ in range(5):
        date += str(random.choice(letters))
        date += str(random.choice(numbers))
    return date


def genAuth() -> int:
    pin = ''
    numbers = ['1','2','3','4','5','6','7','8','9','0']
    for _ in range (8):
        pin += random.choice(numbers)
    return int(pin)


    



genGloEpin('Voucher Details: Amount: NGN 100.0 Serial:6900933204 Pin 1120465120065142 Expiry:23-03-2024 Ref:2024031619492747004024656 Dial *203*3*YOURPIN# to recharge. Voucher Details: Amount: NGN 100.0 Serial:9171139305 Pin 1100728888182374 Expiry:23-03-2024 Ref:2024031619471061602023354 Dial *203*3*YOURPIN# to recharge. Voucher Details: Amount: NGN 100.0 Serial:7037397933 Pin 1230427292154619 Expiry:23-03-2024 Ref:2024031619481101001024716 Dial *203*3*YOURPIN# to recharge. Voucher Details: Amount: NGN 100.0 Serial:8402750594 Pin 1100316141054676 Expiry:23-03-2024 Ref:2024031621574887803193897 Dial *203*3*YOURPIN# to recharge. Voucher Details: Amount: NGN 100.0 Serial:4066169216 Pin 1100370301375777 Expiry:24-03-2024 Ref:2024031710311177403370185 Dial *203*3*YOURPIN# to recharge. Voucher Details: Amount: NGN 100.0 Serial:8281880611 Pin 1120427364941886 Expiry:24-03-2024 Ref:2024031710315595204272002 Dial *203*3*YOURPIN# to recharge. Voucher Details: Amount: NGN 100.0 Serial:7695811805 Pin 1231065510142513 Expiry:24-03-2024 Ref:2024031710323473805272314 Dial *203*3*YOURPIN# to recharge. Voucher Details: Amount: NGN 100.0 Serial:6067982769 Pin 1230456740139498 Expiry:24-03-2024 Ref:2024031710331887901273418 Dial *203*3*YOURPIN# to recharge. Voucher Details: Amount: NGN 100.0 Serial:9898986777 Pin 1100764769043471 Expiry:24-03-2024 Ref:2024031710335526702272914 Dial *203*3*YOURPIN# to recharge. Voucher Details: Amount: NGN 100.0 Serial:4126073790 Pin 1230444355137707 Expiry:24-03-2024 Ref:2024031710343226706273086 Dial *203*3*YOURPIN# to recharge.', 100)


