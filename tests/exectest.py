import unittest
import subprocess
from src.execprocess import Exec

class ExecTest(unittest.TestCase):
    def test_execute_command(self):
        Exec('sleep 10').executeCommand()
        cmds = "ps -ef | grep 'sleep 10' | grep -v grep | awk '{print $8}'"
        ps = subprocess.Popen(cmds, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = ps.communicate()[0]
        self.assertEqual(str(output), "b'sleep\\n'")

if __name__ == '__main__':
    unittest.main()