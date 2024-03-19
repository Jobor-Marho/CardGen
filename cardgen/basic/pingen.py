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


    






