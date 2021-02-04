import ipywidgets as widgets
from ipywidgets import Widget
from PrototypeWidgets import DropdownSelectionWidget, data_upload_widget



class SelectionWindow(Widget):
    def __init__(self, data_path, methods, method_parameters, tests, test_parameters, **kwargs):
        super().__init__(**kwargs)
        self.methods_widget = DropdownSelectionWidget(methods, methods[0], "Methods:",
                                                      method_parameters)
        self.test_widget = DropdownSelectionWidget(tests, tests[0], "Tests:",
                                                   test_parameters)
        self.data_widget = data_upload_widget(data_path, "Data:")
        self.mask_widget = data_upload_widget(data_path, "Masks: ")
        self.accordion = widgets.Accordion(
            children=[self.data_widget, self.mask_widget, self.methods_widget.widget, self.test_widget.widget])
        self.accordion.set_title(2, 'Method')
        self.accordion.set_title(3, 'Test')
        self.accordion.set_title(0, 'Data')
        self.accordion.set_title(1, 'Mask')

    def get_current_values(self):
        return self.data_widget.value, self.mask_widget.value, self.methods_widget.get_value(), \
               self.test_widget.get_value(), self.methods_widget.get_parameter_values(), self.test_widget.get_parameter_values()
