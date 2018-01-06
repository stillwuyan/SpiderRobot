# Initialize project
1. create workspace directory
  ```
  mkdir spider
  cd spider
  ```

2. install python environment
  ```
  pip install pipenv
  ```

3. install dependencies
  ```
  curl -O https://download.lfd.uci.edu/pythonlibs/gjr6o2id/Twisted-17.9.0-cp36-cp36m-win_amd64.whl
  pipenv install ./Twisted-17.9.0-cp36-cp36m-win_amd64.whl
  pipenv install scrapy
  pipenv install pypiwin32
  ```

4. create spider project

   ```
   pipenv shell
   scrapy startproject subtitles
   cd subtitles
   scrapy genspider zimuku www.zimuku.cn
   ```

   1. crawl `http://www.zimuku.cn` with movie name

      ```
      scrapy crawl zimuku -a movie='intern'
      ```

   2. crawl `http://www.zimuku.cn` for test

      ```
      scrapy shell "http://www.zimuku.cn"
      ```

5. run python script file

   ```
   pipenv run python script.py
   ```

6. install from the Pipfile.lock

   ```
   pipenv install --ignore-pipfile
   ```

7. install from requirements.txt

   ```
   pipenv install -r path/to/requirements.txt
   ```

