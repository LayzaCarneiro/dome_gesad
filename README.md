# DomE

<b>Abstract:</b>
DoME is a sophisticated chatbot designed to streamline database management tasks through natural language input. Leveraging advanced NLP techniques, DoME allows users to interact with databases effortlessly, eliminating the need for complex CRUD commands. Users can perform operations such as adding, updating or querying data by simply issuing intuitive commands such as "add a product with name 'Keyboard' and price 150". In addition to basic CRUD operations, DoME offers a range of analytical functionalities to extract insights from data. Currently, a version of the DoME application is also under development, expanding its usability across multiple platforms.

DomE Experiment is an implementation of a reference architecture for creating information systems from the automated evolution of the domain model. The architecture comprises elements that guarantee user access through automatically generated interfaces for various devices, integration with external information sources, data and operations security, automatic generation of analytical information, and automatic control of business processes. All these features are generated from the domain model, which is, in turn, continuously evolved from interactions with the user or autonomously by the system itself.
Thus, an alternative to the traditional software production processes is proposed, which involves several stages and different actors, sometimes demanding a lot of time and money without obtaining the expected result.
With software engineering techniques, self-adaptive systems, and artificial intelligence, it is possible, as will be shown, the integration between design time and execution time, obtaining, directly from the user's actions, the necessary data for the evolution of the domain model. The essential artifacts are built from the domain model, making them available, in real-time and with a good level of security, the primary interfaces for data manipulation by the user.

For additional resources for learning about DoME, please access the [VISION.md](https://github.com/gesad-lab/dome/blob/main/VISION.md) file.

*DoME is currently an experiment and product being developed by undergraduate students at the State University of Ceará (UECE), in the Adaptive and Distributed Software Engineering Group ([GESAD](https://www.instagram.com/gesad.uece/)).

# Labelled test dataset
https://drive.google.com/file/d/1IMckKMW5jZDFPXDdv1kJFw0ye2MEiIG7/view?usp=sharing

<!--
# Demonstration
Access the DoME's Telegram bot at the following link:<br/>
https://t.me/uece_dome_bot
-->

# Installation
## Setup the follow environment variables:
DOME_TELEGRAM_TOKEN=telegram_bot_token<br/>
HUGGINGFACE_TOKEN=huggingface_token<br/>

## Install Microsoft C++ Build Tools<br/>
https://visualstudio.microsoft.com/visual-cpp-build-tools/

## For uses a GPU, install CUDA Toolkit:
https://developer.nvidia.com/cuda-downloads

## Install Requirements
```
pip install -r requirements
```

# Demonstration
[DoME Chatbot - Demonstration Video](https://drive.google.com/file/d/1VWORlVXlQiY2iFF2gspuQnFosYd6wa1x/view?t=1)

# Credits
This project is linked with the Master's Degree Program of the University of State of Ceará (http://www.uece.br/ppgcc/). <br/>
Project Supervisor: PhD Paulo Henrique Maia (https://gesad.github.io/team/paulo-henrique/)<br/>
Project Creator: Anderson Martins Gomes (https://www.linkedin.com/in/amartinsg/)<br/>
Students: Layza Maria Rodrigues Carneiro (www.linkedin.com/in/layzacarneiro), Márcio Gabriel Da Silva Ferreira (https://linkedin.com/in/marciogabrielsf) and Gabriel Luiz Barros De Oliveira.
