# CSSO Antiflash
Very simple antiflash for Source Offensive

Script just change some bytes for removing flashbang overlay
```
csso.write_float(flashstrength, float(0) if csso.read_float(flashstrength) == float(255) else float(255))
```
If `m_flFlashMaxAlpha` is 255, script change value to 0 and back

Installation:
1. `pip install pymem`
2. `python main.py`

# WARNING!
> Any cheats are bad. The script was created as a learning interest
