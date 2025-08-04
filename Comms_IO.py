#
# from Linux clone
#
import  serial.tools.list_ports

def get_coms_info():
    for port in serial.tools.list_ports.comports():
        print(port.manufacturer)
        print(port.name)
        print(port.vid)
        print(port.pid)
