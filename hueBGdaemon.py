import daemon
import hueBG

with daemon.DaemonContext():
    hueBG.main()