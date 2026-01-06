import subprocess

domain = input("Domain: ")

subprocess.run(["subfinder", "-d", domain])
subprocess.run(["assetfinder", domain])
