md-tool is based on https://github.com/paulpierre/markdown-crawler, but it is purpose-built for this project.

It scrapes the docs.myshell.ai GitBook into cleaned up markdown files for me to use as prompting data. The point of making this was so that I could click & run it easily & often to update the reference documents known to the bot.

You can change the url at the top of update-docs.py to try other pages. It will create a new directory based on the url for you inside of ./docs.

If you would like to see it in usage for yourself, please execute the following:

From the root directory of this repo (i.e. `../` from this readme) execute the following:

- Install md-tool to your python env:
```pwsh
pip install ./md-tool
```

- run the updater script to refresh the docs folder.
```pwsh
./update-docs.py
```

Executing these commands from the root of the repo is important, due to reference paths in my lazy code. You're welcome! 😤

Thanks for the great starting point with this one, Paul!