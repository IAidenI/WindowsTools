import subprocess

def IsLibInstalled(packet):
    try:
        subprocess.check_output(["pip", "show", packet])
        return True
    except subprocess.CalledProcessError:
        return False

def LibInstall(packet):
    result = subprocess.run(["pip", "install", packet], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    if result.returncode != 0:
        return False
    else:
        return True
