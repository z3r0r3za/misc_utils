# Miscellaneous Tools

Different tools for automating tasks.

- extconvert.py - For converting files to markdown as a code block for Obsidian.

I like to save what I type in each tmux buffer to a log file. When I want to put the log files in my notes I need to convert it to an md file (markdown) and then I like to wrap the contents with backticks so I put the 3 backticks at the top with the type of code and 3 backticks at the bottom to make it a code block in Obsidian. Doing this manually for each file can become a little tedious. So this utility will loop through all the files in a directory and do all that in one go. You can swap to the md extension from js, html, php, bash, shell or whatever type you need, and change the type of code block it needs to be in Obsidian.

tmux_buffer.log -> tmux_buffer.md
script.js -> script.md

...working on more scripts and will put them here as time permits.
