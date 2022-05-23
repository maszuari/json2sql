class FilterTO:

    def __init__(self, key, type, variable_field_name, join_operator, operations, shared_fields_str):
        self.key = key
        self.type = type
        self.variable_field_name = variable_field_name
        self.join_operator = join_operator
        self.operations = operations
        self.shared_fields_str = shared_fields_str

    def set_from_table(self, edge_from):
        self.from_table = edge_from

    def __str__(self) -> str:
    
        co = ''
        if len(self.operations) == 1:
            op = self.operations[0]
            co = f"'{self.variable_field_name}' {op['operator']} {op['value']}"
        else:
            co = "" 
            for op in self.operations:
                if op != self.operations[-1]:
                    co = co + f"`{self.variable_field_name}` {op['operator']} {op['value']} {self.join_operator} "
                else:
                    co = co + f"`{self.variable_field_name}` {op['operator']} {op['value']}"

        return f"{self.key} as (SELECT {self.shared_fields_str} FROM `{self.from_table}` WHERE {co} )"