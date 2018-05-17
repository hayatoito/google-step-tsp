Google STEP 2018: Travelling Salesman Problem Challenges
====

[Hayato Ito](https://github.com/hayatoito) (hayato@google.com)

Quick Links
----

- [Scoreboard]
- [GitHub Issues]

[scoreboard]: https://docs.google.com/spreadsheets/d/1Aa_NNQf7sFANuHKt0FTvUBQ83QO3OOKZjifhsmjOxqc/edit?usp=sharhing
[GitHub Issues]: https://github.com/hayatoito/google-step-tsp/issues

Problem Statement
----

In this assignment, you will design an algorithm to solve a fundamental problem
faced by every travelling salesperson, called *Travelling Salesman Problem*
(TSP).  I’ll explain TSP in the onsite class.  TSP
is very famous problem. See [Wikipedia](http://en.wikipedia.org/wiki/Travelling_salesman_problem).
You can understand the problem without any difficulties.

Quoted from [Wikipedia](http://en.wikipedia.org/wiki/Travelling_salesman_problem):

> The travelling salesman problem (TSP) asks the following question: Given a
> list of cities and the distances between each pair of cities, what is the
> shortest possible route that visits each city exactly once and returns to the
> origin city?

Assignment
----

The assignment is hosted on GitHub, [https://github.com/hayatoito/google-step-tsp](https://github.com/hayatoito/google-step-tsp).
You can download the assignment by `git clone`:

    git clone https://github.com/hayatoito/google-step-tsp
    git checkout gh-pages

I recommend you to [fork](https://help.github.com/articles/fork-a-repo/) this
repository to your github account before cloning it.

This document doesn't explain “what is git?’ nor “how to use GitHub?”. It is your responsibility to master the
usage of git and GitHub.

The repository includes sample scripts written in Python 3, rather than in Python 2. It’s your responsibility to
install Python 3 if you want to run the scripts, though running the scripts is not mandatory.

There are 7 challenges of TSP in the assignment, from N = 5 to N = 2048:

  | Challenge    | N (= the number of cities) | Input file  | Output file            |
  | ------------ | -------------------------: | ----------- | ---------------------- |
  | Challenge 0  |                          5 | input_0.csv | output_0.csv               |
  | Challenge 1  |                          8 | input_1.csv | output_1.csv               |
  | Challenge 2  |                         16 | input_2.csv | output_2.csv               |
  | Challenge 3  |                         64 | input_3.csv | output_3.csv               |
  | Challenge 4  |                        128 | input_4.csv | output_4.csv               |
  | Challenge 5  |                        512 | input_5.csv | output_5.csv               |
  | Challenge 6  |                       2048 | input_6.csv | output_6.csv               |

See *Data Format Specification* section to know the format of input and output files.

### Your tasks

In coding phase:

* Write a program, solveing each TSP by designing and implementing an algorithm.
* Overwrite each output file, `output_{0-6}.csv`, with the output of your program.
* Enter the *path length* of your solution in the [scoreboard], for each challenge. Needless to say, a shorter path is better then a longer path.
* Enter your git repository's location in the [scoreboard].

### An optional task (Speed challenge)

What matters in this optional task is your program's *speed* (execution time). The path length does not matter as long as it is meets the condition.

Your task is: Given `input_6.csv`, write a program which outputs a path shorter than `47,000`

Input your program's execution time in the [scoreboard]. Faster (smaller) is better.

You can measure the execution time by `time` command. For example,

```shellsession
$ time yourprogram input_6.csv solution_yours_6.csv
2.96s user 0.07s system 97% cpu 3.116 total
```

In this case, your score is `3.116` (s).

### Visualizer

The demo page of the visualizer is [here](http://hayato.io/google-step-tsp/visualizer/build/default/).

The assignment includes a helper Web page, `visualizer/build/default/index.html`, which
visualizes your solutions. You need to run a HTTP server on your local machine
to access the visualizer. Any HTTP server is okay. If you are not sure how to
run a web server, use the following command to run the HTTP server included in
the assignment. Make sure that you are in the top directory of the assignment
before running the command.

``` shellsession
python3 -m http.server
# python2 -m SimpleHTTPServer # If you don’t have Python 3
```

Then, open a browser and navigate to the
[http://localhost:8000/visualizer/build/default/](http://localhost:8000/visualizer/build/default/).

Visualizer was only tested by Google Chrome. Using the visualizer is up-to you. You don’t have to use the visualizer to finish the assignment. The
visualizer is provided for the purpose of helping you understand the problem.

Once you publish a git repository, you can also enter the URL of a visualizer for your solutions in the [scoreboard]
(e.g. [http://your_github_account_name.github.io/google-step-tsp/visualizer/build/default/](http://your_github_account_name.github.io/google-step-tsp/visualizer/build/default/)).

Data Format Specification
----

### Input Format

The input consists of `N + 1` lines. The first line is always `x,y`. It is followed by `N` lines, each line represents an i-th city’s location, point `xi,yi` where `xi`, `yi` is a floating point number.

```
x,y
x_0,y_0
x_1,y_1
…
x_N-1,y_N-1
```

### Output Format

Output has `N + 1` lines. The first line should be “index”. It is followed by `N` lines, each line is the index of city, which represents the visitation order.

```
index
v_0
v_1
v_2
…
v_N-1
```

### Example (Challenge 0, N = 5)

Input Example:

```
x,y
214.98279057984195,762.6903632435094
1222.0393903625825,229.56212316547953
792.6961393471055,404.5419583098643
1042.5487563564207,709.8510160219619
150.17533883877582,25.512728869805677
```

Output (Solution) Example:

```
index
0
2
3
1
4
```

These formats are requirements for the visualizer, which can take only properly formatted CSV files as input.

Schedule
----

### The class begins: 2018-06-22 (Fri) 5:00pm (JST)

The class starts. You are strongly encouraged to bring your laptop.

Befoer explaining assignments, I'll give you a special lecture, called "How the computer works" at the beginning.

Then, I'll explain this "TSP" assignements.
You are expected to understand the problem and solve a challenge with a small N in the class, if we have enough time.

### Coding phase: From: 2018-06-22 (Fri) 8:00pm - To: 2017-06-29 (Fri) 5:00pm

The deadline of the final submission is the next Friday.

Until the deadline, you are expected to improve your algorithm and enter the
score in the [scoreboard] manually for each challenge. You can update the score
as many times as needed. I highly recommend you to update your score whenever
you can find a shorter path.

You can enter your git repository's location in the [scoreboard] once it is ready. Publish your git repository as soon as possible.
Other participants want to see your code even if your code is work in progress.

You can also enter the visualizer URL so that other students can see how your
salesperson is visiting each city in your solution.

Note:

- You can see and use code written in other students freely.
- Please try to publish your code as much as possible so that other students can see your code.

#### (Optional) Office hours: (2017-06-26 (Tue) 5:00pm - )

I will hold office hours on next Tuesday at Google Tokyo office. I will be available until nealy 10:00pm. You can come anytime and leave anytime.

How to attend office hours: I will announce it later at [GitHub Issues] or other places.

As a bunus for ofifce hours attendees, I have a plan to explain the advanced topics very roughly: 'Understand how program runs, in a hard way'.

These topcs are very basic fundamental knowledge to understand how your program (and/or programming languages) runs and are represened in your computer. These are optional topics, but if are interested in, please join us anytime.

#### (Optional) Yet another optional task: Challenge 7: 2017-06-27 (Wed)

I will announce it on 2017-06-28 (Wed) at [GitHub Issues].

What’s included in the assignment
----

To help you understand the problem, there are some sample scripts / resources
in the assignment, including, but not limited to:

- `solver_random.py` - Sample stupid solver. You never lose to this stupid one.
- `sample/random_{0-6}.csv` - Sample output files by solver_random.py.
- `solver_greedy.py` - Sample solver using the greedy algorithm. You should beat this definitely.
- `sample/greedy_{0-6}.csv` - Sample output files by solver_greedy.py.
- `sample/sa_{0-6}.csv` - Yet another sample output files. I expect all of you will beat this one too. The solver itself is not included intentionally.
- `output_{0-6}.csv` - You should overwrite these files with your program's output.
- `output_verifier.py` - Try to validate your output files and print the path length.
- `input_generator.py` - Python script which was used to create input files, `input_{0-6}.csv`
- `visualizer/` - The directory for visualizer.

Details are intentionally omitted here. It is your responsibility to understand the contents of the repository.

Collaboration Rules / Discussions / Code of Conduct
----

### Team

In this year, work as a member of a team. We dicide a team on Friday.
Bacially, we divide people into teams by programming languages you use.

Please use one GitHub repository per a team. You should mention who are the members
in `README.md` file in the repository. Please feel free to upate `README.md` file.

Regarding office hours, I recommend each team's members to attend the office hours at the same time, as much as team members can.

##### Hints

It's up to each team how to collaborate. I strongly suggest:

- Use GitHub's isseus on team member's repository.
- Use slack chat. I can respond there.

Regarding "PR" ([pull request]), the following are quick hints:

[pull request]: https://help.github.com/categories/collaborating-with-issues-and-pull-requests/


Since GitHub doesn't allow forking the same origin repository more than once into your account, the followings might be helpful to send a pull request to other team member's repository.

Assuming that:

- You are `alice`. Your repository is https://github.com/alice/google-step-tsp.git

- You are trying to send a pull request to `bob`'s repository, https://github.com/bob/google-step-tsp.git

In your google-step-tsp directory, which was cloned from https://github.com/alice/google-step-tsp.git, do the followings:

    # Add and fetch bob's repository
    git remote add bob https://github.com/bob/google-step-tsp.git
    git fetch bob

    # See bob's branches
    git branches -a

    # Create a local branch, bob-gh-pages, from bob's remote branch, bob/gh-pages
    git checkout -b bob-gh-pages bob/gh-pages

    # Work on local bob-gh-pages branch, as usual
    ....

    # When it is ready, push the bob-gh-pages branch to your repository, https://github.com/alice/google-step-tsp.git
    # Your repository is usually called 'origin'.
    git push origin bob-gh-pages

    # Create a pull request at https://github.com/alice/google-step-tsp.git with:
    # base fork: bob/google-step-tsp, base: gh-pages  .... head fork: alice/google-step-tsp, compare: bob-gh-pages


### Discussion

- I highly encourage you to exchange an idea between students. If you have any
  question, or any idea, please share it at [GitHub Issues] or any other places.
  It is very important to share your question among all students so that everyone can get
  benefits from the discussion there. Other students may have the same
  question. Please feel free to answer a question from other students. I will join
  the discussion as much as possible.

- You might want to [watch the repository](https://help.github.com/articles/watching-repositories/)
  so that you get a notification when new question is posted.

### Code of Conduct

- You can get an assistance only from other STEP students or me. Please refrain from getting an assistance from any other people (e.g. your friends, other Googlers, etc).
- Use your best judgment when using third party libraries. No one wants to review code which just uses third-party libraries.
- It is okay to use built-in libraries provided by programming languages.

Please see also [code of conduct](https://online.berklee.edu/about/code-of-conduct), if you are interested in, as a general code of conduct, as a reference.

Feedback from me
----

I will make my best effort to answer your questions via:

-   [GitHub Issues] for this class, or GitHub Issues on team's repository
-   Slack channel
-   Office hours

I will review your code and give you a comment as much as possible, if all of the following conditions are satisfied:

-   Your code is hosted on GitHub. I will use GitHub's code review system.

-   Your code is consistency well formatted.  Please make sure to use appropriate code formatter, if you are not in confident.

-   Your code is written in one of the followings: C++, Rust, Scala, Python3, Python2, Java, C, JavaScript, Haskell, OCaml, and Lisp.
    I can't promise to review your code if the code is written in other programming languages.

Please feel free to [mention](https://github.com/blog/821) **@hayatoito** at
GitHub anytime if you need my help. I will get notified if you mention me. I will make my best effort to give a comment on your code.

I will not comment much about your approach itself. I will comment mainly about the quality of your code, in terms of readability and efficiency (time and space).

You can also comment on other student's code at GitHub. Please get familiar with Git and GitHub, and use them effectively as a collaboration tool.

FAQ
----

This FAQ includes the questions and the answers in the past years, as is. Some Q/A might be obsolete for this year.
Please use [GitHub Issues] for a new question.

- Q. I found a typo in this document.

- A. Please feel free to send a [pull request](https://help.github.com/articles/using-pull-requests/) or file an issue at [GitHub Issues] to improve this document.

- Q. Do I have to use the same code for every challenges?

- A. No.

- Q. Is there any limitation of machine resources I can use? Can I use multiple machines? Can I run my algorithm 24 hours?

- A. No limitation at all. You can use any machine resources you have.

- Q. It seems that this document and the scoreboard are publicly viewable. Is this intentional?

- A. Yes. I am a fan of transparency. If you have any concerns, please let me know that. I’ll honor your preference. Don’t enter any confidential information.

- Q. Can I look other team's repository?

- A. Yes. Don't try to hide anything. Eveything should be open. It's totally fine to exchange ideas between other teams.

- Q. Visualizer does not work well on firefox (or any other browsers you are using)

- A. I appreciate if you could send a pull request which fixes the issue. You can consider this as an optional assignment. Your contribution is highly welcome.

Acknowledgments
----

This assignment is heavily inspired by [Discrete Optimization Course on Coursera](https://www.coursera.org/learn/discrete-optimization).
