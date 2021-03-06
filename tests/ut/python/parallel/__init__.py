# Copyright 2019 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import mindspore.context as context
from mindspore.parallel._auto_parallel_context import auto_parallel_context
from mindspore.parallel._utils import _reset_op_id


def setup_module(module):
    auto_parallel_context().set_enable_all_reduce_fusion(enable_all_reduce_fusion=True)
    context.set_context(mode=context.GRAPH_MODE, device_target="Ascend", save_graphs=False)
    _reset_op_id()


def teardown_module():
    context.reset_auto_parallel_context()
    _reset_op_id()
