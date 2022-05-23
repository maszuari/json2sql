class InputTO:
    shared_fields_str = ""

    def __init__(self, key, type, table_name, fields):
            self.key = key
            self.type = type
            self.table_name = table_name
            self.fields = fields

    def __str__(self):
        return f"WITH {self.key} as (SELECT {self.shared_fields_str} FROM `{self.table_name}`)"
 
    def get_shared_fields_str(self):
        for field in self.fields:
            if field != self.fields[-1]:
                self.shared_fields_str += f"`{field}`,"
            else:
                self.shared_fields_str += f"`{field}`"
        return self.shared_fields_str