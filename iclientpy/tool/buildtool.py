import os
import sys
import platform
import shutil
import subprocess


def writedir2file(path, targetfile):
    for root, dirs, files in os.walk(path):
        for file in files:
            targetfile.write(os.path.join(root, file), os.path.join(root, file)[len(path):])


def window_task(tool_file, dir):
    import zipfile
    zipf = zipfile.ZipFile(tool_file, 'w', zipfile.ZIP_DEFLATED)
    writedir2file(dir, zipf)
    zipf.close()


def linux_task(tool_file, dir):
    import tarfile
    tarf = tarfile.open(tool_file, 'w')
    tarf.write = tarf.add
    writedir2file(dir, tarf)
    tarf.close()


def delete_dirs(dirs):
    for dir in dirs:
        if os.path.exists(dir):
            shutil.rmtree(dir)


def main():
    rootdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
    icpy_dir = os.path.join(rootdir, 'build', 'icpy')
    tokentool_dir = os.path.join(rootdir, 'dist', 'tokentool')
    cachetool_dir = os.path.join(rootdir, 'dist', 'cachetool')
    initserver_dir = os.path.join(rootdir, 'dist', 'initserver')
    delete_dirs([icpy_dir, tokentool_dir, cachetool_dir])
    pyinstaller_cmd = ['pyinstaller', '--clean', '-y', '-c', 'icpy.spec']
    subprocess.check_call(pyinstaller_cmd, cwd=rootdir)
    for dir in [tokentool_dir, initserver_dir]:
        for root, dirs, files in os.walk(dir):
            for file in files:
                shutil.copy(os.path.join(dir, file), cachetool_dir)
    sysstr = platform.system()
    if (sysstr == "Windows"):
        tool_file = os.path.join(rootdir, 'tool', 'icpy-tools.zip')
        task = window_task
    elif (sysstr == "Linux"):
        tool_file = os.path.join(rootdir, 'tool', 'icpy-tools.tar')
        task = linux_task
    else:
        raise Exception('操作系统暂不支持')
    if os.path.exists(tool_file):
        os.remove(tool_file)
    task(tool_file, cachetool_dir)


if __name__ == '__main__':
    main()
