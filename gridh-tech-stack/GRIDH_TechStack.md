#  GRIDH: Gothenburg Research Infrastructure in Digital Humanities

## Tech Stack
This document gives an overview of GRIDH's current tech stack that provides both human and machine readable public interfaces. With these interfaces, we help researchers to develop research applications and navigate datasets, and assist memory institutions that seek new ways to make their collections available for research and public alike. GRIDH's tech stack was shaped by several developers over the years and has grown organically while we strive to streamline technologies and keep them up-to-date.

### Backend
<img src="https://static.djangoproject.com/img/logos/django-logo-negative.png" alt="Django logo" height="50px;"/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img src="https://avatars.githubusercontent.com/u/177010?s=48&v=4" alt="Omeka logo" height="50px;"/>
<!-- TODO: find better logo file for Omeka-S -->

For data management, the implementation of data models and API endpoints, GRIDH mainly uses the python-based webframework [Django](https://www.djangoproject.com/). However, in case GRIDH is working together with cultural heritage institutions like libraries, archives and museums, we also uses the data publishing platform [Omeka-S](https://omeka.org/s/).

In projects, where there is no additional backend but data is fetched from other endpoints, GRIDH also gathered experience in using other python-based web and microframeworks like [FastAPI](https://fastapi.tiangolo.com/) and [Flask](https://flask.palletsprojects.com/).

#### Databases
<img src="https://wiki.postgresql.org/images/3/30/PostgreSQL_logo.3colors.120x120.png" alt="Postgresql logo" height="50px;"/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img src="https://mariadb.com/wp-content/webp-express/webp-images/doc-root/wp-content/uploads/2019/11/mariadb-logo_black-transparent-300x75.png.webp" alt="MariaDB logo" height="40px;"/>

Depending on the backend software's support, GRIDH projects use either [Postgresql](https://www.postgresql.org/) (e.g. for Django applications) or [MariaDB](https://mariadb.com/) (e.g. for Omeka-S or Wordpress) as open source relational database management systems.

There are also projects where data is not stored in their own database, but only fetched via APIs and visualized. In these cases, we make use of Linked Open Data and FAIR data around the world.

#### APIs
In order to share data openly accessible with other services and platforms, GRIDH implemented REST-APIs with [Django REST framework](https://www.django-rest-framework.org/) and the [Omeka-S REST API](https://omeka.org/s/docs/developer/api/rest_api/). 

You can find an overview of GRIDH's available API endpoints [here](../gridh-apis/GRIDH_APIs.md) (work in progress).

#### Search engines
Some GRIDH projects with the requirement for fast and more complex search queries use the open source, distributed search and analytics engine [Elasticsearch](https://www.elastic.co/elasticsearch) in the background.

### Frontend
<img src="https://github.com/vuejs/art/raw/master/logo.png" alt="Vue JS logo" height="50px;"/>

For most frontends, GRIDH uses [Vue JS](https://vuejs.org/) as base for visualizing data from the backends and providing users with flexible and performant user interfaces.

### Image Server
For providing users and applications with high resolution images with deep zoom functionalities that can be structured, compared and annotated, GRIDH has set up its own IIIF server with the help of [IIPImage server](https://iipimage.sourceforge.io/) that implements the [IIIF](https://iiif.io) standard. 

GRIDH's IIIF server supports the Image API 3.0. Additionally, the Presentation API is currently under development for certain projects.

### Containers
<img src="https://github.com/containers/podman/raw/main/logo/podman-logo-source.svg" alt="Podman logo" height="50px;"/>

For some of the projects, the applications are running in [Podman](https://podman.io/) containers in order to keep them seperate in their own environment.

Being part of the IT infrastructure of Gothenburg University, GRIDH can also deploy podman containers to the university's container infrastructure.

### Annotation Software
For annotating media like images or videos, GRIDH is using the open source data labelling platform [Label Studio](https://labelstud.io/).

### Content Management

<img src="https://s.w.org/style/images/about/WordPress-logotype-standard.png" alt="Wordpress logo" height="60px;"/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img src="https://github.com/wagtail/wagtail/raw/main/.github/wagtail-inverse.svg" alt="Wagtail logo" height="45px;"/>

For content management, GRIDH's team has set up several [Wordpress](https://wordpress.org/) instances which are mostly running in podman containers. We also started to use [Wagtail](https://wagtail.org/) for projects that already use Django for the web framework and more flexibiblity was needed.
One project is also using the headless CMS [Strapi](https://strapi.io/).

### Analytics

GRIDH uses the privacy-first, open source web analytics application [Matomo](https://matomo.org/) for web statistics and reports.
