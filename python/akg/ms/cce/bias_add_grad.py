#!/usr/bin/env python3
# coding: utf-8
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

"""BiasAddGrad"""
from akg.ops.nn import bias_add_ad
from akg.utils.format_transform import get_shape

def BiasAddGrad(dout, data_format=None):
    """grediant of bias_add"""
    if data_format is None:
        data_format = ["NCHW"]
    dout_shape = get_shape(dout)
    return bias_add_ad.bias_add_ad(dout, dout_shape, data_format[0])
