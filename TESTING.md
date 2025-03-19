# Testing Guide

This document explains how to run tests for the **iNaturalist Python Client** project.

## Prerequisites

Ensure you have the following installed:

- Python 3.x
- `pip`
- `pytest` and `pytest-cov` (for test coverage)

Install dependencies:

```bash
pip install -r requirements.txt -r test-requirements.txt
```

## Running Tests

To run all tests:

```bash
pytest --cov=inat_client
```

This runs the tests and generates a coverage report.
