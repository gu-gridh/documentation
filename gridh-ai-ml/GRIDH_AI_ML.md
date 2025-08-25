# AI Tools and Development in Digital Humanities Research

## Abstract

The Gothenburg Research Institute for Digital Humanities (GRIDH) leverages cutting-edge artificial intelligence methodologies to advance humanities scholarship through computational analysis of textual, visual, and cultural heritage materials. This document presents an overview of our AI-driven research initiatives, demonstrating the application of deep learning, natural language processing, and computer vision techniques to enhance scholarly inquiry in the humanities.

## Introduction

Digital humanities research increasingly relies on sophisticated computational methods to analyze large-scale cultural datasets. GRIDH's approach integrates state-of-the-art AI technologies with domain-specific humanities expertise, creating tools and methodologies that expand the analytical capabilities of researchers while maintaining rigorous scholarly standards. Our projects demonstrate the transformative potential of AI in cultural heritage preservation, literary analysis, and historical documentation.

## Project Overview

### 1. Litteraturlaboratoriet (LittLab): Automated Analysis of Graphic Elements in Historical Publications

**Objective**: Development of a comprehensive pipeline for detecting and cataloging visual elements in digitized Swedish literary works from the 19th and early 20th centuries.

**Methodology**: 
The project employs a multi-stage machine learning approach combining object detection, visual similarity analysis, and semantic tagging. A manually annotated dataset serves as ground truth for training deep learning models to identify seven distinct categories of graphic elements:

- Illustrationer
- Ornament
- Anfanger
- Tillbakamateria
- Proveniens
- Omslagsbilder
- Table of contents (Innehållsförteckning)

**Technical Implementation**:
- **Object Detection**: YOLOv8 architecture fine-tuned on domain-specific annotations [1]
- **Visual Similarity**: ResNeXt50-32x4d feature extraction with FiftyOne framework [2], utilizing Spotify's Annoy library for approximate nearest neighbor computation [3]
- **Semantic Analysis**: Automated tagging via the Recognize Anything Model (RAM) [4] with Swedish translation and hierarchical categorization
- **User Interface**: Standalone application developed using CustomTkinter framework [5]

**Significance**: This work enables large-scale analysis of visual culture in Swedish literature, providing insights into publishing practices, artistic trends, and cultural circulation patterns.

**Access**: https://littlabb.dh.gu.se

---

### 2. Kritikens Nya Ordning (KNO): Computational Analysis of Swedish Literary Criticism

**Objective**: Longitudinal study of Swedish literary criticism across three temporal markers (1906, 1956, 2006) to trace evolutionary patterns in critical discourse and evaluative frameworks.

**Dataset**: 700 digitized literary reviews with comprehensive metadata including temporal, authorial, and gender classifications.

**AI Applications**:
- **Text Correction**: Large language models (GPT-4o, Claude Sonnet 3.5) employed for OCR error correction and textual standardization
- **Sentiment Analysis**: Automated extraction of reviewer attitudes and evaluative stances
- **Thematic Classification**: AI-generated categorical labels for thematic content analysis

**Analytical Framework**:
- **Lexical Analysis**: Term Frequency-Inverse Document Frequency (TF-IDF) vectorization for distinctive vocabulary identification
- **Semantic Modeling**: Swedish Sentence-BERT embeddings (KBLab model) for capturing semantic relationships [Rekathati 2021]
- **Dimensionality Reduction**: UMAP visualization for clustering reviews by linguistic and thematic similarity

**Interactive Visualization**: Web-based interfaces enabling multi-dimensional exploration of critical discourse patterns.

**Research Impact**: Provides quantitative evidence for stylistic and ideological shifts in Swedish literary criticism, demonstrating the evolution of evaluative criteria across the 20th century.

**Access**: 
- Attitude Visualization: https://home.dh.gu.se/david/attitude
- Interactive Review Map: https://dh.gu.se/kno

---

