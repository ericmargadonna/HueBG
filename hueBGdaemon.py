#Written by Eric Margadonna
#January 21, 2021

import daemon
import hueBG

with daemon.DaemonContext():
    hueBG.main()
