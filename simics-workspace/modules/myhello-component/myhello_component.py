# MODULE: myhello-component
# COMPONENT: myhello_component

# empty_component.py - sample code for a Simics configuration component
# Use this file as a skeleton for your own component implementations.

from comp import *

class myhello_component(StandardConnectorComponent):
    """The empty component class."""
    _class_desc = "empty component"
    _help_categories = ()

    def setup(self):
        StandardConnectorComponent.setup(self)
        if not self.instantiated.val:
            self.add_objects()

    def add_objects(self):
        # TODO: replace the example pci-bus connector with relevant connectors
        self.add_connector('pci_bus', PciBusUpConnector(0, 'afdxES'))
        afdxES = self.add_pre_obj('afdxES', 'afdxES')
        afdxES2 = self.add_pre_obj('afdxES2', 'afdxES2')
        RDC = self.add_pre_obj('rtc_module', 'rtc_module')
        afdxES2.RDC = RDC
        RDC.ARINC664_2 = afdxES2
        RDC.LoadCfg = afdxES2
        afdxES.phyA = afdxES2
        afdxES2.phyA = afdxES
        afdxES.phyB = afdxES2
        afdxES2.phyB = afdxES
        afdxES.config_mac_mode = afdxES2
        #afdxES.mode = 1
		
    class component_connector(Interface):
        def get_check_data(self, cnt):
            return []
        def get_connect_data(self, cnt):
            return [[[0, self._up.get_slot('afdxES')]]]
        def check(self, cnt, attr):
            return True
        def connect(self, cnt, attr):
            self._up.get_slot('afdxES').pci_bus = attr[1]
        def disconnect(self, cnt):
            self._up.get_slot('afdxES').pci_bus = None

   