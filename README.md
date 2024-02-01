# Welcome to Intel® oneAPI AI Analytics Toolkit on RedHat OpenShift Data Science!
This document covers the basics of Intel® oneAPI AI Analytics Toolkit (AI Kit) on Red Hat OpenShift Data Science for Data Science Projects. It provides information on where to access certain Intel AI optimizations within the AI Analytics Toolkit pre-built kernel environments, and more resources on examples and how to find more information on Intel® oneAPI AI Analytics Toolkit.

## Overview of Intel® oneAPI AI Analytics Toolkit
The Intel® oneAPI AI Analytics Toolkit gives data scientists, AI developers, and researchers familiar Python* tools and frameworks to accelerate end-to-end data science and machine learning pipelines on Intel® architectures. The components are built using oneAPI libraries for low-level compute optimizations. This toolkit maximizes performance from preprocessing through machine and deep learning phases and provides interoperability for efficient model development and deployment across single and multinodes. 

Using this toolkit, you can:

- Deliver high-performance deep learning (DL) training and inference on Intel® XPUs with Intel-optimized DL frameworks: TensorFlow* and PyTorch*, pretrained models, and low-precision tools.  

- Achieve drop-in acceleration for data preprocessing and machine learning workflows with compute-intensive Python packages: Modin*, Scikit-Learn*, and XGBoost* optimized for Intel.

- Seamlessly scale up and scale out to leverage AI compute continuum across single and multi nodes

- Gain direct access to Intel’s latest machine and deep learning optimizations in a single integrated package tested for interoperability.


## Table of Contents
1. [Intel® oneAPI AI Analytics Toolkit Pre-built Environment Packages Information](#sec-env)
2. [Intel® oneAPI AI Analytics Toolkit Getting Started Resources](#sec-gettingstarted)

<a id="sec-env"></a>
## 1. Intel® oneAPI AI Analytics Toolkit Environment Packages Information

You can find more detailed information on using the Intel® oneAPI AI Analytics Toolkit at <a href="https://www.intel.com/content/www/us/en/developer/tools/oneapi/ai-analytics-toolkit.html">AI Tools</a>. 

On RedHat OpenShift Data Science, we have provided some pre-installed AI Kit environments based on different workload needs:

**`Intel SKLearn, XGBoost, & Modin` Kernel Environment**
- <a href="https://software.intel.com/content/www/us/en/develop/tools/oneapi/components/distribution-of-modin.html">Intel® Distribution of Modin*</a>
- <a href="https://www.intel.com/content/www/us/en/developer/tools/oneapi/scikit-learn.html">Intel® Extension for Scikit-Learn*</a>
- <a href="https://software.intel.com/content/www/us/en/develop/tools/oneapi/components/distribution-for-python.html">Intel® Distribution for Python (including Intel optimizations for NumPy, SciPy, and Numba)</a>
- <a href="https://www.intel.com/content/www/us/en/developer/tools/frameworks/overview.html#xgboost">XGBoost Optimized for Intel Architecture</a>

**`Intel TensorFlow & Quantization` Kernel Environment**
- <a href="https://software.intel.com/content/www/us/en/develop/tools/frameworks.html#tensorflow">Intel® Optimization for TensorFlow</a>
- <a href="https://www.intel.com/content/www/us/en/developer/tools/oneapi/neural-compressor.html">Intel® Neural Compressor</a>
- <a href="https://github.com/IntelAI/models">Model Zoo for Intel® Architecture</a>

**`Intel PyTorch & Quantization` Kernel Environment**
- <a href="https://software.intel.com/content/www/us/en/develop/tools/frameworks.html#pytorch">Intel® Optimization for PyTorch</a>
- <a href="https://www.intel.com/content/www/us/en/developer/tools/oneapi/neural-compressor.html">Intel® Neural Compressor</a>
- <a href="https://github.com/IntelAI/models">Model Zoo for Intel® Architecture</a>

You can also create and install additional AI kit packages and environments on Red Hat OpenShift Data Science using <a href="https://www.intel.com/content/www/us/en/develop/documentation/installation-guide-for-intel-oneapi-toolkits-linux/top/installation/install-using-package-managers/conda/install-intel-ai-analytics-toolkit-via-conda.html">Conda* Package Manager</a>.

<a name="sec-gettingstarted"></a>
## 2. Intel® oneAPI AI Analytics Toolkit Getting Started Resources
As part of the Intel® oneAPI AI Analytics Toolkit on RedHat OpenShift Data Science, we have provided you several examples to help you get started with different AI Kit optimizations. These can be found in the `oneAPI-samples.git` directory.

For even more examples and information on AI Kit optimizations consider visiting the following resources:
- <a href="https://software.intel.com/en-us/oneapi/ai-kit">Intel® oneAPI AI Analytics Toolkit Website</a>
- <a href="https://github.com/oneapi-src/oneAPI-samples/tree/master/AI-and-Analytics">Intel® oneAPI AI Analytics Toolkit Code Samples</a>
- <a href="https://software.intel.com/content/www/us/en/develop/articles/oneapi-ai-analytics-toolkit-release-notes.html">Intel® oneAPI AI Analytics Toolkit Release Notes</a>

