# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource import Resource


class FlattenedProduct(Resource):
    """FlattenedProduct

    :param id: Resource Id
    :type id: str
    :param type: Resource Type
    :type type: str
    :param tags:
    :type tags: dict
    :param location: Resource Location
    :type location: str
    :param name: Resource Name
    :type name: str
    :param pname:
    :type pname: str
    :param lsize:
    :type lsize: int
    :param provisioning_state:
    :type provisioning_state: str
    """ 

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'pname': {'key': 'properties.pname', 'type': 'str'},
        'lsize': {'key': 'properties.lsize', 'type': 'int'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
    }

    def __init__(self, id=None, type=None, tags=None, location=None, name=None, pname=None, lsize=None, provisioning_state=None):
        super(FlattenedProduct, self).__init__(id=id, type=type, tags=tags, location=location, name=name)
        self.pname = pname
        self.lsize = lsize
        self.provisioning_state = provisioning_state
