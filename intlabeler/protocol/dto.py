"""Module Doc
"""
import intlabeler.const.payload as payload
import intlabeler.const.msg as const_msg
from intlabeler.base.dto import AsDict
from collections import namedtuple
import json

MSG_VERSION_VAL = '1.0'

class Version():
    version = MSG_VERSION_VAL

class Data(namedtuple("Data", [ payload.X, 
                                payload.LABEL_NAME, 
                                payload.TITLE, 
                                payload.LABEL_TYPE,
                                payload.Y, 
                              ]), AsDict):
    pass

class Error(namedtuple("Error", [ const_msg.ERROR_TITLE, 
                                  const_msg.ERROR_DESC, 
                              ]), AsDict):
    pass


class ServerMsg(namedtuple("ServerMsg", [const_msg.DATA, const_msg.TYPE, const_msg.ID]), AsDict, Version):
    """This class have a payload - see data field
    """
    pass

class ServerReq(namedtuple("ServerReq", [const_msg.TYPE, const_msg.ID]), AsDict, Version):
    """This class doesn't have a payload field. Created on purpose for lightweight requests
    """
    pass

class ServerError(namedtuple("ServerError", [const_msg.DATA, const_msg.TYPE, const_msg.ID]), AsDict, Version):
    """Error message
    """
    pass


class ClientMsg(namedtuple("ClientMsg", [const_msg.DATA, const_msg.TYPE, const_msg.ID]), AsDict, Version):
    """This class have a payload - see data field
    """
    pass

class ClientReq(namedtuple("ClientReq", [const_msg.TYPE, const_msg.ID]), AsDict, Version):
    """This class doesn't have a payload field. Created on purpose for lightweight requests
    """
    pass
