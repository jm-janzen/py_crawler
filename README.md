# Simple CLI Python Webcrawler example

## Package Requirements
`Python-v3.5.2`, `Geckodriver-v0.11.1-linux64`

## Python Module Requirements
`Selenium-v3.0.2`, `Xvfbwrapper-0.2.8`

---

### Install Python modules [locally]
```bash
pip install [--user] selenium
pip install [--user] xvfbwrapper
```

### Install FF webdriver
- Browse binaries: [geckdriver](https://github.com/mozilla/geckodriver/releases) (v0.11.1)
```bash
# download
wget https://github.com/mozilla/geckodriver/releases/download/v0.11.1/geckodriver-v0.11.1-linux64.tar.gz

# unpack tarball
tar xf geckodriver-v0.11.1-linux64.tar.gz

# add unpacked bin to PATH env (NB: This should be added to an upstart script!)
export PATH="$PATH:/path/to/geckodriver/dir"
```

### Running
```bash
python crawler.py <URL> <ATTR>  # Some HTML attribute to search for
```

