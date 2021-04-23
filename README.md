# Taxiway Sign Generator

This project creates taxiway signs to be used as a training dataset for neural networks.

## Usage

Set font and size in `config.py`.
```
python sign_generator.py [-ul UP-LEFT] [-l LEFT] [-dl DOWN-LEFT] [-c CURRENT] [-ur UP-RIGHT] [-r RIGHT] [-dr DOWN-RIGHT]
```

generates a single sign.

```
python batch_generate.py creates a number of different and random signs.
```
![examples](/img/examples.png)

## Requirements

[Python-Pillow](https://github.com/python-pillow/Pillow)

[Overpass font](https://github.com/RedHatOfficial/Overpass)
