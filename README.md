# python-points

[![github action status](https://github.com/hexlet-components/python-points/workflows/Python%20CI/badge.svg)](https://github.com/hexlet-components/python-points/actions)

A SICP'ish Points implemented in Python using hexlet-pairs.

## Install

```shell
pip install hexlet-points
```

## Usage example

<!-- This code will be doctested. Do not touch the markup! -->

    >>> from hexlet import points
    >>> p = points.make(100, 200)
    >>> print(points.to_string(p))
    (100, 200)
    >>> points.get_x(p)
    100
    >>> points.get_y(p)
    200
    >>> points.get_quadrant(p)
    1

[![Hexlet Ltd. logo](https://raw.githubusercontent.com/Hexlet/assets/master/images/hexlet_logo128.png)](https://ru.hexlet.io/pages/about)

This repository is created and maintained by the team and the community of Hexlet, an educational project. [Read more about Hexlet (in Russian)](https://ru.hexlet.io/pages/about?utm_source=github&utm_medium=link&utm_campaign=python-points).
