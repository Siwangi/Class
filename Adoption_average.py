class Store:
    def __init__(self, division_name, region_name, active_employee, inactive_employee):
        self.division_name = division_name
        self.region_name = region_name
        self.active_employee = active_employee
        self.inactive_employee = inactive_employee
        self.total = active_employee + inactive_employee


    def adoption_rate(self):




