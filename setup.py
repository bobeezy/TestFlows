# Copyright 2019 Katteli Inc.
# TestFlows.com Open-Source Software Testing Framework (http://testflows.com)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fd:
    long_description = fd.read()

setup(
    name="testflows",
    version="1.6.63",
    description="TestFlows.com Open-Source Software Testing Framework",
    author="Vitaliy Zakaznikov",
    author_email="vzakaznikov@testflows.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/testflows/testflows",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.6',
    license="Apache-2.0",
    zip_safe=False,
    install_requires=[
        "testflows.core>=1.6.201101.1131719",
        "testflows.asserts>=6.3.200715.1200940",
        "testflows.uexpect>=1.6.201003.1161749",
        "testflows.connect>=1.6.201003.1161623",
        "testflows.database>=1.6.200713.1142213"
    ],
    extras_require={
        "dev": [
        ]
    }
)
