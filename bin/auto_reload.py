#!/usr/bin/env python3
import subprocess
import sys
import asyncio
import os
import pathlib


class SubProcess:

    def __init__(self, cmd: str):
        self.cmd = cmd
        self.process = None

    async def start(self):
        if self.process is not None:
            raise ValueError("Process already started")
        s = self.cmd.split(" ")
        cmd, cmd_args = s[0], s[1:]
        self.process = await asyncio.create_subprocess_exec(
            cmd,
            *cmd_args,
            stdout=sys.stdout,
            stderr=sys.stderr,
            stdin=subprocess.PIPE,
        )

    async def restart(self):
        print("restarting..")
        self.process.terminate()
        await self.process.wait()
        self.process = None
        await self.start()


class FileWatcher:

    def __init__(self):
        self.files = self.find_files()

    @classmethod
    def find_files(cls):
        files = os.listdir(".")
        files = [pathlib.Path(".", f) for f in files if f.endswith(".py")]
        return set(files)

    @classmethod
    def last_modified(cls, file):
        statinfo = os.stat(file)
        return statinfo.st_atime_ns

    async def watch(self, on_change):
        last_modified = {}
        while True:
            for file in self.files:
                modified = self.last_modified(file)
                if modified > last_modified.get(file, modified):
                    if asyncio.iscoroutinefunction(on_change):
                        await on_change(file)
                last_modified[file] = modified
            await asyncio.sleep(1)


async def main(cmd):

    async def on_file_change(file):
        print("Changes detected, restarting.")
        await sub_proc.restart()

    sub_proc = SubProcess(cmd)
    watcher = FileWatcher()
    await sub_proc.start()
    await watcher.watch(on_change=on_file_change)


if __name__ == "__main__":
    command = " ".join(sys.argv[1:])
    print(f"Starting auto reload for: '{command}'")
    asyncio.run(main(cmd=command))
