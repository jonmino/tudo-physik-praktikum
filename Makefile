TOPTARGETS := all clean

SUBDIRS := $(wildcard v*/.)

listdirs:
	# List of directories: $(SUBDIRS)

$(TOPTARGETS): $(SUBDIRS)

$(SUBDIRS):
	$(MAKE) -C $@ $(MAKECMDGOALS)

v%: FORCE
	$(MAKE) -C v$* all

c%: FORCE
	$(MAKE) -C v$* clean

FORCE:

.PHONY: $(TOPTARGETS) $(SUBDIRS)