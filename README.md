# datavisualization_courses

## git command
to download git repository (or use ssh):   
```
git clone https://github.com/JujuDesFruits/Tell-me-a-story.git
```
create your own branch   
```
git checkout -b "name_branch"
```
do your updates   
to push updates to the main branch   
```
git add .
git commit -m "explicit_modification_flag"
git push --set-upstream origin name_branch
```
click on the link to complete pull request.   
to keep your own branch update:   
```
git checkout master
git pull
git checkout "name_branch"
git pull . master
```

## initialize workspace
I'm using visual studio code to work and here is how to initialize workspace :   
- install jupyter extension and python in *VS code*
- download this repository into your workspace
- into *VS code* terminal type :   
```
pip install --upgrade pip
```   
```
pip install matplotlib
```   
```
pip install pandas
```   