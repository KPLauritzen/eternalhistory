# Eternal history

Never lose your command history.

## Setup
In your bashrc (or shell profile rc) add the following lines
```sh
HOSTNAME="$(hostname)"
HOSTNAME_SHORT="${HOSTNAME%%.*}"
HISTDIR="${HOME}/.history"
mkdir -p ${HISTDIR}/$(date -u +%Y/%m)
HISTFILE="${HISTDIR}/$(date -u +%Y/%m/%d-%H:%M)_${HOSTNAME_SHORT}_$$"
```

This creates a `.history` folder in your HOME dir and makes <YEAR>/<MONTH> subfolders.
Each terminal you start will create a file with the current date, time, hostname and PID.

Place `eternalhistory.py` somewhere in your `$PATH`. Search through your old commands by year, month and day.