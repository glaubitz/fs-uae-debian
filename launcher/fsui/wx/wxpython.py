#import sys
#if not hasattr(sys, "frozen"):
#    try:
#        import wxversion
#    except ImportError:
#        pass
#    else:
#        try:
#            wxversion.select(["2.8"])
#        except wxversion.VersionError as e:
#            # if a new interpreter is started with sys.executable on
#            # Mac, sys.frozen may not be set, so we allow/ignore
#            # this error
#            print(repr(e))

wx = None
