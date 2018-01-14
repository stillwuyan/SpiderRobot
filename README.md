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
  pipenv install patool
  ```

4. Create spider project

   ```
   pipenv shell
   scrapy startproject subtitles
   cd subtitles
   scrapy genspider zimuku www.zimuku.cn
   ```

   1. Crawl `http://www.zimuku.cn` with movie name and output file name

      ```
      scrapy crawl -a movie='intern' -s file='subtitles.json' zimuku
      ```

   2. Crawl `http://www.zimuku.cn` for test

      ```
      scrapy shell "http://www.zimuku.cn"
      ```

5. Run python script file

   ```
   pipenv run python run.py
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

# Setup ESLint for Sublime Text 3

+ Install nodejs and ESLint
   ```
   npm install -g eslint babel-eslint
   ```

+ Install SublimeLinter and SublimeLinter-eslint on Sublime Text
   1. `Ctrl+Shift+P`
   2. Input `Install Package`
   3. Input `SublimeLinter` and press `Enter`
   4. `Ctrl+Shift+P`
   5. Input `Install Package`
   6. Input `SublimeLinter-eslint` and press `Enter`

+ Initialize eslintrc file in the project
   ```
   cd ${PROJECT_PATH}
   eslint --init
   ```