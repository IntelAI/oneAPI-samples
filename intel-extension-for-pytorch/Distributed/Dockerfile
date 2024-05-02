ARG BASE_IMAGE
FROM $BASE_IMAGE as ray-ipex-cpu

#Intall multi-node packages
RUN python -m pip install ray[data,train,tune,serve] && \
    python -m pip install --extra-index-url=https://pytorch-extension.intel.com/release-whl/stable/cpu/us/ oneccl_bind_pt==2.1.0
