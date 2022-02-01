import subprocess

def test_cli():
    x = subprocess.run("fixup", capture_output=True)
    x.check_returncode()
    assert x.stderr.decode() == ""
    assert x.stdout.decode() == "hello world!"
