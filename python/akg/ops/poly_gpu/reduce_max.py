# Copyright 2020 Huawei Technologies Co., Ltd
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

"""reduce_max"""
import akg
from akg.ops.math_gpu import reduce_max
import akg.topi as topi


@akg.schedule(topi.cuda.schedule_reduce)
def reduce_max_manual(data, axis, keepdims):
    """Reduce max with manual schedule."""
    return reduce_max.reduce_max(data, axis=axis, keepdims=keepdims)

def reduce_max_auto(data, axis, keepdims):
    """Reduce max with auto schedule."""
    return reduce_max.reduce_max(data, axis=axis, keepdims=keepdims)
