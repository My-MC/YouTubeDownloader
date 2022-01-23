# 参考 http://silence2you.blogspot.com/2013/05/py2exeexe.html
from distutils.core import setup
import py2exe

option = {"compressed": 1, "optimize": 2, "bundle_files": 3, }
# bundle_filesを3にしておくと、exe自体のファイルサイズを小さく抑えることができます。

setup(option={'py2exe': option},
      windows=[{'script': 'main.py', 'icon_resources': 'ico/icon.ico'}])
# windowsにすると、コンソールが表示されずにプログラムが実行されます
# icon_resourcesでexeのiconにしたいiconファイルを指定します。
# zipfileを設定することにより、ディレクトリ配下にlibというフォルダを作成し、
# ライブラリを固めてくれるので、見た目がよくなります。