import os
import subprocess
import shlex

import requests


def get_editor_choice():
    while True:
        choice = input("请选择编辑器 (1: VSCode, 2: Cursor) [默认: 1]: ").strip()
        if not choice:
            return "vscode"
        if choice == "1":
            return "vscode"
        if choice == "2":
            return "cursor"
        print("无效的选择，请重新输入")


def list_extensions(editor):
    if editor == "vscode":
        cmd = "code --list-extensions --show-versions"
    else:
        cmd = "cursor --list-extensions --show-versions"

    p = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE, env=os.environ)
    out = p.stdout.read()
    data = out.decode().split("\n")
    extensions = []

    print(data)
    for item in data:
        if not item:
            continue
        pub_ext, version = item.split("@")
        pub, ext = pub_ext.split(".")
        extensions.append([pub, ext, version])

    return extensions


def download(publisher, ext, version):
    # 确保 extensions 目录存在
    os.makedirs("extensions", exist_ok=True)

    local_name = f"extensions/{publisher}.{ext}@{version}.vsix"
    if os.path.exists(local_name):
        print(f"exsis {local_name}-------------- skippppppppppppppp -----------------")
        return local_name
    redirectURL = f"https://{publisher}.gallery.vsassets.io/_apis/public/gallery/publisher/{publisher}/extension/{ext}/{version}/assetbyname/Microsoft.VisualStudio.Services.VSIXPackage"
    print(redirectURL)
    # content = requests.get(f"https://rajasimon.github.io/download-vsix?publisher={publisher}&extension={ext}&version={version}")
    with requests.get(redirectURL, stream=True) as r:
        with open(local_name, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

    return local_name


if __name__ == "__main__":
    editor = get_editor_choice()
    extensions = list_extensions(editor)
    scripts = []
    for ext in extensions:
        name = download(*ext)
        if editor == "vscode":
            scripts.append(f"code --install-extension {name}")
        else:
            scripts.append(f"cursor --install-extension {name}")

    with open("install.ps1", "w") as f:
        for line in scripts:
            f.write(line + "\n")
