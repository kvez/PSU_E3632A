# -*- mode: python ; coding: utf-8 -*-
# Keysight E3632A tápegység vezérlő – PyInstaller spec
# Build: python -m PyInstaller PSU_E3632A.spec --noconfirm
# Eredmény: dist\PSU_E3632A.exe

from PyInstaller.utils.hooks import collect_all

datas, binaries, hiddenimports = [], [], [
    'serial',
    'serial.tools',
    'serial.tools.list_ports',
    'serial.tools.list_ports_windows',
    'matplotlib.backends.backend_tkagg',
    'matplotlib.backends._backend_tk',
    'tkinter', 'tkinter.ttk',
]

tmp = collect_all('matplotlib')
datas += tmp[0]; binaries += tmp[1]; hiddenimports += tmp[2]

tmp = collect_all('serial')
datas += tmp[0]; binaries += tmp[1]; hiddenimports += tmp[2]

a = Analysis(
    ['psu_e3632a.py'],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['scipy', 'uvicorn', 'fastapi', 'pyvisa'],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='PSU_E3632A',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
