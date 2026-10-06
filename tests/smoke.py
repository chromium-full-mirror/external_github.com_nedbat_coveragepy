# Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
# For details: https://github.com/coveragepy/coveragepy/blob/main/NOTICE.txt

"""
A smoke test to verify that the binary tracer module can be imported.
This is not a test used by pytest, it's run by cibuildwheel.
"""

# pragma: exclude file from coverage
from coverage.tracer import CTracer  # pylint: disable=import-error, no-name-in-module


assert hasattr(CTracer(), "start")
print("CTracer OK!")
