# Numerical Data Source Code Survey

![Proactive Programmers](.github/images/Square-Proactive-Programmers-Logo.svg)

[![build](../../actions/workflows/build.yml/badge.svg)](../../actions/)
![Platforms: Linux, MacOS, Windows](https://img.shields.io/badge/Platform-Linux%20%7C%20MacOS%20%7C%20Windows-blue.svg)
[![Language: Python](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![Code Style: Black](https://img.shields.io/badge/Code%20Style-Black-blue.svg)](https://github.com/psf/black)
[![Commits: Conventional](https://img.shields.io/badge/Commits-Conventional-blue.svg)](https://www.conventionalcommits.org/en/v1.0.0/)
[![Discord](https://img.shields.io/discord/872320492936257537?logo=discord)](https://discord.gg/kjah8MFYbR)

## Introduction

- Due date: Check the [Proactive Programmers Discord
server](https://discord.gg/kjah8MFYbR).
- This assignment will be submitted on GitHub following
the expectations in the syllabus on
[Assignment Submission](https://github.com/allegheny-college-cmpsc-101-fall-2023/course-materials#assignment-submission).
- To begin, read this `README` and the Proactive Programmers' project
description for
[Numerical Data](https://proactiveprogrammers.com/data-abstraction/source-code-surveys/numerical-data/)
- Modifications to the gatorgrade.yml file are not permitted without explicit instruction.
- This assignment is a Source Code Survey and will be evaluated as
described in the
[Assessment Strategies](https://proactiveprogrammers.com/proactive-learning/assessment-strategy/#source-code-surveys).
- You can check the
[numerical-data-starter repository](https://github.com/allegheny-college-cmpsc-101-fall-2023/numerical-data-starter)
for any updates to this project's documentation or
source code.

## Learning Objectives

This assignment is about using introductory programming concepts and
software development
tools to complete a command line interface for testing primality
of numbers. The learning objectives of this assignment are to:

1. Use Git and GitHub to manage source code file changes
2. Study type annotations in function declarations, floating point arithmetic
   and modulus operations
4. Write clearly about the programming concepts in this assignment.

## Seeking Assistance

Please review the course expectations on the syllabus about
[Seeking Assistance](https://github.com/allegheny-college-cmpsc-101-fall-2023/course-materials#seeking-assistance).
Students are reminded
to uphold the Honor Code. Cloning the assignment repository is a
commitment to the latter.

For this assignment, you may use class materials, textbooks, notes, and the
internet. However,
when asked to write "in your own words", you must use _your own_ words.

Post questions to the [Proactive Programmers Discord server](https://discord.gg/kjah8MFYbR).

## Project Overview

After cloning this repository to your computer, please take the following
steps:

- Make sure that you have already installed and know how to use all of the
  programming tools that are mentioned in the description of the [Proactive
  Skills](https://proactiveprogrammers.com/proactive-skills/technical-skills/introduction-technical-skills/).
- Use the `cd` command to change into the directory for this repository.
- At this point, run `gatorgrade --config config/gatorgrade.yml` and check whether
the output matches the gatorgrade output reported in GitHub actions.
  - if they do not match:
    - create a virtual environment in your local directory!
    - run `python -m venv ./.venv`
    - run `source .venv/bin/activate`
    - rerun and recheck the local gatorgrade output report for a match with GitHub actions!
- Change into the program source code directory by typing `cd source`.
- Run the provided Python scripts by typing the following:
  - `python determine-even-odd.py`: demonstrate computation with integer values and modular arithmetic
  - `python floating-point-confusion.py`: demonstrate computation with floating-point values
  - `python type-annotation.py`: practice thinking about and using type annotations
- Follow the
  [instructions](https://proactiveprogrammers.com/data-abstraction/source-code-surveys/numerical-data/) on the Proactive Programmers web site for this project
  to take all of the needed steps and to complete all of the required
  deliverables.
- Confirm that the programs are producing the expected output.
- Make sure that you can explain why the programs produce the output that they do.
- Don't forget to provide all of the required responses to the technical writing
  prompts in the `writing/reflection.md` file.
- Please make sure that you completely delete the `TODO` markers and their
  labels from all of the provided source code. This means that instead of only
  deleting the `TODO` marker from the code you should instead delete the `TODO`
  marker and the entire prompt and then add your own comments to demonstrate
  that you understand all of the source code in this project.
- Please make sure that you also completely delete the `TODO` markers and their
  labels from every line of the `writing/reflection.md` file. This means that
  you should not simply delete the `TODO` marker but instead delete the entire
  prompt so that your reflection is a document that contains polished technical
  writing that is suitable for publication on your professional web site.
