# -*- mode: python -*-

block_cipher = None


a = Analysis(['dosisTest\\dosisV1.py'],
             pathex=['C:\\Python27\\share\\qt'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
ui_file =  [('mainwindow.ui', 'dosisTest\\mainwindow.ui', 'DATA')]
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='dosisV1',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
                a.datas + ui_file,
               strip=False,
               upx=True,
               name='dosisV1')
