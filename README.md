# README

<img width="500" alt="Screen Shot 2022-03-24 at 18 21 14" src="https://user-images.githubusercontent.com/58789864/159963920-c46e7e28-da7b-42a0-8865-d769cf1d1f8b.png">

## Setup

### Install brew dependencies
```sh
brew install watch
brew install harfbuzz
```

### Install perl dependencies
```sh 
sudo perl -MCPAN -e shell

install Font::TTF::Font
install Text::Unicode::Equivalents
```

### Install python dependencies
```sh 
pip3 install fontTools
```

### Install font ttf scripts
```sh
git clone https://github.com/silnrsi/font-ttf-scripts.git
cd font-ttf-scripts
perl Makefile.PL
make
sudo make install
```


## Usage

`make watch`
