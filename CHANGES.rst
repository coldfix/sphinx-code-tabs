CHANGES
-------

v0.5.3
~~~~~~
Date: 28.11.2021

- fix CHANGES to appear in long description


v0.5.2
~~~~~~
Date: 28.11.2021

- fix ImportError triggered on readthedocs due to ancient sphinx version (v1.8)


v0.5.1
~~~~~~
Date: 28.11.2021

- update description for landing page


v0.5.0
~~~~~~
Date: 28.11.2021

- add ``tab`` directive for arbitrary (non-code) content
- add ``tabs`` directive and make ``code-tabs`` a backward-compatibility alias
  of ``tabs``, to account for the new more general tab containers
- make the ``:title:`` option no longer required (wasn't enforced anyway by
  sphinx)
- add grouped tabs
- make non-code tabs look better in latex output by boxing them like listings


v0.4.0
~~~~~~
Date: 27.11.2021

- fix bug that selects all tab buttons on click (introduced in prerender
  commit)


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
