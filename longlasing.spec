# -*- mode: python ; coding: utf-8 -*-
from kivy_deps import sdl2, glew
block_cipher = None

a = Analysis(['Music Player.py'],
             pathex=['C:\\Users\\CCS\\Desktop\\MusicPlayer'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
a.datas += [('Code\builder.kv', 'C:\\Users\\CCS\\Desktop\\MusicPlayer\\builder.kv', 'DATA')]
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Music Player',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe, Tree('C:\\Users\\CCS\\Desktop\\MusicPlayer\\'),
               a.binaries,
               a.zipfiles,
               a.datas,
               *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Music Player')
