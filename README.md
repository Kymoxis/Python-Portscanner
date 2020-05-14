# Python-Portscanner
A simple colorful Python TCP Port Scanner; just for a quick scan.

## Install
You will need the colorama Module, because on Windows the ANSI colors are not working properly
```
pip install colorama
```

## Usage
```
python3 pyscanner.py <ip> <starting Port> <End Port>
```
or

Set the executable Flag:
```
chmod +x pyscanner.py

./pyscanner.py <ip> <starting Port> <End Port>
```

## Example:

```

./pyscanner.py 192.168.2.1 1 1023

```

or

```

python3 pyscanner.py 192.168.2.1 1 1023

```

### License
MIT license; see LICENSE file.
