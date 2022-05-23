import json
from input_to import InputTO
from filter_to import FilterTO
from sort_to import SortTO
from text_transformation_to import TextTransformationTO
from output_to import OutputTO

def main():
    with open('request-data.json') as jfile:
        data = json.load(jfile)

        shared_fields_str = ''
        shared_fields_list = []
        sql_str = ''
        for node in data['nodes']:
            transform_obj = None
            if node['type'] == 'INPUT':
                transform_obj = InputTO(node['key'], node['type'], 
                node['transformObject']['tableName'], 
                node['transformObject']['fields'])
                shared_fields_str = transform_obj.get_shared_fields_str()
                shared_fields_list = node['transformObject']['fields']
            elif node['type'] == 'FILTER':
                transform_obj = FilterTO(node['key'], node['type'],
                node['transformObject']['variable_field_name'], 
                node['transformObject']['joinOperator'],
                node['transformObject']['operations'],
                shared_fields_str)
            elif node['type'] == 'SORT':
                transform_obj = SortTO(node['key'], node['type'],
                node['transformObject'],
                shared_fields_str)
            elif node['type'] == 'TEXT_TRANSFORMATION':
                transform_obj = TextTransformationTO(node['key'], node['type'],
                node['transformObject'],
                shared_fields_list)
            elif node['type'] == 'OUTPUT':
                transform_obj = OutputTO(node['key'], node['type'],
                node['transformObject']['limit'],
                node['transformObject']['offset'])
            
            for edge in data['edges']:
                if transform_obj and edge['to'] == transform_obj.key and transform_obj.type != 'INPUT':
                    transform_obj.set_from_table(edge['from'])
            
            if node != data['nodes'][-1]:
                sql_str += str(transform_obj)+","
            else:
                sql_str += str(transform_obj) 
            print(str(transform_obj))

        print(sql_str)
        if sql_str:
            with open('result.sql', 'w') as f:
                f.write(sql_str)


if __name__ == '__main__':
    main()