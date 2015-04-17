#Configure Recall client settings

RECALL_URL=http://localhost:8888/
RECALL_MON=$HOME/Documents/recall/client/histmon.py
RECALL_HISTORY_DIR=$HOME/.recall/histories

#Bash History Config
#References:
# http://unix.stackexchange.com/questions/1288/preserve-bash-history-in-multiple-terminal-windows
# http://unix.stackexchange.com/questions/1288/preserve-bash-history-in-multiple-terminal-windows#3055135
# http://tldp.org/HOWTO/Bash-Prompt-HOWTO/x264.html

#export HISTCONTROL=ignoredups
export HISTSIZE=10000
export HISTIGNORE="ls:ls -l:pwd:cd:cd .."
export HISTTIMEFORMAT='%b %d %H:%M:%S: '
shopt -s histappend    # append to history, don't overwrite it
export PROMPT_COMMAND="history -a; history -c; history -r;"
export HISTFILE=$RECALL_HISTORY_DIR/hist.`echo $HOSTNAME | cut -d. -f1`_`date +%F`.txt

export RECALL_URL
export HOSTNAME
python $RECALL_MON $HISTFILE &
MONPID=$!
trap 'kill $MONPID' EXIT