class OutputTO:

    def __init__(self, key, type, limit, offset):
        self.key = key
        self.type = type
        self.limit = limit
        self.offset = offset

    def __str__(self) -> str:
        return f"{self.key} as (SELECT * FROM `{self.from_table}` limit {self.limit} offset {self.offset}) SELECT * FROM {self.key};"

    def set_from_table(self, edge_from):
        self.from_table = edge_from
        