# Initialize spider project
1. Create workspace directory
  ```
  mkdir spider
  cd spider
  ```

2. Install python environment
  ```
  pip install pipenv
  ```

3. Install dependencies
  ```
  curl -O https://download.lfd.uci.edu/pythonlibs/gjr6o2id/Twisted-17.9.0-cp36-cp36m-win_amd64.whl
  pipenv install ./Twisted-17.9.0-cp36-cp36m-win_amd64.whl
  pipenv install scrapy
  pipenv install pypiwin32
  ```

4. Create spider project

   ```
   pipenv shell
   scrapy startproject subtitles
   cd subtitles
   scrapy genspider zimuku www.zimuku.cn
   ```

   1. Crawl `http://www.zimuku.cn` with movie name

      ```
      scrapy crawl -a movie='intern' zimuku
      ```

   2. Crawl `http://www.zimuku.cn` for test

      ```
      scrapy shell "http://www.zimuku.cn"
      ```

5. Run python script file

   ```
   pipenv run python script.py
   ```

6. Install from the Pipfile.lock

   ```
   pipenv install --ignore-pipfile
   ```

7. Install from requirements.txt

   ```
   pipenv install -r path/to/requirements.txt 
   ```


# Create http server

+ `python -m http.server 8000`
+ `python -m webbrowser -t "http://localhost:8000"`

