#!/usr/bin/env python

import os
import sys
import argparse


def get_arguments():
    parser = argparse.ArgumentParser(
        # Don't escape the \n like it's done here in the example. See printed help.
        # The escape is here so that it prints correctly when using "extconvert.py -h".
        description="A utility that preps a tmux log file for Obsidian.",
        epilog="""
            Example:
            python3 extconvert.py -d "/dir/of/files" -o log -n md -t "\\n```shell\\n" -b "```\\n"
        """,
    )
    parser.add_argument(
        "-d", "--directory", dest="directory", help="The directory: /files/in/here"
    )
    parser.add_argument(
        "-o", "--oldextension", dest="oldextension", help="The old extension: log"
    )
    parser.add_argument(
        "-n", "--newextension", dest="newextension", help="The new extension: md"
    )
    parser.add_argument("-t", "--top", dest="top", help="Text to insert at the top.")
    parser.add_argument(
        "-b", "--bottom", dest="bottom", help="Text to insert at the bottom."
    )
    args = parser.parse_args()
    if not args.directory:
        parser.error("[-] Please specify a directory")
    elif not args.oldextension:
        parser.error("[-] Please specify the old extension.")
    elif not args.newextension:
        parser.error("[-] Please specify the new extension.")
    elif not args.top:
        parser.error("[-] Please specify text for the top.")
    elif not args.bottom:
        parser.error("[-] Please specify text for the bottom.")
    return args


opt = get_arguments()
folder = opt.directory
ox = opt.oldextension
nx = opt.newextension
top = opt.top
bot = opt.bottom

# .encode('utf-8')


def prepend(filename, top, bot):
    # Fix \n - new lines from input so they are working.
    top = top.replace("\\n", "\n")
    bot = bot.replace("\\n", "\n")
    # Make a backup of the file.
    backupname = filename + os.extsep + "bak"
    try:
        os.unlink(backupname)  # remove previous backup if it exists
    except OSError:
        pass
    os.rename(filename, backupname)
    # Open input/output files. Outputfile's permissions will be lost.
    with open(backupname) as inputfile, open(filename, "w") as outputfile:
        # Prepend text to file.
        outputfile.write(top)
        # Copy the rest of the file.
        buf = inputfile.read()
        while buf:
            outputfile.write(buf)
            # Append text to file.
            outputfile.write(bot)
            buf = inputfile.read()
    # Remove the backup after it succeeds.
    try:
        os.unlink(backupname)
    except OSError:
        pass


def ext_replace(folder, ox, nx, top, bot):
    # Save extensions in dictionary.
    # extensions = {'log': 'md'}
    extensions = {ox: nx}
    # Loop through sorted list of files amd replace extensions.
    # Use prepend() to get text ready to display as code in markdown.
    for fn in sorted(os.listdir(folder)):
        # prepend(f"{folder}/{fn}", "\n```shell\n", "```\n")
        # Wrap text with 3 backticks for code block in markdown.
        prepend(f"{folder}/{fn}", top, bot)
        # Save file name, extension and remove the dot/period.
        file_name, ext = os.path.splitext(fn)
        ext = ext.replace(".", "")
        # If you have the extension that needs to be changed.
        if ext in extensions:
            # Set up the file name with the new extension.
            new_ext = extensions[ext]
            new_file_name = file_name + "." + new_ext
            # Set up the absolute paths for the old and new file names.
            pervious_path = os.path.join(folder, fn)
            new_path = os.path.join(folder, new_file_name)
            # Rename the file to have the new extension.
            os.rename(pervious_path, new_path)


if __name__ == "__main__":
    try:
        # folder ="C:/Users/Mooky/Test Notes"
        # folder = "/home/kali/Work/PEH/AD_REVIEW/01_INITIAL/tmux_buffers/md"
        ext_replace(folder, ox, nx, top, bot)

    except Exception as e:
        print("MAIN - Error Return Type: ", type(e))
        # print(e)
