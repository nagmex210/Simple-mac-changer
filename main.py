import subprocess
import optparse
import re


print("started")


def get_uinpt():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--interface", dest="interface", help="interface to change!")
    parse_object.add_option("-m", "--mac", dest="mac_adress", help="new mac adress")

    (user_inputs, arguments) = parse_object.parse_args()

    return user_inputs


def change_mac_adress(ui, umadrs):
    subprocess.call(["ifconfig", ui, "down"])
    subprocess.call(["ifconfig", ui, "hw", "ether", umadrs])
    subprocess.call(["ifconfig", ui, "up"])

def control_new_mac(interface):
    ifconfig = subprocess.check_output(["ifconfig",interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig))
    if new_mac:
        return new_mac.group(0)
    else:
        return None


user_inputs = get_uinpt()
change_mac_adress(user_inputs.interface, user_inputs.mac_adress)
finalized_mac = control_new_mac(str(user_inputs.interface))

if finalized_mac == user_inputs.mac_adress:
    print("sucsess")
else:
    print("didnt changed")
