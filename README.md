
# Obsidian Property Modifier

## Description

[Obsidian](https://obsidian.md/) is a powerful note taking app (and so much more). In some cases, it is useful to manage notes with metadata. This metadata is called properties in Obsidian notes.

Sometimes it is neccessary to change or delete this properties, because the data processing behind needs it.

This python script process a directory with markdown files and adds or deletes properties in their.

## Usage

```
Obsidian Property Modifier 0.1.0 by psycore8
usage: Obsidian Property Modifier [-h] [-m] [-d] -wd WORKING_DIR -pn PROP_NAME [-pv PROP_VALUE]

Tool for mass manipulating Obsidian Properties

options:
  -h, --help            show this help message and exit
  -m, --modify          add or modify properties in a directory
  -d, --delete          delete properties in a directory
  -wd WORKING_DIR, --working-dir WORKING_DIR
                        the directory with the md files to process
  -pn PROP_NAME, --prop-name PROP_NAME
                        the property name is required for delete and modify
  -pv PROP_VALUE, --prop-value PROP_VALUE
                        the property value is needed for add or mod
```

## Examples

### MD File

```markdown
---
field1: false
field2: Stringfield
field3:
  - tag1
  - tag2
---
# Testfile

## Notes
```

`-m -wd directory -pn field2 -pv godmode`
`-d -wd directoy -pn field3`

The properties will be modified as followed:

```markdown
---
field1: false
field2: godmode
---
# Testfile

## Notes
```