### 3. St. Sophia Digital Archive: Multilingual Documentation Enhancement

**Objective**: Application of AI translation and transliteration technologies to improve accessibility of Ukrainian historical and religious manuscripts.

**Technical Components**:
- **Machine Translation**: Claude Sonnet 3.5 integration for Ukrainian-to-English translation
- **Romanization**: Automated Cyrillic-to-Latin script conversion for enhanced accessibility
- **Quality Assurance**: Human-in-the-loop validation workflows ensuring translation accuracy

**Scholarly Impact**: Enables international scholarship on Eastern Orthodox religious texts and Ukrainian cultural heritage materials.

**Access**: https://saintsophia.dh.gu.se

---

### 4. Image Inspector: Automated Visual Content Analysis Platform

**Development Status**: In progress

**Objective**: Creation of a comprehensive tool for automated extraction, analysis, and cataloging of visual content within digitized publications.

**Core Capabilities**:
- **Image Segmentation**: Automated detection and extraction of visual elements from scanned pages
- **Caption Generation**: AI-powered descriptive metadata creation
- **Content Classification**: Deep learning-based categorization of visual materials
- **Similarity Clustering**: Identification of related visual content across large corpora

**Target Applications**: Cultural heritage institutions, digital libraries, and visual culture research initiatives.

**Repository**: https://github.com/gu-gridh/Image-Inspector

---

### 5. Advanced Topic Modeling for Swedish Textual Corpora

**Framework**: BERTopic implementation with Swedish-optimized transformer models

**Technical Specifications**:
- **Embedding Model**: KBLab/sentence-bert-swedish-cased for Swedish-specific semantic representations
- **Clustering Algorithm**: HDBSCAN for hierarchical topic identification
- **Dimensionality Reduction**: UMAP for topic space visualization

**Applications**: 
- Literary review corpus analysis
- Historical document thematic clustering
- Comparative discourse analysis across temporal periods

**Research Value**: Enables discovery of latent semantic structures in Swedish textual materials, supporting both exploratory and confirmatory research approaches.

## Technical Infrastructure

GRIDH maintains high-performance computing environments optimized for AI research in the humanities, including:

- **OCR Systems**: Tesseract and HtrFlow for historical document digitization
- **Deep Learning Frameworks**: PyTorch, TensorFlow, and specialized NLP libraries
- **Scalable Computing**: GPU clusters for training large-scale models
- **Data Management**: Secure storage and version control systems for sensitive cultural heritage materials

## Research Impact and Future Directions

These initiatives demonstrate the successful integration of AI methodologies into humanities research workflows, enabling:

1. **Scale Enhancement**: Analysis of cultural corpora previously intractable due to size constraints
2. **Pattern Discovery**: Identification of subtle trends and relationships invisible to traditional methods
3. **Accessibility Improvement**: Multilingual and multimodal access to cultural heritage materials
4. **Methodological Innovation**: Development of domain-specific AI applications for humanities research

Future development priorities include expansion of multilingual capabilities, integration of multimodal analysis frameworks, and development of interpretable AI models specifically designed for humanities applications.


## References

[1] Jocher, G., et al. (2023). Ultralytics YOLOv8. https://github.com/ultralytics/ultralytics

[2] Moore, B., et al. (2020). FiftyOne: The open-source tool for building high-quality datasets and computer vision models. https://github.com/voxel51/fiftyone

[3] Bernhardsson, E. (2013). Annoy: Approximate Nearest Neighbors in C++/Python. https://github.com/spotify/annoy

[4] Zhang, S., et al. (2023). Recognize Anything: A Strong Image Tagging Model. *arXiv preprint arXiv:2306.03514*.

[5] Schiman, T. (2022). CustomTkinter: Modern and customizable Python UI-library. https://github.com/TomSchimansky/CustomTkinter

[6] Rekathati, F. (2021). Swedish Sentence-BERT: A Swedish Sentence Embedding Model. KBLab Technical Report.
