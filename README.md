# CI/CD Final Project

## Project Overview

This project demonstrates Continuous Integration and Continuous Deployment
(CI/CD) using a sample Python application.

## Technologies Used

- Python 3.11
- flake8 for code linting
- Python unittest for automated unit testing
- GitHub Actions for continuous integration
- Tekton for reusable CI/CD tasks
- Red Hat OpenShift for pipeline execution

## Application

The application includes a greeting function and an addition function.
Five unit tests verify normal inputs, empty names, whitespace handling,
and positive and negative numbers.

## GitHub Actions

The workflow is defined in `.github/workflows/workflow.yml`.
It runs on pushes and pull requests targeting the main branch.
The workflow installs dependencies, runs flake8, and executes unit tests.

## Tekton Tasks

The `.tekton/tasks.yml` file defines two tasks:

- cleanup: removes temporary Python files and caches.
- nose: runs code linting and unit tests.

## Run Locally

Run the unit tests:

    python3 -m unittest discover -s tests -v

Run the application:

    python3 app.py

## OpenShift

The OpenShift portion covers persistent storage, pipeline configuration,
pipeline execution, and application log inspection.
These steps must be verified in the IBM Skills Network lab environment.
