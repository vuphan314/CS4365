<h6>top

# KNOTTY
computer algebra system for knot theory

## GOAL
to assist mathematicians with symbolic computation
- example: verification of some formulas in these papers
  (published in the Journal of Knot Theory and Its Ramifications):
  - [(2, 2*p + 1)-torus knot][paperTorus]
  - [figure-eight knot][paperFigure8]

## DESCRIPTION
the Knotty system includes:
- the Knotty language: a programming language for math,
  specializing in knot theory
- the Knotty engine:
  - receives a source file (in the Knotty language)
    - example:
      ```
      def p(x) return (1 + x) * (x^-1 + 1) - 3

      def c return p(1)

      ```
  - returns a simplified file (in the Knotty language)
    - example:
      ```
      def p(x) return x - 1 + x^-1

      def c return 1

      ```
- the Knotty webapp
  - includes:
    - a text box: in which the user can type a source file
    - a button: when clicked will simplify the source file
      (by invoking the Knotty engine)
    - a preview box: in which the simplified file is shown
  - is similar to the [SPARC webapp][sparcWeb]

## LINKS
- [demo webapp][demoWebapp]
- [kanban][trello]
- [documentation][onedrive]

## FILES
`code/`
- `knengine/`: Knotty engine
- `webapp/`: web application

## SETUP GUIDE
- first time:
  - install latest
    - [Python][pythonDownload]
    - [Git][gitDownload]
  - command-line interface:
    ```
    pip install mpmath

    pip install sympy

    ```
  - browse directory (Windows Command Prompt):
    ```
    cd/d <parent_dir_of_repo>

    ```
    example: my `<parent_dir_of_repo>` is `D:/repos/`
  - clone repository:
    ```
    git clone --recursive https://github.com/vuphan314/CS4365

    ```
- each following time:
  - browse directory:
    ```
    cd/d <dir_of_repo>

    ```
    example: my `<dir_of_repo>` is `D:/repos/CS4365/`
  - update repository:
    ```
    git pull --prune

    ```
  - browse tag:
    ```
    git checkout tags/v0.1.0

    ```
    note: [all releases][githubReleases]

## CONTRIBUTION GUIDE
- switch branch:
  ```
  git checkout branchzach

  ```  
- create/change your folders/files
- tell Git:
  ```
  git add --all

  git commit --all --message "say what you did"

  git push

  ```

## ACKNOWLEDGEMENT
- [Git submodule][gitmodules]: [generic parser][genparserSpec]
  - by [Evgenii Balai][evgeniiGithub]
- Python package: [SymPy][sympyHome]

[paperTorus]:
http://www.math.ttu.edu/~rgelca/gs6.pdf
[paperFigure8]:
http://www.math.ttu.edu/~rgelca/jr5.pdf

[sparcWeb]:
http://ec2-52-25-88-7.us-west-2.compute.amazonaws.com/

[demoWebapp]:
http://99.64.48.184/
[trello]:
https://trello.com/b/tCAfkInX
[onedrive]:
https://1drv.ms/f/s!Asl14HFRStFKgZlSCNCMQ4qIWcOoIg

[pythonDownload]:
https://www.python.org/downloads/
[gitDownload]:
https://git-scm.com/downloads

[githubReleases]:
https://github.com/vuphan314/CS4365/releases

[gitmodules]:
https://github.com/vuphan314/CS4365/blob/master/.gitmodules
[genparserSpec]:
https://github.com/iensen/genparser/blob/master/docs/main/astgen.pdf
[evgeniiGithub]:
https://github.com/iensen

[sympyHome]:
http://www.sympy.org/en/index.html
