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
# ==============================================================================
from util import save_and_check

import mindspore.dataset as ds
from mindspore import log as logger

DATA_DIR = ["../data/dataset/testTFTestAllTypes/test.data"]
SCHEMA_DIR = "../data/dataset/testTFTestAllTypes/datasetSchema.json"
COLUMNS = ["col_1d", "col_2d", "col_3d", "col_binary", "col_float",
           "col_sint16", "col_sint32", "col_sint64"]
GENERATE_GOLDEN = False


def test_case_columns_list():
    """
    a simple repeat operation.
    """
    logger.info("Test Simple Repeat")
    # define parameters
    repeat_count = 2
    parameters = {"params": {'repeat_count': repeat_count}}
    columns_list = ["col_sint64", "col_sint32"]
    # apply dataset operations
    data1 = ds.TFRecordDataset(DATA_DIR, SCHEMA_DIR, columns_list=columns_list, shuffle=False)
    data1 = data1.repeat(repeat_count)

    filename = "columns_list_result.npz"
    save_and_check(data1, parameters, filename, generate_golden=GENERATE_GOLDEN)
