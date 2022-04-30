from jnpr.junos import Device
from jnpr.junos.utils.config import Config

with Device(host='IP_HERE', user='USERNAME', passwd='PASSWORD') as srx1:
    with Config(srx1, mode="exclusive") as cu:
            cu.load(path="Configuration/confirm.conf", overwrite=True)
            cu.commit_check()
            print("Device configuration has been confirmed.")
            #