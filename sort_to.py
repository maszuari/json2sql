class SortTO:

    def __init__(self, key, type, target_fields, shared_fields_str):
        self.key = key
        self.type = type
        self.target_fields = target_fields
        self.shared_fields_str = shared_fields_str
    
    def set_from_table(self, edge_from):
        self.from_table = edge_from

    def __str__(self):
        fields_str = ''
        for field in self.target_fields:
            if field != self.target_fields[-1]:
               fields_str += f"`{field['target']}` {field['order']}, "
            else:
               fields_str += f"`{field['target']}` {field['order']}" 

        return f"{self.key} as (SELECT {self.shared_fields_str} FROM `{self.from_table}` ORDER BY {fields_str})"

    