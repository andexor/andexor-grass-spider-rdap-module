#!/bin/bash

# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 Andexor Network, Inc.
# Author: Ed Jenkins<ed@andexor.net>

# Modify and run this to add new dependencies.

# httpx
# [HTTPX](https://www.python-httpx.org/)
uv --quiet add httpx
uv --quiet add httpx[http2]

# whodap
# [whodap](https://pypi.org/project/whodap/)
# [whodap](https://github.com/pogzyb/whodap)
uv --quiet add whodap

# To get a license report, you can use pip-licenses.
# It is not required for the project to run,
# but it is useful for auditing dependencies.
# https://pypi.org/project/pip-licenses/

mkdir -p reports
uv --quiet add pip-licenses
uv --quiet sync
echo " " >> reports/license-report.txt
date --iso-8601 seconds >> reports/license-report.txt
echo " " >> reports/license-report.txt
uv run pip-licenses --format=markdown >> reports/license-report.txt

# Check for known vulnerabilities in dependencies.
echo " " >> reports/uv-audit-report.txt
date --iso-8601 seconds >> reports/uv-audit-report.txt
echo " " >> reports/uv-audit-report.txt
uv --preview-features audit-command audit 2>> reports/uv-audit-report.txt
