PYTHON ?= python3
ROOT := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
SLUG ?= master

ifeq ($(SLUG),master)
  YAML := $(ROOT)master/resume.yaml
  OUT  := $(ROOT)output/master
else
  YAML := $(ROOT)output/$(SLUG)/resume.yaml
  OUT  := $(ROOT)output/$(SLUG)
endif

BUILD_DIR := $(OUT)/build
PDF       := $(shell $(PYTHON) $(ROOT)scripts/resolve_pdf.py $(SLUG))

.PHONY: docker-build render build build-master build-variant upload-variant validate install-deps

docker-build:
	docker build -t resume-tailor-tex $(ROOT)

render:
	$(PYTHON) $(ROOT)scripts/render.py --yaml $(YAML) --out $(BUILD_DIR)

build: render
	chmod +x $(ROOT)scripts/build.sh
	$(ROOT)scripts/build.sh $(BUILD_DIR) $(PDF)

build-master:
	$(MAKE) build SLUG=master

build-variant:
	@test -f $(YAML) || (echo "Missing $(YAML). Run tailor-resume first." && exit 1)
	$(MAKE) build SLUG=$(SLUG)

upload-variant:
	@test -f $(PDF) || (echo "Missing $(PDF). Run build-variant first." && exit 1)
	$(PYTHON) $(ROOT)scripts/upload_to_mongo.py --slug $(SLUG) $(UPLOAD_ARGS)

validate:
	$(PYTHON) $(ROOT)scripts/migrate_tex_to_yaml.py --yaml $(YAML)

install-deps:
	$(PYTHON) -m pip install -r $(ROOT)requirements.txt
