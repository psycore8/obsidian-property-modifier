import glob, yaml

class Files:
    def GetFilesInDirectory(Directory):
        FileList = glob.glob(Directory)
        return FileList

class Properties:

    def ConvertDataType(input=any, data_type=str):
        if data_type == 'bool':
            if input == 'true':
                output = True
            else:
                output = False
        elif data_type == 'int':
            output = int(input)
        else:
            output = input
        return output

    def ExtractProperties(file_name):
        with open(file_name, 'r') as file:
            lines = file.readlines()
        between_section = False
        extracted_props = []
        for line in lines:
            if line.strip() == '---':
                between_section = not between_section
                continue
            if between_section:
                extracted_props.append(line)
            extracted_props_str = ''
        for line in extracted_props:
            extracted_props_str += line
        return extracted_props_str

    def DumpProperties(file_name, properties):
        with open(file_name, 'r') as file:
            lines = file.readlines()
        between_section = False
        changed_lines = []
        for line in lines:
            if line.strip() == '---':
                between_section = not between_section
                if not between_section:
                    changed_lines.extend('---\n')
                    changed_lines.extend(properties)
                    changed_lines.extend('---\n')
                continue
            if not between_section:
                changed_lines.append(line)
        with open(file_name, 'w') as file:
           file.writelines(changed_lines)
    
    def Delete(properties=str, property_name=str):
        data = yaml.safe_load(properties)
        data.pop(property_name)
        yaml_data = yaml.dump(data, default_flow_style=False)
        return yaml_data

    def ModifyValue(properties=str, property_name=str, property_value=any):
        data = yaml.safe_load(properties)
        data[property_name] = property_value
        yaml_data = yaml.dump(data, default_flow_style=False)
        return yaml_data
    
    def ModifyField(properties=str, property_name=str, property_new_name=any):
        data = yaml.safe_load(properties)
        if property_name in data:
            data[property_new_name] = data.pop(property_name)
        yaml_data = yaml.dump(data, default_flow_style=False)
        return yaml_data