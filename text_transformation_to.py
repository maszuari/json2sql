class TextTransformationTO:

    def __init__(self, key, type, columns_list, fields):
        self.key = key
        self.type = type
        self.columns_list = columns_list
        self.fields = fields

    def set_from_table(self, edge_from):
        self.from_table = edge_from

    def __str__(self) -> str:
        fields_str = ""
        for col in self.columns_list:
            for fld in self.fields:
                if col['column'] == fld:
                    if fld != self.fields[-1]:
                        fields_str += f" {col['transformation']}(`{col['column']}`) as `{fld}`,"
                    else:
                        fields_str += f" {col['transformation']}(`{col['column']}`) as `{fld}`"
                else:
                    if fld != self.fields[-1]:
                        fields_str += f" `{fld}`,"
                    else:
                        fields_str += f" `{fld}`"

        return f"{self.key} as (SELECT {fields_str} FROM `{self.from_table}`  )" 