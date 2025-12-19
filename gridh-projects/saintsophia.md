# Saint Sophia's Inscriptions

The <a href="https://www.gu.se/en/research/digital-documentation-of-inscriptions-in-the-saint-sophia-cathedral-in-kyiv">Saint Sophia's Inscriptions project</a> is led by Gunnar Almevik and Jonathan Westin at University of Gothenburg. The backend is developed as an initial clone of the [Diana database coordination solution](https://github.com/gu-gridh/diana-backend), developed by GRIDH and is available <a href="https://github.com/gu-gridh/Saint_Sophia/">here</a>. The project frontend is developed as a part of the <a href="https://github.com/gu-gridh/multimodal-map#multimodal-map">Multimodal Map</a> project, a repository of user interface modules developed by GRIDH specifically aimed at spatio-temporal visualisations. The data explorer tools are developed as part of the <a href="https://github.com/gu-gridh/multimodal-viewer#multimodal-viewer">Multimodal Viewer</a> project.

## Funding
The projekt was funded by <a href="https://www.formas.se">**Formas research council for sustainable development**</a>, <a href="https://www.raa.se/">**The Swedish National Heritage Agency**</a>, and <a href="https://www.vitterhetsakademien.se/">**The Royal Swedish Academy of Letters, History and Antiquities**</a>.

## Project Team

### Project lead
<a href="https://www.gu.se/om-universitetet/hitta-person/gunnaralmevik">**Gunnar Almevik**</a> (University of Gothenburg).  
<a href="https://www.gu.se/om-universitetet/hitta-person/jonathanwestin">**Jonathan Westin**</a>  (University of Gothenburg).

### Data collection, registration and processing
**Viacheslav Korniienko** (National Conservation Area “St. Sophia of Kyiv”).  
**Sergii Trofymchuk** (National Conservation Area “St. Sophia of Kyiv”).  
**Alexander Ganshin** (National Conservation Area “St. Sophia of Kyiv”).  
**Oksana Kovalska** (National Conservation Area “St. Sophia of Kyiv”).  
**Sviatoslav Petryk** (National Conservation Area “St. Sophia of Kyiv”).  

**Fedir Androshchuk** (National Museum of the History of Ukraine).  
**Anastasia Diachenko** (National Museum of the History of Ukraine).  
**Mariia Prokopenko** (National Museum of the History of Ukraine).  
**Maryna Lutsyk** (National Museum of the History of Ukraine).  

**Gunnar Almevik** (University of Gothenburg).  
**Jonathan Westin** (University of Gothenburg).  
**Ashely Green** (University of Gothenburg).  
**Lucie Urbanová** (Czech Republic).  

### Development
**Jonathan Westin**, frontend development (GRIDH).  
**Tristan Bridge**, frontend development (GRIDH).  
**Matteo Tomasini**, backend development (GRIDH).  
**Ashely Green**, frontend development (GRIDH).  
**Aram Karimi**, backend development (GRIDH).    

## Datasets
The foundational dataset of inscriptions comes from Viacheslav Korniienko's twelve volume work Корпус _Графіті Софії Київської_ (2009-2020). As part of the project, Korniienko has been instrumental in translating this work into an open dataset.

The documentation of the surfaces - consisting of 3d-models, orthophotos, topographical visualisaitons, and reflectance transformation imaging - was carried out in 2024 and 2025 by an international team; Gunnar Almevik, Jonathan Westin and Ashely Green (University of Gothenburg, Sweden), and Olexandr Ganshin, Sviatoslav Petryk, Oksana Kovalska, and Sergii Trofymchuk (National Conservation Area “St. Sophia of Kyiv”, Ukraine).


## Database and API documentation

The backend solution upon which the Saint Sophia's Inscriptions portal is developed allows for consistent data input, and facilitates the interaction of end-users with the data shown in the frontend. To make the data open and reusable, Inscriptions of Saint Sophia makes available compliant REST APIs (including GeoJSON API), generated through the Django REST framework. These are the same APIs the projects's own frontend relies upon. Below follows a description of the APIs. [under construction]

**APIs**<br>
https://saintsophia.dh.gu.se/api/<br>
https://saintsophia.dh.gu.se/api/inscriptions/inscription/<br>
https://saintsophia.dh.gu.se/api/inscriptions/geojson/panel/

## Change log
**2025 - Week 51**<br>
Version 1.5.1 released: Routing to selected view and panel, faster gallery. RTI for surface 120-23.

**2025 - Week 50**<br>
Orthophoto, topography and mesh added for surface 120-23 and 205-05.

**2025 - Week 48**<br>
Version 1.5 released: Interactive Summary-view, bug fixes. Change log created.




