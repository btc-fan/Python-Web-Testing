# Form submission and Captcha breaker for https://www.optoutprescreen.com/

## Before testing ensure you have following libraries installed

### First install pyenv as follows:
### Required python version >=3.6.2

```
Brew install:
brew install pyenv
pyenv install 3.6.0

Or my working method:
CFLAGS="-I$(brew --prefix openssl)/include -I$(brew --prefix bzip2)/include -I$(brew --prefix readline)/include -I$(xcrun --show-sdk-path)/usr/include" LDFLAGS="-L$(brew --prefix openssl)/lib -L$(brew --prefix readline)/lib -L$(brew --prefix zlib)/lib -L$(brew --prefix bzip2)/lib" pyenv install --patch 3.6.0 < <(curl -sSL https://github.com/python/cpython/commit/8ea6353.patch\?full_index\=1)

```

### Then check python version

```
python --version
pyenv local 3.6.0
```

### Proceed with tensorflow installation.

```
install --upgrade pip
pip install tensorflow==1.15.5

```

### Now proceed with requirements installation

```
pip install -r requirements.txt

```

# Note

## Open every script and correct the paths accordingly

## In order to extract image information for model training please use labelImg tool. Download it from here:

```
git clone https://github.com/tzutalin/labelImg.git
pip install PyQt5
```

# Push big size file to git:

```
brew install git-lfs
git lfs install
git lfs track "*.pb"
git lfs track "*.ckpt"
git lfs track "models/**"
git commit -m "first commit"
git push origin main

git lfs untrack "*.zip"
git add --renormalize .
git commit -m 'Restore file contents that were previously in LFS'

```

# Proto building for models:

## Models is considered builded if models/research/object_detection/protos have python scritps with \_pb2 at the end: Example name anchor_generator_pb2.py

```
git clone https://github.com/tensorflow/models
cd research
protoc object_detection/protos/*.proto --python_out=.

```

# Pay attention to other .txt files in current project with python commands and explanations
```
pyenv install 3.6.2 --patch <<(curl -sSL https://github.com/python/cpython/commit/8ea6353.patch)
```
