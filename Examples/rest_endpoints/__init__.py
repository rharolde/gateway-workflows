# Copyright 2020 BlueCat Networks (USA) Inc. and its affiliates
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
#
# By: BlueCat Networks
# Date: 2020-12-16
# Gateway Version: 20.3.1
# Description: Example Gateway workflow

# pylint: disable=redefined-builtin,missing-docstring
type = 'api'
sub_pages = [
    {
        'name'        : 'rest_endpoints',
        'title'       : 'Simple RESTful API Endpoints',
        'endpoint'    : 'rest_endpoints/get_test',
        'description' : 'Simple RESTful API Endpoints'
    }
]