#!/usr/bin/env python
import banner_config
try:
    import main
    main.start_main_script()
except KeyError:
    print("Script is supports only Desktop!.".center(banner_config.terminal_size))
