
# Obsidian Property Modifier

## Description

[Obsidian](https://obsidian.md/) is a powerful note taking app (and so much more). In some cases, it is useful to manage notes with metadata. This metadata is called properties in Obsidian notes.

Sometimes it is neccessary to change or delete this properties, because the data processing behind needs it.

The Python script processes markdown files within a directory. It can add, modify, or delete properties.

## Usage

```
Obsidian Property Modifier 0.1.3 by psycore8
Tool for mass manipulating Obsidian Properties

usage: Obsidian Property Modifier [-h] [-m {field,value}] [-d] [-dir WORKING_DIR] -f FIELD [-n NEW_FIELD]
                                  [-t {bool,int,str,date,datetime}] [-v VALUE]

options:
  -h, --help            show this help message and exit
  -m {field,value}, --modify {field,value}
                        add or modify property fields or values in a directory
  -d, --delete          delete properties in a directory
  -dir WORKING_DIR, --working-dir WORKING_DIR
                        the directory with the md files to process
  -f FIELD, --field FIELD
                        the property field is required for delete and modify
  -n NEW_FIELD, --new-field NEW_FIELD
                        modify the field name to this value
  -t {bool,int,str,date,datetime}, --type {bool,int,str,date,datetime}
                        data type for property field
  -v VALUE, --value VALUE
                        the property value is needed for add or mod
```

If your working directory is always the same, you can use a config file to input this argument:

```stylus
[arguments]
working_directory = directory
```

## Examples

### Markdown File

```stylus
---
city: Ohio
district: Florida
---
```

### Adding a field with value

`python propmod.py -dir directory --modify value --field short --value FL`

```stylus
---
city: Ohio
district: Florida
short: FL
---
```

#### Adding a date or datetime

`python propmod.py -dir directory --modify value --field date --value 01.05.1999 --type date`

or

`python propmod.py -dir directory --modify value --field datetime --value 01.05.1999-12:35 --type datetime`

results in

```stylus
...
date: 1999-05-01
OR
datetime: 1999-05-01 12:35:00
...
```
#### Modify

#### Modify a value

`python propmod.py -dir directory --modify value --field city --value Miami`

```stylus
---
city: Miami
district: Florida
short: FL
---
```

#### Modify a value and the data type

`python propmod.py -dir directory --modify value --field proof --value True --type bool`

```stylus
---
city: Miami
district: Florida
short: FL
proof: True
---
```
#### Modify a field

`python propmod.py -dir directory --modify field --field district --new-field state`

```stylus
---
city: Miami
state: Florida
short: FL
proof: True
---
```

#### Delete a field

`python propmod.py -dir directory --delete --field short`

```stylus
---
city: Miami
state: Florida
proof: True
---
```