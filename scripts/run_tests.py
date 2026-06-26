import subprocess
import sys

cmd = [sys.executable, "-m", "pytest", "tests", "-v", "--tb=short"]
result = subprocess.run(cmd)
sys.exit(result.returncode)
