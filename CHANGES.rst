CHANGES
-------

v0.3.0
~~~~~~
Date: 27.11.2021

- fix AssertionError if :title: option is missing (see #3)
- increase css specificity to fix big margins that have appeared due to some
  CSS change in sphinx or rtd
- fix exception when building pdf documents (#1, #4)
- prerender tab hidden/selected state to avoid content reflow on page (re-)load


v0.2.0
~~~~~~
Date: 21.06.2021

- update css for sphinx 4


v0.1.0
~~~~~~
Date: 10.10.2020

- fix missing assets when using the extension on readthedocs
- add documentation along with visual example on readthedocs


v0.0.1
~~~~~~
Date: 10.10.2020

Initial version with basic functionality:

- all rendering is done by JS, no prerendering
- so far no "notebook-groups" that switch the language simultaneously
