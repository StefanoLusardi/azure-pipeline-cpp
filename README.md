# azure-pipeline-cpp
Demo project to build a cross-platform CMake-based C++ solution on Azure DevOps Pipelines for Windows, Linux and MacOS

|OS|Compiler|Status|
|:--:|:--:|:--:|
| Windows 2019 | Visual Studio 2019 | [![Build Status](https://stefanolusardi.visualstudio.com/azure-pipeline-cpp/_apis/build/status%2Fbuild?branchName=main&jobName=Build&configuration=Build%20windows2019_msvc)](https://stefanolusardi.visualstudio.com/azure-pipeline-cpp/_build/latest?definitionId=23&branchName=main) | 
| Windows 2019 | clang 15 | [![Build Status](https://stefanolusardi.visualstudio.com/azure-pipeline-cpp/_apis/build/status%2Fbuild?branchName=main&jobName=Build&configuration=Build%20windows2019_clang)](https://stefanolusardi.visualstudio.com/azure-pipeline-cpp/_build/latest?definitionId=23&branchName=main) | 
| Windows 2019 | clang-cl 15 | [![Build Status](https://stefanolusardi.visualstudio.com/azure-pipeline-cpp/_apis/build/status%2Fbuild?branchName=main&jobName=Build&configuration=Build%20windows2019_clang_cl)](https://stefanolusardi.visualstudio.com/azure-pipeline-cpp/_build/latest?definitionId=23&branchName=main) | 
| Windows 2022 | Visual Studio 2022 | [![Build Status](https://stefanolusardi.visualstudio.com/azure-pipeline-cpp/_apis/build/status%2Fbuild?branchName=main&jobName=Build&configuration=Build%20windows2022_msvc)](https://stefanolusardi.visualstudio.com/azure-pipeline-cpp/_build/latest?definitionId=23&branchName=main) | 
| Windows 2022 | clang 15 | [![Build Status](https://stefanolusardi.visualstudio.com/azure-pipeline-cpp/_apis/build/status%2Fbuild?branchName=main&jobName=Build&configuration=Build%20windows2022_clang)](https://stefanolusardi.visualstudio.com/azure-pipeline-cpp/_build/latest?definitionId=23&branchName=main) | 
| Windows 2022 | clang-cl 15 | [![Build Status](https://stefanolusardi.visualstudio.com/azure-pipeline-cpp/_apis/build/status%2Fbuild?branchName=main&jobName=Build&configuration=Build%20windows2022_clang_cl)](https://stefanolusardi.visualstudio.com/azure-pipeline-cpp/_build/latest?definitionId=23&branchName=main) | 
| Ubuntu 20.04 | clang 10 | [![Build Status](https://stefanolusardi.visualstudio.com/azure-pipeline-cpp/_apis/build/status%2Fbuild?branchName=main&jobName=Build&configuration=Build%20ubuntu2004_clang_10)](https://stefanolusardi.visualstudio.com/azure-pipeline-cpp/_build/latest?definitionId=23&branchName=main) |
| Ubuntu 20.04 | clang 11 | [![Build Status](https://stefanolusardi.visualstudio.com/azure-pipeline-cpp/_apis/build/status%2Fbuild?branchName=main&jobName=Build&configuration=Build%20ubuntu2004_clang_11)](https://stefanolusardi.visualstudio.com/azure-pipeline-cpp/_build/latest?definitionId=23&branchName=main) |
| Ubuntu 20.04 | clang 12 | [![Build Status](https://stefanolusardi.visualstudio.com/azure-pipeline-cpp/_apis/build/status%2Fbuild?branchName=main&jobName=Build&configuration=Build%20ubuntu2004_clang_12)](https://stefanolusardi.visualstudio.com/azure-pipeline-cpp/_build/latest?definitionId=23&branchName=main) |
| Ubuntu 20.04 | gcc 9 | [![Build Status](https://stefanolusardi.visualstudio.com/azure-pipeline-cpp/_apis/build/status%2Fbuild?branchName=main&jobName=Build&configuration=Build%20ubuntu2004_gcc_9)](https://stefanolusardi.visualstudio.com/azure-pipeline-cpp/_build/latest?definitionId=23&branchName=main) |
| Ubuntu 20.04 | gcc 10 | [![Build Status](https://stefanolusardi.visualstudio.com/azure-pipeline-cpp/_apis/build/status%2Fbuild?branchName=main&jobName=Build&configuration=Build%20ubuntu2004_gcc_10)](https://stefanolusardi.visualstudio.com/azure-pipeline-cpp/_build/latest?definitionId=23&branchName=main) |
| Ubuntu 22.04 | clang 13 | [![Build Status](https://stefanolusardi.visualstudio.com/azure-pipeline-cpp/_apis/build/status%2Fbuild?branchName=main&jobName=Build&configuration=Build%20ubuntu2204_clang_13)](https://stefanolusardi.visualstudio.com/azure-pipeline-cpp/_build/latest?definitionId=23&branchName=main) |
| Ubuntu 22.04 | clang 14 | [![Build Status](https://stefanolusardi.visualstudio.com/azure-pipeline-cpp/_apis/build/status%2Fbuild?branchName=main&jobName=Build&configuration=Build%20ubuntu2204_clang_14)](https://stefanolusardi.visualstudio.com/azure-pipeline-cpp/_build/latest?definitionId=23&branchName=main) |
| Ubuntu 22.04 | clang 15 | [![Build Status](https://stefanolusardi.visualstudio.com/azure-pipeline-cpp/_apis/build/status%2Fbuild?branchName=main&jobName=Build&configuration=Build%20ubuntu2204_clang_15)](https://stefanolusardi.visualstudio.com/azure-pipeline-cpp/_build/latest?definitionId=23&branchName=main) |
| Ubuntu 22.04 | gcc 9 | [![Build Status](https://stefanolusardi.visualstudio.com/azure-pipeline-cpp/_apis/build/status%2Fbuild?branchName=main&jobName=Build&configuration=Build%20macos12_gcc_12)](https://stefanolusardi.visualstudio.com/azure-pipeline-cpp/_build/latest?definitionId=23&branchName=main) |
| Ubuntu 22.04 | gcc 10 | [![Build Status](https://stefanolusardi.visualstudio.com/azure-pipeline-cpp/_apis/build/status%2Fbuild?branchName=main&jobName=Build&configuration=Build%20ubuntu2204_gcc_10)](https://stefanolusardi.visualstudio.com/azure-pipeline-cpp/_build/latest?definitionId=23&branchName=main) |
| Ubuntu 22.04 | gcc 11 | [![Build Status](https://stefanolusardi.visualstudio.com/azure-pipeline-cpp/_apis/build/status%2Fbuild?branchName=main&jobName=Build&configuration=Build%20ubuntu2204_gcc_11)](https://stefanolusardi.visualstudio.com/azure-pipeline-cpp/_build/latest?definitionId=23&branchName=main) |
| Ubuntu 22.04 | gcc 12 | [![Build Status](https://stefanolusardi.visualstudio.com/azure-pipeline-cpp/_apis/build/status%2Fbuild?branchName=main&jobName=Build&configuration=Build%20ubuntu2204_gcc_12)](https://stefanolusardi.visualstudio.com/azure-pipeline-cpp/_build/latest?definitionId=23&branchName=main) |
| Ubuntu 22.04 | gcc 13 | [![Build Status](https://stefanolusardi.visualstudio.com/azure-pipeline-cpp/_apis/build/status%2Fbuild?branchName=main&jobName=Build&configuration=Build%20ubuntu2204_gcc_13)](https://stefanolusardi.visualstudio.com/azure-pipeline-cpp/_build/latest?definitionId=23&branchName=main) |
| MacOS 12 | clang 14 | [![Build Status](https://stefanolusardi.visualstudio.com/azure-pipeline-cpp/_apis/build/status%2Fbuild?branchName=main&jobName=Build&configuration=Build%20macos12_clang)](https://stefanolusardi.visualstudio.com/azure-pipeline-cpp/_build/latest?definitionId=23&branchName=main) |
| MacOS 12 | gcc 11 | [![Build Status](https://stefanolusardi.visualstudio.com/azure-pipeline-cpp/_apis/build/status%2Fbuild?branchName=main&jobName=Build&configuration=Build%20macos12_gcc_11)](https://stefanolusardi.visualstudio.com/azure-pipeline-cpp/_build/latest?definitionId=23&branchName=main) |
| MacOS 12 | gcc 12 | [![Build Status](https://stefanolusardi.visualstudio.com/azure-pipeline-cpp/_apis/build/status%2Fbuild?branchName=main&jobName=Build&configuration=Build%20macos12_gcc_12)](https://stefanolusardi.visualstudio.com/azure-pipeline-cpp/_build/latest?definitionId=23&branchName=main) |
| MacOS 13 | clang 14 | [![Build Status](https://stefanolusardi.visualstudio.com/azure-pipeline-cpp/_apis/build/status%2Fbuild?branchName=main&jobName=Build&configuration=Build%20macos13_clang14)](https://stefanolusardi.visualstudio.com/azure-pipeline-cpp/_build/latest?definitionId=23&branchName=main) |
| MacOS 13 | gcc 11 | [![Build Status](https://stefanolusardi.visualstudio.com/azure-pipeline-cpp/_apis/build/status%2Fbuild?branchName=main&jobName=Build&configuration=Build%20macos13_gcc_11)](https://stefanolusardi.visualstudio.com/azure-pipeline-cpp/_build/latest?definitionId=23&branchName=main) |
| MacOS 13 | gcc 12 | [![Build Status](https://stefanolusardi.visualstudio.com/azure-pipeline-cpp/_apis/build/status%2Fbuild?branchName=main&jobName=Build&configuration=Build%20macos13_gcc_12)](https://stefanolusardi.visualstudio.com/azure-pipeline-cpp/_build/latest?definitionId=23&branchName=main) |

---

## Setup
```bash
python -m pip install --upgrade pip
python -m venv .venv

# Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate.bat

pip3 install -r scripts/requirements.txt --no-cache-dir --disable-pip-version-check

python3 scripts/conan/profile.py <COMPILER_NAME> <COMPILER_VERSION>
python3 scripts/conan/install.py <Debug|Release> <PROFILE>
```

## Build
```bash
python ./scripts/cmake/configure.py Release <PROFILE>
python ./scripts/cmake/build.py Release
python ./scripts/cmake/install.py Release
```
