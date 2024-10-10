import utils.obsidian
import utils.helper
import argparse

Version = '0.1.1'

def main():
    nstate = utils.helper.nstate
    print(f'{nstate.HEADER}Obsidian Property Modifier {Version} by psycore8{nstate.ENDC}')
    parser = argparse.ArgumentParser(
        prog='Obsidian Property Modifier',
        description='Tool for mass manipulating Obsidian Properties',
        epilog='2024 @psycore8'
    )
    parser.add_argument('-m', '--modify', choices=['field', 'value'], help='add or modify property fields or values in a directory')
    parser.add_argument('-d', '--delete', action='store_true', help='delete properties in a directory')
    parser.add_argument('-wd', '--working-dir', required=True, help='the directory with the md files to process')
    parser.add_argument('-pf', '--prop-field', required=True, help='the property field is required for delete and modify')
    parser.add_argument('-nf', '--new-field', help='modify the field name to this value')
    parser.add_argument('-pv', '--prop-value', help='the property value is needed for add or mod')
    args = parser.parse_args()
    if args.modify == 'value':
        if args.prop_field != '' and args.prop_value != '':
            FileList = utils.obsidian.Files.GetFilesInDirectory(f'{args.working_dir}\\*.md')
            for filename in FileList:
                print(f'{nstate.OKBLUE} processing {filename}')
                properties = utils.obsidian.Properties.ExtractProperties(filename)
                mod_properties = utils.obsidian.Properties.ModifyValue(properties, args.prop_field, args.prop_value)
                utils.obsidian.Properties.DumpProperties(filename, mod_properties)
                print(f'{nstate.OKGREEN} DONE!')
        else:
            print(f'{nstate.FAIL} please specify --prop-field and --prop-value')
            exit()
    elif args.modify == 'field':
        if args.prop_field != '' and args.new_field != '':
            FileList = utils.obsidian.Files.GetFilesInDirectory(f'{args.working_dir}\\*.md')
            for filename in FileList:
                print(f'{nstate.OKBLUE} processing {filename}')
                properties = utils.obsidian.Properties.ExtractProperties(filename)
                mod_properties = utils.obsidian.Properties.ModifyField(properties, args.prop_field, args.new_field)
                utils.obsidian.Properties.DumpProperties(filename, mod_properties)
                print(f'{nstate.OKGREEN} DONE!')
        else:
            print(f'{nstate.FAIL} please specify --prop-field and --new-field')
            exit()
    elif args.delete:
        if args.prop_field != '':
            FileList = utils.obsidian.Files.GetFilesInDirectory(f'{args.working_dir}\\*.md')
            for filename in FileList:
                print(f'{nstate.OKBLUE} processing {filename}')
                properties = utils.obsidian.Properties.ExtractProperties(filename)
                mod_properties = utils.obsidian.Properties.Delete(properties, args.prop_field)
                utils.obsidian.Properties.DumpProperties(filename, mod_properties)
                print(f'{nstate.OKGREEN} DONE!')
        else:
            print(f'{nstate.FAIL} please specify --prop-field')
            exit()

if __name__ == '__main__':
    main()