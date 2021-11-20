# ~/.profile: executed by Bourne-compatible login shells.

if [ "$BASH" ]; then
  if [ -f ~/.bashrc ]; then
    . ~/.bashrc
  fi
fi

alias ..='cd ..'
alias python='python3'
function g() {
	git add -A
	git commit -m $1
	git push origin main
}

function archieve() {
	touch /workspace/PyQt_Asobi/Archieves/$1
	cat /workspace/PyQt_Asobi/index.py > /workspace/PyQt_Asobi/Archieves/$1
}

function update_profile() {
	touch /workspace/PyQt_Asobi/profile
	cat ~/.profile > /workspace/PyQt_Asobi/profile
	source ~/.profile
}

mesg n || true
parse_git_branch() {
  git branch 2> /dev/null | sed -e "/^[^*]/d" -e "s/* \(.*\)/(\1)/"
}
PS1="\[\e]0;\u@\h: \w\a\]${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$(parse_git_branch)\\$ "
alias git="LANGUAGE=en_US.UTF-8 git"
export HISTIGNORE="df /"
export PYTHONPATH=/goormService/caffe/python:$PYTHONPATH
