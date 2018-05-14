#!/bin/bash

git add -A
read MSG
git commit -m "$MSG"
git push
