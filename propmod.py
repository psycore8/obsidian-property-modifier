import utils.obsidian
import utils.helper
import argparse
from configparser import ConfigParser
from os import path

Version = '0.1.3'

def main():
    nstate = utils.helper.nstate
    print(f'\n\n{nstate.HEADER}Obsidian Property Modifier{nstate.ENDC} {Version} by psycore8{nstate.ENDC}')
    print(f'{nstate.LINK}https://github.com/psycore8{nstate.ENDC}\n\n')
    parser = argparse.ArgumentParser(
        prog='Obsidian Property Modifier',
        description='Tool for mass manipulating Obsidian Properties',
        epilog='2024 @psycore8'
    )

    config = ConfigParser()
    print(f'{nstate.OKBLUE} Checking config file...')
    if path.exists('propmod.ini'):
        print(f'{nstate.OKGREEN} Config file found!')
        config.read('propmod.ini')
        working_directory = config.get('arguments','working_directory')
        print(f'{nstate.OKGREEN} Working directory set to {working_directory}')
    else:
        print(f'{nstate.FAIL} Config file not found, use {nstate.clGRAY}--work-dir{nstate.ENDC} as argument!')

    parser.add_argument('-m', '--modify', choices=['field', 'value'], help='add or modify property fields or values in a directory')
    parser.add_argument('-d' ,'--delete', action='store_true', help='delete properties in a directory')
    parser.add_argument('-dir', '--working-dir', required=False, help='the directory with the md files to process')
    parser.add_argument('-f', '--field', required=True, help='the property field is required for delete and modify')
    parser.add_argument('-n', '--new-field', help='modify the field name to this value')
    parser.add_argument('-t', '--type', choices=['bool', 'int', 'str', 'date', 'datetime'],
                        default='str',
                        help='data type for property field')
    parser.add_argument('-v', '--value', help='the property value is needed for add or mod')
    args = parser.parse_args()

    if working_directory == '':
        if args.working_dir != '':
            working_directory = args.working_dir
        else:
            print(f'{nstate.FAIL} No working directory specified, use a config file or try {nstate.clGRAY}--working-dir{nstate.ENDC} as argument')
            exit()
   
    if args.modify == 'value':
        if args.field != '' or args.value != '':
            FileList = utils.obsidian.Files.GetFilesInDirectory(f'{working_directory}\\*.md')
            for filename in FileList:
                print(f'{nstate.OKBLUE} processing {filename}')
                property_value = utils.obsidian.Properties.ConvertDataType(args.value, args.type)
                properties = utils.obsidian.Properties.ExtractProperties(filename)
                mod_properties = utils.obsidian.Properties.ModifyValue(properties, args.field, property_value)
                utils.obsidian.Properties.DumpProperties(filename, mod_properties)
            print(f'{nstate.OKGREEN} DONE!')
        else:
            print(f'{nstate.FAIL} please specify {nstate.clGRAY}--field{nstate.ENDC} and {nstate.clGRAY}--value{nstate.ENDC}')
            exit()
    elif args.modify == 'field':
        if args.field != '' and args.new_field != '':
            FileList = utils.obsidian.Files.GetFilesInDirectory(f'{working_directory}\\*.md')
            for filename in FileList:
                print(f'{nstate.OKBLUE} processing {filename}')
                properties = utils.obsidian.Properties.ExtractProperties(filename)
                mod_properties = utils.obsidian.Properties.ModifyField(properties, args.field, args.new_field)
                utils.obsidian.Properties.DumpProperties(filename, mod_properties)
            print(f'{nstate.OKGREEN} DONE!')
        else:
            print(f'{nstate.FAIL} please specify {nstate.clGRAY}--field{nstate.ENDC} and {nstate.clGRAY}--new-field{nstate.ENDC}')
            exit()
    elif args.delete:
        if args.field != '':
            FileList = utils.obsidian.Files.GetFilesInDirectory(f'{working_directory}\\*.md')
            for filename in FileList:
                print(f'{nstate.OKBLUE} processing {filename}')
                properties = utils.obsidian.Properties.ExtractProperties(filename)
                mod_properties = utils.obsidian.Properties.Delete(properties, args.field)
                utils.obsidian.Properties.DumpProperties(filename, mod_properties)
            print(f'{nstate.OKGREEN} DONE!')
        else:
            print(f'{nstate.FAIL} please specify {nstate.clGRAY}--field{nstate.ENDC}')
            exit()

if __name__ == '__main__':
    main()