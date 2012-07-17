#!/usr/bin/env bash

function clean () {
	find ${PWD} -iname '*.pyc' -exec rm -rf {} \;
	rm -rf ${PWD}/www/tmp/*
	rm -rf ${PWD}/www/log/*
}

trap clean SIGHUP SIGINT SIGTERM
clean
