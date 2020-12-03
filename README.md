<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/control-characters.svg?maxAge=3600)](https://pypi.org/project/control-characters/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/control-characters.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/control-characters.py/actions)

### Installation
```bash
$ [sudo] pip install control-characters
```

#### Features
fixes `plistlib`  problem with control characters
```python
>>> plistlib.dump(data, open(path, 'wb'))
...
ValueError: strings can't contains control characters; use bytes instead
```

#### Examples
environment variables without control characters:
```python
env = dict((k, control_characters.remove(v)) for k, v in os.environ.items())
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>
