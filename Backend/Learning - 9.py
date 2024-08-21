import usb.core
import usb.util

# Barcha USB qurilmalarni aniqlash
devices = usb.core.find(find_all=True)

# Qurilmalarni ro'yxatlash
for device in devices:
    print(f"ID: {device.idVendor}:{device.idProduct}")
    print(f"Manufacturer: {usb.util.get_string(device, device.iManufacturer)}")
    print(f"Product: {usb.util.get_string(device, device.iProduct)}\n")
