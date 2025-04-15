# Changelog

## [v6.0.0](https://github.com/RegioHelden/django-languageselect/tree/v6.0.0) (2025-04-15)

[Full Changelog](https://github.com/RegioHelden/django-languageselect/compare/v5.0.1...v6.0.0)

**Breaking changes:**

- Add support for Django 5.1 and 5.2, remove support for Django 5.0 and Python 3.10 [\#17](https://github.com/RegioHelden/django-languageselect/pull/17) (@lociii)

**Implemented enhancements:**

- Migrate to reusable github workflows [\#15](https://github.com/RegioHelden/django-languageselect/pull/15) (@lociii)

## 5.0.1 (2024-06-27)

**Breaking changes:**

* Remove support for Python below 3.10
* Remove support for Django below 4.2

**Implemented enhancements:**

* Add support for Django 5.0
* Add support for Python 3.11
* Add support for Python 3.12
* Modernize build and test environment

## 5.0.0 (2024-06-27)

Not released to due an issue with the deploy action

## 4.0.1 (2023-01-02)

**Breaking changes:**

* Remove support for Django < 3.2
* Remove support for Python < 3.8

**Implemented enhancements:**

* Modernize build and test environment

## 4.0.0 (2023-01-02)

Not released to due an issue with the deploy action

## 3.0.0 (2021-05-05)

**Breaking changes:**

* Remove support for Django 2.x

**Implemented enhancements:**

* Remove utf 8 headers as all Python 3 files must be unicode anyways
* Modernize build and test environment

**Fixed bugs:**

* Fix CI badge in readme

# 2.0.2 (2021-05-05)

**Implemented enhancements:**

* Add tests for Django 3.2
* Remove old python 2 and Django compatibility code

**Fixed bugs:**

* Remove setting language in session as this was depreacted since Django 2.x and is broken with Django 3.x

# 2.0.1 (2021-03-25)

**Implemented enhancements:**

* Fix documentation syntax

# 2.0.0 (2021-03-25)

**Breaking changes:**

* Remove support for Django < 2.2

**Implemented enhancements:**

* Update packages
* Update Docker env

# 1.0.0 (2019-11-04)

**Breaking changes:**

* Remove Python 2 support

**Implemented enhancements:**

* Update packages
* Add docker container to run tests locally

# 0.1.6 (2018-01-27)

**Fixed bugs:**

* Add missing folders and modules from package

# 0.1.5 (2018-01-15)

**Implemented enhancements:**

* Add support for python 3 and Django 2, implementing tests in travis ci

# 0.1.4 (2017-04-18)

**Breaking changes:**

* Rename package to django_languageselect (backwards incompatible) to be able to import the module

# 0.1.3 (2016-06-17)

**Fixed bugs:**

*  Fix session key to store language, Django 1.9 compatibility


