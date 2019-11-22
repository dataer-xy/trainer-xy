from .version import __version__


# from .backend import trainerApp # 不要放在这里，加载很费劲



#------------------------------------------------------
# core

from .core import ModelConfigBase

from .core import MqConn
from .core import Serializer
from .core import MessageManager

from .core import run_sysinfo_subprocess

from .core import trainerConfig


from .core import is_continue_in_batchState
from .core import is_continue_in_epochState


#------------------------------------------------------
# utils



