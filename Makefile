# Required program
SHELL               := /bin/bash
NMLC                ?= nmlc
PYTHON              ?= python3

# C compiler
CC                  ?= cc
CC_FLAGS            ?= -C -E -nostdinc -x c-header
CP_FLAGS            ?= $(shell [ "$(OSTYPE)" = "Darwin" ] && echo "-rfX" || echo "-rf")
CC_USER_FLAGS       ?=

# Configurations
-include Makefile.config

# Disable default suffixes rule
.SUFFIXES:

.PHONY: all build clean download_page doc generated bundle bundle_tar

# File names
DIR_NAME            ?= $(shell echo "$(REPO_NAME) $(VERSION)" | xargs | sed s/\ /_/g)
GRF_FILE            ?= $(BASE_FILENAME).grf
NML_FILE            ?= $(BASE_FILENAME).nml
NFO_FILE            ?= $(BASE_FILENAME).nfo
PNML_FILE           ?= $(BASE_FILENAME).pnml
TAG_FILE            ?= custom_tags.txt
DOC_FILE            ?= docs/readme.txt docs/license.txt docs/changelog.md

GRF_GENERATE        ?= $(BASE_FILENAME).grf
NML_GENERATE        ?= $(BASE_FILENAME).nml
NFO_GENERATE        ?= $(BASE_FILENAME).nfo
PNML_GENERATE       ?= $(BASE_FILENAME).pnml
TAR_GENERATE        ?= $(BASE_FILENAME).tar
TAG_GENERATE        ?= custom_tags.txt
DOC_GENERATE        ?= $(DOC_FILE)
BUNDLE_FILES        ?= $(GRF_FILE) $(DOC_FILE)

# target 'all' must be first target
all: build

build: $(GRF_GENERATE) doc bundle_tar
	@echo "... $(VERSION) has built"

# Generate *.txt from *.ptxt
%.txt: %.ptxt generated
	@echo "[DOC] $@"
	@cat $< | sed -e "s/{{\VERSION}}/$(VERSION)/" > ./generated/$(notdir $@)
clean::
	@-rm -rf ./generated/readme.txt

# Documents
doc: generated $(DOC_GENERATE) $(GRF_GENERATE)
	@cp $(CP_FLAGS) ./docs/license.txt ./generated/license.txt
	@cp $(CP_FLAGS) ./docs/changelog.md ./generated/changelog.md
clean::
	@echo "[CLEAN DOC]"
	@-rm -rf ./generated/*.txt
	@-rm -rf ./docs/readme.txt


# Make generated directory
generated:
	@echo "[MKDIR generated]"
	@if [ ! -e $@ ]; then mkdir $@; fi
clean::
	@echo "[CLEAN generated]"
	@-rm -rf ./generated

# Generate *.nml from *.pnml
$(NML_GENERATE): generated $(PNML_GENERATE)
	@echo "[CPP] $@"
	@ $(CC) -D VERSION=$(VERSION) $(CC_USER_FLAGS) $(CC_FLAGS) -o ./generated/$(NML_FILE) $(PNML_FILE)
clean::
	@echo "[CLEAN NML]"
	@-rm -rf $(NML_FILE)

# Generate custom_tags.txt
$(TAG_GENERATE): generated
	@echo "[TAG] $@"
	@echo "VERSION        :$(VERSION)"         > ./generated/$@
	@echo "RECENT_UPDATED :$(RECENT_UPDATED)" >> ./generated/$@
	@echo "AUTHOR_WEBSITE :$(AUTHOR_WEBSITE)" >> ./generated/$@
	@echo "AUTHOR_EMAIL   :$(AUTHOR_EMAIL)"   >> ./generated/$@
clean::
	@echo "[CLEAN TAG]"
	@-rm -rf $(TAG_FILE)

# Generate spec.pnml
spec.pnml: generated
	$(PYTHON) ./src/spec.py
clean::
	@echo "[CLEAN spec.pnml]"
	@-rm -rf ./generated/spec.pnml

# Generate *.grf
$(GRF_GENERATE): generated spec.pnml $(NML_GENERATE) $(TAG_GENERATE)
	@echo "[NMLC] $@"
	@ $(NMLC) -c --custom-tags="./generated/$(TAG_FILE)" --lang-dir="./lang/" "./generated/$(NML_FILE)" --grf="./generated/$(GRF_FILE)"
clean::
	@echo "[CLEAN GRF]"
	@-rm -rf $(GRF_FILE)

$(NFO_GENERATE):
clean::
	@echo "[CLEAN NFO]"
	@-rm -rf $(NFO_FILE)

# Make a bundle
bundle: bundle_tar
bundle_tar: $(BUNDLE_FILES)
	@echo "[BUNDLE TAR]"
	@ tar -cf generated/$(DIR_NAME).tar generated/changelog.md generated/$(GRF_FILE) generated/license.txt generated/readme.txt --transform s/generated/$(DIR_NAME)/
clean::
	@echo "[CLEAN BUNDLE]"
	@-rm -rf $(shell echo "$(REPO_NAME)*" | xargs | sed s/\ /_/g)

# Clean
clean::
	@-rm -rf ./.nmlcache
	@-rm -rf ./src/__pycache__

# Install (Temporarily used for developments)
# dev: build
# 	@cp -r ./generated/$(DIR_NAME).tar /mnt/d/Games/OpenTTD/Nightly/newgrf/Korean_Train_Set-dev.tar
# clean::
# 	@-rm -rf /mnt/d/Games/OpenTTD/Nightly/newgrf/Korean_Train_Set-dev.tar
