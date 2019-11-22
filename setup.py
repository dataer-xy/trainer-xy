
import os
from setuptools import setup, find_packages


# ------------------------------------------------------------------------
# global

DIR = os.path.dirname(os.path.abspath(__file__)) # os.path.dirname(__file__)



# ------------------------------------------------------------------------
# extras_require

# extras_require = {
#   'pyspark': ['pyspark>=2.3.1'],
#   'dask': ['dask[complete]>=1.0.0'],
#   'koalas': ["pyspark>=2.4", "koalas>0.16.0"],
#   'django' : ['django>=2.0'],
#   'bigdata' : ["pyspark>=2.4", "koalas>0.16.0", "dask[complete]>=1.0.0"],
# }
# extras_require['complete'] = sorted(set(sum(extras_require.values(), [])))
extras_require = None

# ------------------------------------------------------------------------
# version
# NOTE: 只需要更改 trainer.version 即可

def get_version(versionTuple):
    if not isinstance(versionTuple[-1], int):
        return ".".join(map(str, versionTuple[:-1])) + versionTuple[-1]
    return ".".join(map(str, versionTuple))


init = os.path.join(
   DIR , "trainer", "version.py"
)

versonLine = list(
    filter(lambda line: line.startswith("VERSION"), open(init))
)[0]


# ------------------------------------------------------------------------
# requirements.txt

def strip_comments(line):
    return line.split("#", 1)[0].strip()


def reqs(*f):
    return list(
        filter(
            None,
            [strip_comments(line) for line in open(os.path.join(DIR, *f)).readlines()]
        )
    )


# ------------------------------------------------------------------------
# readme
# NOTE: setup 已经开始支持 markdown 了

def read_me(f):
    return open(f, "r", encoding='utf-8').read()

README = os.path.join(DIR, "README.md")


# ------------------------------------------------------------------------

NAME = 'trainer-xy' # NOTE: 需要独一无二 unique。将用于 pypi 的显示, 而不是用于 import, import 的包名与 packages 和 package_dir 参数一致。

PACKAGES = ['trainer'] # NOTE: 可能需要将 test 单独分离出来，因为 test 会让项目文件增多

AUTHOR = "syy"

AUTHOR_EMAIL = "1121225022@qq.com"

MAINTAINER = "syy"

MAINTAINER_EMAIL = '1121225022@qq.com'

KEYWORDS = 'trainer, train, machine learning, deep learning'

DESCRIPTION = 'trainer dashboard'

LONG_DESCRIPTION = read_me(README)

LONG_DESCRIPTION_CONTENT_TYPE='text/markdown'

URL = 'https://github.com/songyanyi/Trainer'

VERSION = get_version(eval(versonLine.split("=")[-1]))

INSTALL_REQUIRES = reqs("requirements.txt")

LICENSE = "BSD"

PYTHON_REQUIRES = ">=3.5"

CLASSIFIERS = [
    "Development Status :: 2 - Pre-Alpha",
    "Environment :: Console",
    "Natural Language :: Chinese (Simplified)",
    "Natural Language :: English",
    "Operating System :: OS Independent",  # 不依赖系统
    "Intended Audience :: Science/Research",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Topic :: Scientific/Engineering",
    "Topic :: Scientific/Engineering :: Artificial Intelligence", 
    "Topic :: Scientific/Engineering :: Image Recognition"
] # NOTE: 说明参考 https://pypi.org/pypi?%3Aaction=list_classifiers


# ------------------------------------------------------------------------

setup(name=NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION ,
      long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
      url=URL,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      maintainer=MAINTAINER,
      maintainer_email=MAINTAINER_EMAIL,
      license=LICENSE,
      keywords=KEYWORDS,
      classifiers=CLASSIFIERS,
      packages=PACKAGES, # find_packages()
      python_requires=PYTHON_REQUIRES,
      install_requires=INSTALL_REQUIRES,
      extras_require=extras_require,
      include_package_data=True,
      # setup_requires=setup_requires,
      # tests_require=['pytest'],
      # package_data={
      #   '': ['*.json', '*.pkl'],  # include json and pkl files
      # },
      zip_safe=False)



# ------------------------------------------------------------------------
# NOTE:

# setuptools 和 distutils 对于文件查找的算法是一样的：
# 
#     所有在 py_modules 和 packages 指定的对应模块文件
#     所有在 ext_modules 和 libraries 选项指定的源文件和库
#     scripts 选项指定的脚本文件
#     所有类似测试脚本的文件，比如：test/test*.py (低版本的包管理工具可能不支持)
#     README.txt（或 README），setup.py 以及 setup.cfg（README 文件目前无法支持更多的后缀格式）
#     package_data 选项指定的文件
#     data_files 选项指定的文件




