# Google STEP 2018: Travelling Salesman Problem Challenges

[Hayato Ito](https://github.com/hayatoito) (hayato@google.com)

## Quick Links

- [Scoreboard]
- [GitHub Issues]

[scoreboard]:
  https://docs.google.com/spreadsheets/d/1Aa_NNQf7sFANuHKt0FTvUBQ83QO3OOKZjifhsmjOxqc/edit?usp=sharhing
[github issues]: https://github.com/hayatoito/google-step-tsp/issues

## Problem Statement

In this assignment, you will design an algorithm to solve a fundamental problem
faced by every travelling salesperson, called _Travelling Salesman Problem_
(TSP). I’ll explain TSP in the onsite class. TSP is very famous problem. See
[Wikipedia](http://en.wikipedia.org/wiki/Travelling_salesman_problem). You can
understand the problem without any difficulties.

Quoted from
[Wikipedia](http://en.wikipedia.org/wiki/Travelling_salesman_problem):

> The travelling salesman problem (TSP) asks the following question: Given a
> list of cities and the distances between each pair of cities, what is the
> shortest possible route that visits each city exactly once and returns to the
> origin city?

## Assignment

The assignment is hosted on GitHub,
[https://github.com/hayatoito/google-step-tsp](https://github.com/hayatoito/google-step-tsp).
You can download the assignment by `git clone`:

```shellsession
git clone https://github.com/hayatoito/google-step-tsp
```

I recommend you to [fork](https://help.github.com/articles/fork-a-repo/) this
repository to your github account before cloning it.

This document doesn't explain “what is git?’ nor “how to use GitHub?”. It is
your responsibility to master the usage of git and GitHub.

The repository includes sample scripts written in Python 3, rather than in
Python 2. It’s your responsibility to install Python 3 if you want to run the
scripts, though running the scripts is not mandatory.

There are 7 challenges of TSP in the assignment, from N = 5 to N = 2048:

| Challenge   | N (= the number of cities) | Input file  | Output file  |
| ----------- | -------------------------: | ----------- | ------------ |
| Challenge 0 |                          5 | input_0.csv | output_0.csv |
| Challenge 1 |                          8 | input_1.csv | output_1.csv |
| Challenge 2 |                         16 | input_2.csv | output_2.csv |
| Challenge 3 |                         64 | input_3.csv | output_3.csv |
| Challenge 4 |                        128 | input_4.csv | output_4.csv |
| Challenge 5 |                        512 | input_5.csv | output_5.csv |
| Challenge 6 |                       2048 | input_6.csv | output_6.csv |

See _Data Format Specification_ section to know the format of input and output
files.

### Your tasks

Note: As explainerd later, you will work as a member of a _team_. Please replace
_you_ with a _team_, as necessary.

- Write a program, solving each TSP by designing and implementing an algorithm.
- Overwrite each output file, `output_{0-6}.csv`, with the output of your
  program.
- Enter the _path length_ of your output in the [scoreboard], for each
  challenge. Needless to say, a shorter path is better then a longer path.

### An optional task (Speed challenge)

What matters in this optional task is your program's _speed_ (execution time).
The path length does not matter as long as it is meets the condition.

Your task is: Given `input_6.csv`, write a program which outputs a path shorter
than `45,000`

Input your program's execution time in the [scoreboard]. Faster (smaller) is
better.

You can measure the execution time by `time` command. For example,

```shellsession
$ time yourprogram input_6.csv solution_yours_6.csv
2.96s user 0.07s system 97% cpu 3.116 total
```

In this case, your score is `3.116` (s).

### Visualizer

The demo page of the visualizer is
[here](http://hayato.io/google-step-tsp/visualizer/build/default/).

The assignment includes a helper Web page,
`visualizer/build/default/index.html`, which visualizes your solutions. You need
to run a HTTP server on your local machine to access the visualizer. Any HTTP
server is okay. If you are not sure how to run a web server, use the following
command to run the HTTP server. Make sure that you are in the top directory of
the assignment before running the command.

```shellsession
python3 -m http.server
# python2 -m SimpleHTTPServer # If you don’t have Python 3
```

Then, open a browser and navigate to the
[http://localhost:8000/visualizer/build/default/](http://localhost:8000/visualizer/build/default/).

Visualizer was only tested by Google Chrome. Using the visualizer is up-to you.
You don’t have to use the visualizer to finish the assignment. The visualizer is
provided for the purpose of helping you understand the problem.

Once you publish a git repository, you can also enter the URL of a visualizer
for your solutions in the [scoreboard] (e.g.
[http://your_github_account_name.github.io/google-step-tsp/visualizer/build/default/](http://your_github_account_name.github.io/google-step-tsp/visualizer/build/default/)).

See
[GitHub Help](https://help.github.com/articles/configuring-a-publishing-source-for-github-pages/)
to know how to enable GitHub pages on your repository.

## Data Format Specification

### Input Format

The input consists of `N + 1` lines. The first line is always `x,y`. It is
followed by `N` lines, each line represents an i-th city’s location, point
`xi,yi` where `xi`, `yi` is a floating point number.

```
x,y
x_0,y_0
x_1,y_1
…
x_N-1,y_N-1
```

### Output Format

Output has `N + 1` lines. The first line should be “index”. It is followed by
`N` lines, each line is the index of city, which represents the visitation
order.

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

These formats are requirements for the visualizer, which can take only properly
formatted CSV files as input.

## Schedule

### The class begins: 2018-06-22 (Fri) 5:00pm (JST)

The class starts. You are strongly encouraged to bring your laptop.

1.  I'll give you a special lecture, called "How the Computer Works: Memory and
    Data Structures for Hackers" at the beginning (in 2 hours).

2.  Then, I'll explain this "TSP" assignments. You are expected to understand
    the problem and solve a challenge with a small N in the class, if we have
    enough time.

Action items on Friday:

1.  [All] Decide a team:

    - Enter your GitHub account name in "Team members" field in the
      [Scoreboard].
    - e.g. Team XXX: "alice, bob, charlie"

2.  [Team] Decide the team's GitHub repository

    - Enter the team's GitHub repository location in the [Scoreboard].
    - e.g. Use alice's repository as the team's repository:
      "https://github.com/alice/google-step-tsp/"

3.  [Team] Invite team members as collaborators to the team's repository.

    - See
      [Inviting collaborators to a personal repository](https://help.github.com/articles/inviting-collaborators-to-a-personal-repository/)
      fore more info.

4.  [All] Watch the team's repository

    - See
      [watching and unwatching repositories](https://help.github.com/articles/watching-and-unwatching-repositories/)
      for more info.

5.  [All] "Say Hello" to the team's GitHub Issues:

    - e.g. Go to
      [https://github.com/alice/google-step-tsp/issues](https://github.com/alice/google-step-tsp/issues),
      click "New Issue", and say hello to the team; "Hi, I'm bob".

6.  [Optional] Enjoy dinner with team members

    - Each team might want to discuss the followings:
      - How to collaborate?
      - Whether to attend office hours or not. If so, when?
    - If the team can come to the office hours, please input _firstname_,
      _lastname_, and _email_ (optional) for each team member who can come in
      this
      [office hours sign up sheet](https://docs.google.com/spreadsheets/d/1Aa_NNQf7sFANuHKt0FTvUBQ83QO3OOKZjifhsmjOxqc/edit#gid=2110766836).

### Coding: From: 2018-06-22 (Fri) 8:00pm - To: 2018-06-29 (Fri) 5:00pm

The deadline of the final submission is the next Friday.

Until the deadline, you (team) are expected to improve your algorithm and enter
the score in the [scoreboard] manually for each challenge. You can update the
score as many times as needed. I highly recommend you to update your score
whenever you can find a shorter path.

You can also enter the visualizer URL so that other teams can see how your
team's salesperson is visiting each city.

Please try to publish your code, via `git push`, as often as possible so that
other members or other teams can see your code.

#### (Optional) Office hours: (2018-06-26 (Tue) 5:00pm - )

I will hold office hours on next Tuesday at Google Tokyo office. I will be
available until nealy 10:00pm. You can come anytime and leave anytime.

As a side bonus for office hours attendees, I have a plan to explain the
following topics very roughly there:

- How to improve code readability
- Essential tools for coding (lint, auto code formatter, and others)
- How to use `git` and GitHub effectively as a team
- How the computer runs a program (loading a program binary, stack and heap)
- Programming Languages: Pros and Cons (Interpreter, Compiler, Type Systems)
- Using [Parser Combinators](https://en.wikipedia.org/wiki/Parser_combinator) to
  solve the _calculator homework_ (in class 3) in a modern way

All of these are optional topics. If are interested in, please join us anytime.

#### (Optional) Yet another optional task: Challenge 7: 2018-06-27 (Wed)

I will announce it on 2018-06-28 (Wed).

## What’s included in the assignment

To help you understand the problem, there are some sample scripts / resources in
the assignment, including, but not limited to:

- `solver_random.py` - Sample stupid solver. You never lose to this stupid one.
- `sample/random_{0-6}.csv` - Sample output files by solver_random.py.
- `solver_greedy.py` - Sample solver using the greedy algorithm. You should beat
  this definitely.
- `sample/greedy_{0-6}.csv` - Sample output files by solver_greedy.py.
- `sample/sa_{0-6}.csv` - Yet another sample output files. I expect all of you
  will beat this one too. The solver itself is not included intentionally.
- `output_{0-6}.csv` - You should overwrite these files with your program's
  output.
- `output_verifier.py` - Try to validate your output files and print the path
  length.
- `input_generator.py` - Python script which was used to create input files,
  `input_{0-6}.csv`
- `visualizer/` - The directory for visualizer.

Details are intentionally omitted here. It is your responsibility to understand
the contents of the repository.

## Collaboration / Code of Conduct

### Team

In this year, you are expected to work as a member of a team. We dicide a team
on Friday. Bacially, we divide people into teams by a programming language a
team uses.

Please use one GitHub repository per a team. You should mention who are the
members in `README.md` file in the repository. Please feel free to update
`README.md` file.

Regarding office hours, I recommend team members in the same team to attend the
office hours together as much as you can.

### Hints: Work as a team

It's up to each team how to collaborate. I suggest:

- Use GitHub's isseus on team's repository effectively.
  - Share any question there so that other team members can help you
    - e.g. "I got _conflicts_ in git, and I don't know how to resolve it. What
      should I do???"
- Help team members. Share what you have done as much as possible.
- Use slack chat. I can respond there.

Regarding "PR" ([pull request]), the followings are quick hints:

[pull request]:
  https://help.github.com/categories/collaborating-with-issues-and-pull-requests/

Assuming that:

- You are `bob`. Your repository is https://github.com/bob/google-step-tsp.git

- You are trying to send a pull request to `alice`'s repository,
  https://github.com/alice/google-step-tsp.git

In your google-step-tsp directory, which was cloned from
https://github.com/bob/google-step-tsp.git, do the followings:

```shellsession
# Add and fetch alice's repository
git remote add alice https://github.com/alice/google-step-tsp.git
git fetch alice

# See alice's branches
git branches -a

# Create a local branch, alice-master, from alice's remote branch, alice/master
git checkout -b alice-master alice/master

# Work on local alice-master branch, as usual
....

# When it is ready, push the alice-master branch to your repository, https://github.com/bob/google-step-tsp.git
# Your repository is usually called 'origin'.
git push origin alice-master

# Create a pull request, "New pull request", at "https://github.com/bob/google-step-tsp" with:
# base fork: alice/google-step-tsp, base: master  .... head fork: bob/google-step-tsp, compare: alice-master
```

### Code of Conduct

- You can get an assistance only from other STEP students or me.
- Don't get any assistance from any other people (e.g. your friends, other
  Googlers, etc). That can be considered as a _cheat_.
- Use your best judgment when using third party libraries. No one wants to
  review your code which just uses third-party libraries.
- It is okay to use built-in libraries provided by programming languages, of
  course.

Please see also
[code of conduct](https://online.berklee.edu/about/code-of-conduct), if you are
interested in, as a general code of conduct, as a reference.

## Feedback from me

I will make my best effort to answer your questions via:

- "GitHub Issues" on each team's GitHub repository, or
  [on this class](https://github.com/hayatoito/google-step-tsp/issues).
- Slack channel
- Office hours

I will review your code and give you a comment as much as possible.

Please feel free to [mention](https://github.com/blog/821) **@hayatoito** at
GitHub anytime if your team needs my help. I will get notified if you mention me
there.

I will not comment much about your team's approach itself. I will comment mainly
about the quality of your code, in terms of readability and efficiency (time and
space) in Google Standard.

You can also comment on other team member's code at GitHub. Please get familiar
with Git and GitHub, and use them effectively as a collaboration tool.

### Tips for better collaboration

The following tips might be helpful:

- Commit often, and push often. Small commits are easy to review, and are
  unlikely to conflict others' changes.

- Your code should be consistency well formatted. Please make sure to use
  appropriate code formatter, if you are not in confident. Don't try to format
  your code by yourself if a tool can do that.

- I can review your code if your code is written in one of the followings: C++,
  Rust, Scala, Python 3, Python 2, Java, C, JavaScript, TypeScript, Haskell,
  OCaml, and Lisp. I can't promise to review your code if the code is written in
  other programming languages.

## FAQ

This FAQ includes the questions and the answers in the past years, as is. Some
Q/A might be obsolete for this year. Please use [GitHub Issues] for a new
question.

- Q. I found a typo in this document.

- A. Please feel free to send a
  [pull request](https://help.github.com/articles/using-pull-requests/), as a
  practice, or file an issue at [GitHub Issues].

- Q. Do I have to use the same code for every challenges?

- A. No.

- Q. Is there any limitation of machine resources I can use? Can I use multiple
  machines? Can I run my algorithm 24 hours?

- A. No limitation at all. You can use any machine resources you have.

- Q. It seems that this document and the scoreboard are publicly viewable. Is
  this intentional?

- A. Yes. I am a fan of transparency. If you have any concerns, please let me
  know that. I’ll honor your preference. Don’t enter any confidential
  information.

- Q. Can I look other team's repository?

- A. Yes. Don't try to hide anything. Eveything should be open. It's fine to
  exchange ideas between other teams, or borrow their ideas.

## Acknowledgments

This assignment is heavily inspired by
[Discrete Optimization Course on Coursera](https://www.coursera.org/learn/discrete-optimization).
