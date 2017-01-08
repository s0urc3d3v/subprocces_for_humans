import subprocess


def run_script(exec): #Exec muesst ein List sein ob ihr wollen mehr denn eine Befehl
    subprocess.run(args=exec, returncode=0)
def run_script_with_ouput(exec): #WARNUNG: These kann ein Sicherheit Problem sein veil ich gemacht die shell=True Argument!
    return subprocess.run(exec, shell=True, check=True, stdout=subprocess.PIPE)