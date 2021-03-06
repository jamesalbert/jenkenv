.ONESHELL:
.SHELL := /bin/bash
.PHONY: build-runner

package-runner:
	git submodule update --recursive --remote
	docker run -v `pwd`/jenkenv/jenkinsfile-runner:/src -w /src maven:3.5.2 mvn package

clean:
	rm -rf build dist jenkenv.egg-info

package: clean
	python setup.py sdist bdist_wheel
	twine upload --repository-url https://upload.pypi.org/legacy/ dist/*

install-locally:
	python setup.py install
	pyenv rehash
