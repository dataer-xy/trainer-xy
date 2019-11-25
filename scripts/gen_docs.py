""" 生成文档

sphinx-quickstart

cd docs
sphinx-apidoc -o source/reference/api + 源码

make clean
make html
make latexpdf

"""

import os
import os.path as op
import shutil
import errno
import subprocess

from sphinx.application import Sphinx
from sphinx.util.docutils import docutils_namespace

# DIR = os.getcwd() # NOTE: 注意getcwd 的使用格式，这个需要在调试的时候使用，改成 file 的形式
DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.path.pardir)) # 父级目录


docDir = os.path.join(DIR,"docs")


def clear_all_api():
    # Remove previously generated rst files. Ignore errors just in case it stops generating whole docs.
    shutil.rmtree(os.path.join(docDir,"source","reference","api") , ignore_errors=True)
    try:
        os.mkdir(os.path.join(docDir,"source","reference","api"))
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise



def gen_html(isRebuild=False):
    """ make html """

    if isRebuild:
        clear_all_api()

    srcDir = os.path.join(DIR,"docs") # Directory containing source
    confDir = os.path.join(docDir,"source") # Directory containing ``conf.py``
    outDir = op.join(docDir, '_build', 'html') # Directory for storing build documents.
    toctreesDir = op.join(docDir, '_build', 'toctrees') # Directory for storing pickled doctrees
    # Avoid warnings about re-registration, see: https://github.com/sphinx-doc/sphinx/issues/5038
    with docutils_namespace():
        app = Sphinx(srcDir, confDir, outDir, toctreesDir,
                     buildername='html')
        # need to build within the context manager for automodule and backrefs to work
        app.build(force_all=isRebuild, filenames=[])
    return app


def gen_pdf(isRebuild=False):
    """make latexpdf """

    if isRebuild:
        clear_all_api()

    srcDir = os.path.join(DIR,"docs")
    confDir = os.path.join(docDir,"source")
    outDir = op.join(docDir, '_build', 'latex')
    toctreesDir = op.join(docDir, '_build', 'toctrees-pdf')
    # Avoid warnings about re-registration, see: https://github.com/sphinx-doc/sphinx/issues/5038
    with docutils_namespace():
        app = Sphinx(srcDir, confDir, outDir, toctreesDir,
                     buildername='latex') # latex 只有 tex 文件
        # need to build within the context manager for automodule and backrefs to work
        app.build(force_all=isRebuild, filenames=[])
    
    # 构建 pdf ERROR 不行，有异常，还是手动编译算了
    isBuildPdf = False
    if isBuildPdf:
        cmd = "pdflatex {texFile} -output-directory={pdfDir}".format(
            texFile = os.path.join(outDir,"dataset.tex"),
            pdfDir=outDir
        )
        ret = subprocess.run(
            cmd, 
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True
        )
        if ret.returncode != 0: 
            print("子程序错误！\n {err}".format(err=ret.stderr.decode("utf-8")))
            code = 1
        else:
            code = 0
        return code


def main():
    isRebuild = True
    gen_html(isRebuild)
    # gen_pdf(isRebuild)


if __name__ == "__main__":
    main()







