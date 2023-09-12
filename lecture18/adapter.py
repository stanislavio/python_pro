class OldElectricityOutlet:
    def connect(self):
        return "Connected using two-pin plug"


class NewDevice:
    def plug_in(self):
        return "Plugged in using three-pin plug"


class OutletAdapter:
    def __init__(self, new_device):
        self.new_device = new_device

    def connect(self):
        return self.new_device.plug_in()


old_outlet = OldElectricityOutlet()
new_device = NewDevice()

print(old_outlet.connect())

adapter = OutletAdapter(new_device)
print(adapter.connect())
