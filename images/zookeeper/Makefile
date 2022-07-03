SHELL := /bin/bash
REG := quay.io
ORG := odra
NAME := zookeeper
TAG := latest
IMAGE := ${REG}/${ORG}/${NAME}:${TAG}
CRI := podman

build:
	@${CRI} build -t ${IMAGE} .

debug: build
	@${CRI} run -it --entrypoint /bin/bash ${IMAGE}

run: build
	@${CRI} run -it ${IMAGE}]

push: build
	@${CRI} push ${IMAGE}
