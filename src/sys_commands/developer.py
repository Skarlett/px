from standard import online_cnt, uptime, total_cnt
from __init__ import Command

USE = True

def test(_):
  print "did you hear that..?"
  return "Someone, Finally!" # Callback

def setup(cmd):
  cmd.commands.extend([
    Command(online_cnt, ('-oc',), self_name=False),
    Command(total_cnt, ('-tc',), self_name=False),
    uptime, test
  ])