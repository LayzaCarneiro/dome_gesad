import util.delete_util as delutil
from dome import multichannelapp as MUP

# deleting the old gen files
# delutil.deleteOldManagedFiles()

MUP.MultiChannelApp(run_server=True, run_telegram=False)
