import util.delete_util as delutil
from dome import multichannelapp as MUP

# deleting the old gen files
# delutil.deleteOldManagedFiles()

# MUP.MultiChannelApp(run_telegram=False, run_server=True) # to run server http
MUP.MultiChannelApp(run_telegram=True, run_server=False) # to run telegram bot  
