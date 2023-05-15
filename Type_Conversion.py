#!/usr/bin/python3
# -*- encoding: utf-8 -*-
import binascii
from struct import pack

string_type = "wangxiao"
byte_type = b"wangxiao"
byte_hex_type = b'\x00\xff\x03\xee\x02\x01'
hex_string = binascii.hexlify(byte_hex_type).decode('utf-8')

def mac_hex_to_str(addr):
    result = []
    str_mac = binascii.hexlify(addr).decode('utf-8')
    for i in range(0, len(str_mac), 2):
        result.append(str_mac[i:i + 2])
    str_mac = ':'.join(result)
    return str_mac

byte_info = string_type.encode('latin-1')
print(f"string类型:{string_type} 转换成byte类型:{byte_info}")

string_info = byte_type.decode('latin-1')
print(f"byte类型:{byte_type} 转换成string类型:{string_info}")

