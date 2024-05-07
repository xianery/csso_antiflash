import pymem.memory

offsets = {
    "dwLocalPlayer": int(0x6D6870),
    "m_flFlashMaxAlpha": int(0x9CE0),
}

csso = pymem.Pymem('hl2.exe')
client = pymem.process.module_from_name(csso.process_handle, 'client.dll').lpBaseOfDll

localplayer = csso.read_uint(client + offsets['dwLocalPlayer'])
flashstrength = localplayer + offsets['m_flFlashMaxAlpha']

csso.write_float(flashstrength, float(0) if csso.read_float(flashstrength) == float(255) else float(255))

csso.close_process()
