# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['/Users/louismelahn/Documents/GitHub/Python/pdfMakerInit/src/pdf_maker_init/main.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['pdf_maker_init'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='pdfMakerInit',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='pdfMakerInit',
)
app = BUNDLE(
    coll,
    name='pdfMakerInit.app',
    icon=None,
    bundle_identifier=None,
)