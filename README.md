
# Obsidian Property Modifier

## Description

[Obsidian](https://obsidian.md/) is a powerful note taking app (and so much more). In some cases, it is useful to manage notes with metadata. This metadata is called properties in Obsidian notes.

Sometimes it is neccessary to change or delete this properties, because the data processing behind needs it.

The Python script processes markdown files within a directory. It can add, modify, or delete properties.

## Usage

```
Obsidian Property Modifier 0.1.1 by psycore8
usage: Obsidian Property Modifier [-h] [-m {field,value}] [-d] -wd WORKING_DIR -pf PROP_FIELD [-nf NEW_FIELD]
                                  [-pv PROP_VALUE]

Tool for mass manipulating Obsidian Properties

options:
  -h, --help            show this help message and exit
  -m {field,value}, --modify {field,value}
                        add or modify property fields or values in a directory
  -d, --delete          delete properties in a directory
  -wd WORKING_DIR, --working-dir WORKING_DIR
                        the directory with the md files to process
  -pf PROP_FIELD, --prop-field PROP_FIELD
                        the property field is required for delete and modify
  -nf NEW_FIELD, --new-field NEW_FIELD
                        modify the field name to this value
  -pv PROP_VALUE, --prop-value PROP_VALUE
                        the property value is needed for add or mod
```

## Examples

### Markdown File

```markdown
---
city: Ohio
district: Florida
---
```

#### Adding a field with value

`python propmod.py -wd directory --modify value --prop-field short --prop-value FL`

```markdown
---
city: Ohio
district: Florida
short: FL
---
```

#### Modify a value

`python propmod.py -wd directory --modify value --prop-field city --prop-value Miami`

```markdown
---
city: Miami
district: Florida
short: FL
---
```

#### Modify a field

`python propmod.py -wd directory --modify field --prop-field district --new-field state`

```markdown
---
city: Miami
state: Florida
short: FL
---
```

#### Delete a field

`python propmod.py -wd directory --delete --prop-field short`

```markdown
---
city: Miami
state: Florida
---
```