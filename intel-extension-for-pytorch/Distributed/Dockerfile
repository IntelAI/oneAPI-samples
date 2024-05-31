ARG BASE_IMAGE
FROM $BASE_IMAGE as ray-ipex-cpu

RUN echo "unset BASH_ENV PROMPT_COMMAND ENV" >> ${CPU_ENV}/bin/activate

ENV BASH_ENV="${CPU_ENV}/bin/activate" \
    ENV="${CPU_ENV}/bin/activate" \
    PROMPT_COMMAND=". ${CPU_ENV}/bin/activate"

#Intall multi-node packages
RUN python -m pip install --no-cache-dir ray[data,train,tune,serve] && \
    python -m pip install --no-cache-dir --extra-index-url=https://pytorch-extension.intel.com/release-whl/stable/cpu/us/ oneccl_bind_pt==2.1.0
