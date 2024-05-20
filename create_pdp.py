from pydomo.datasets import DataSetRequest, Schema, Column, ColumnType, Policy
from pydomo.datasets import PolicyFilter, FilterOperator, PolicyType, Sorting
#from src.helpers.connection import DomoSDKExamples

import logging
import random
from pydomo import Domo
from pydomo.datasets import DataSetRequest, Schema, Column, ColumnType, Policy
from pydomo.datasets import PolicyFilter, FilterOperator, PolicyType, Sorting
from pydomo.users import CreateUserRequest
from pydomo.datasets import DataSetRequest, Schema, Column, ColumnType
from pydomo.streams import UpdateMethod, CreateStreamRequest
from pydomo.groups import CreateGroupRequest


def pdp_policy_creation(domo,dataset_id,column,values,name,users,groups):

        pdp_filter = PolicyFilter()
        pdp_filter.column = column
        pdp_filter.operator = FilterOperator.EQUALS
        pdp_filter.values = values
        pdp_request = Policy()
        pdp_request.name = name
        pdp_request.filters = [pdp_filter]
        pdp_request.type = PolicyType.USER
        pdp_request.users = users
        pdp_request.groups = groups
        domo.pdp_create(dataset_id,pdp_request)
        
        return {'pdp created on Dataset': dataset_id}
