#!/bin/sh

git log --date=short --pretty=format:"%ad : %s %b%n" --reverse > CHANGELOG
vi CHANGELOG
