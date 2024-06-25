#!/bin/bash

if [ -z "$1" ]; then
  echo "Please provide the name of the new environment. Exiting."
  return
fi

CONDA_ENV=$1

echo "Checking whether $CONDA_ENV exists..."
if [ -n "$(conda env list --json | grep "\\\\${CONDA_ENV}\"")" ]; then
  echo "The environment already exists. Exiting."
  return
fi

echo "It does not exist. Creating the new conda environment."
echo conda create --yes --name $CONDA_ENV "python==3.9.*"
conda create --yes --name $CONDA_ENV "python==3.9.*"

install_local_package(){
    echo cd $1
    cd $1
    echo conda run -n $CONDA_ENV pip install -e .
    conda run -n $CONDA_ENV pip install -e .
    echo cd -
    cd -
}

conda run -n $CONDA_ENV python -m pip install sphinx

install_local_package .
