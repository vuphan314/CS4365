# -*- mode: python -*-

block_cipher = None

#####################################################################
#####################################################################
# Vu needs to manually edit the spec file

added_files = [
        ('kn_lexicon.txt', ''),
        ('kn_grammar.txt', '')
    ]

a = Analysis(['engine.py'],
             pathex=['D:\\repos\\CS4365\\code\\knengine'],
             binaries=None,
             datas=added_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

#####################################################################
#####################################################################

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='engine',
          debug=False,
          strip=False,
          upx=True,
          console=True )